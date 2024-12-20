import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import pandas as pd
import numpy as np
import plotly.express as px

# Inicializando o Dash
load_figure_template("darkly")

app = dash.Dash(
    external_stylesheets=[dbc.themes.DARKLY]
)
server = app.server

# Carregando os dados
file_path = os.path.join(os.path.dirname(__file__), 'supermarket_sales.csv')
df_data = pd.read_csv(file_path)
df_data['Date'] = pd.to_datetime(df_data['Date'])

# Layout da aplicação
app.layout = html.Div(
    children=[
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    html.H2('ASIMOV', style={'padding_top': '20px'}),
                    html.Hr(),
                    html.H5('Cidades,', style={'margin-top':'10px'}),
                    dcc.Checklist(
                        df_data['City'].value_counts().index,
                        df_data['City'].value_counts().index,
                        inline=False,
                        id='check_city',
                        inputStyle={"margin-right": "5px", "margin-left": "20px",'margin-top':'10px'}
                    ),
                    html.H5('Variável de análise', style={'margin-top':'10px'}),
                    dcc.RadioItems(
                        options=['gross income', 'Rating'],
                        value='gross income',
                        id='main_variable',
                        inline=False,
                        inputStyle={"margin-right": "5px", "margin-left": "20px",'margin-top':'10px'}
                    ),
                ], style={'padding': '20px', 'height': '90vh', 'margin': '20px'})
            ], sm=2),
            dbc.Col([
                dbc.Row([
                    dbc.Col([dcc.Graph(id='city-fig')], sm=4),
                    dbc.Col([dcc.Graph(id='gender_fig')], sm=4),
                    dbc.Col([dcc.Graph(id='pay-fig')], sm=4),
                ]),
                dbc.Row([dcc.Graph(id='income_per_date_fig')]),
                dbc.Row([dcc.Graph(id='income_per_product_fig')]),
            ], sm=10)
        ])
    ]
)

# Callback para atualizar os gráficos
@app.callback(
    [
        Output(component_id='city-fig', component_property='figure'),
        Output(component_id='pay-fig', component_property='figure'),
        Output(component_id='gender_fig', component_property='figure'),
        Output(component_id='income_per_date_fig', component_property='figure'),
        Output(component_id='income_per_product_fig', component_property='figure')
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
    df_gender = df_filtered.groupby(["Gender", "City"])[main_variable].apply(operation).to_frame().reset_index()
    df_payment = df_filtered.groupby('Payment')[main_variable].apply(operation).to_frame().reset_index()
    df_income_time = df_filtered.groupby("Date")[main_variable].apply(operation).to_frame().reset_index()
    df_product_income = df_filtered.groupby(['Product line', 'City'])[main_variable].apply(operation).to_frame().reset_index()

    # Gráficos
    fig_city = px.bar(df_city, x='City', y=main_variable, title='Análise por Cidade')
    fig_payment = px.bar(df_payment, y='Payment', x=main_variable, title='Análise por Método de Pagamento', orientation="h")
    fig_gender = px.bar(df_gender, y=main_variable, x="Gender",title='Análise por Genero', color="City", barmode="group")
    fig_product_income = px.bar(df_product_income, x=main_variable, y='Product line', color="City",
                                title='Análise por Produto', orientation="h", barmode="group")
    fig_income_date = px.bar(df_income_time, y=main_variable, x="Date")

    # Ajuste das legendas e margens
    for fig in [fig_city, fig_payment, fig_gender]:
        fig.update_layout(
            legend=dict(
                yanchor="top",
                y=0.9,
                xanchor="left",
                x=0.1
            ),
            margin=dict(l=10, r=10, t=80, b=50)
        )

    fig_product_income.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=500)
    fig_income_date.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=200)

    return fig_city, fig_payment, fig_gender, fig_income_date, fig_product_income


# Executando o servidor
if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
