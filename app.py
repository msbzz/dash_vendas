import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

import plotly.express as px

# Inicializando o Dash
app = dash.Dash(__name__)
server = app.server

# Carregando os dados
file_path = os.path.join(os.path.dirname(__file__), 'supermarket_sales.csv')
df_data = pd.read_csv(file_path)
df_data['Date'] = pd.to_datetime(df_data['Date'])

# Layout da aplicação
app.layout = html.Div(
    children=[
        html.H5('Cidades'),
        dcc.Checklist(
            df_data['City'].value_counts().index,
            df_data['City'].value_counts().index,
            inline=True,
            id='check_city'
        ),
        html.H5('Variável de análise'),
        dcc.RadioItems(
            options=['gross income', 'Rating'],
            value='gross income',
            id='main_variable',
            inline=True
        ),
        dcc.Graph(id='city-fig'),
        dcc.Graph(id='pay-fig'),
        dcc.Graph(id='income_per_product'),
    ]
)

# Callback para atualizar os gráficos
@app.callback(
    [
        Output(component_id='city-fig', component_property='figure'),
        Output(component_id='pay-fig', component_property='figure'),
        Output(component_id='income_per_product', component_property='figure')
    ],
    [
        Input(component_id='check_city', component_property='value'),
        Input(component_id='main_variable', component_property='value'),
    ]
)
def render_graphs(cities, main_variable):
    # Define se é um somatório ou média
    operation = np.sum if main_variable == 'gross income' else np.mean
    
    # Filtra apenas a lista de cidades
    df_filtered = df_data[df_data['City'].isin(cities)]
    
    
    # Agrupamento por cidade
    df_city = df_filtered.groupby('City')[main_variable].apply(operation).to_frame().reset_index()
	
     
    ## Agrupamento por método de pagamento
    df_payment = df_filtered.groupby('Payment')[main_variable].apply(operation).to_frame().reset_index()
     
    
    # Agrupamento por produto
    df_product_income = df_filtered.groupby(['Product line', 'City'])[main_variable].apply(operation).to_frame().reset_index()
 

    # Gráficos
    fig_city = px.bar(df_city, x='City', y=main_variable, title='Análise por Cidade')
    fig_payment = px.bar(df_payment, y='Payment', x=main_variable,title='Análise por Método de Pagamento', orientation="h") 
    fig_product_income = px.bar(df_product_income, x=main_variable, y='Product line', color="City",title='Análise por Produto', orientation="h", barmode="group")    
    return fig_city, fig_payment, fig_product_income

# Executando o servidor
if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
