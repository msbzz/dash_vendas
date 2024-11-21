import os
import dash
from dash import html,dcc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__)
server = app.server

file_path = os.path.join(os.path.dirname(__file__), 'supermarket_sales.csv')

df_data = pd.read_csv(file_path)
df_data['Date']=pd.to_datetime(df_data['Date'])

#============ Layout ================#

app.layout = html.Div(
    children=[

      html.H5('Cidades'),
      dcc.Checklist(df_data['City'].value_counts().index,
                    df_data['City'].value_counts().index,inline=True,
                    id='check_city'),

      html.H5('Variável de análise'),

      dcc.RadioItems(
         options= ['gross income','Rating'],
         value= 'gross income',
         id='main_variable',
         inline=True
          ),    

      html.H5('Por cidade'),
      dcc.Graph(id='city-fig'),
      html.H5('Por pagamentos'),
      dcc.Graph(id='pay-fig'),
      html.H5('Por produtos'),
      dcc.Graph(id='income_per_product'),                

    ]
)

#============ CallBacks ================#

@app.callback(
    #[
      Output(component_id='city-fig', component_property='figure'),
      # Output(component_id='pay-fig', component_property='figure'),
      # Output(component_id='income_per_product', component_property='figure')
    #],
    [
      Input(component_id='check_city', component_property='value'),
      Input(component_id='main_variable', component_property='value'),
    ])
def render_graphs(cities,main_variable):
  
 
  #aqui define se é um somatorio ou media
  operation = np.sum if main_variable=='gross income' else np.mean
  #filtra apenas a lista de cidades
  df_filtered = df_data[df_data['City'].isin(cities)]
  # agrupar por cidade
  df_city = df_filtered.groupby('City')[main_variable].apply(operation).to_frame().reset_index()
    
  fig_city = px.bar(df_city,x='City',y=main_variable)
  
  return fig_city
#============ Run server ================#

if __name__ == "__main__":
    app.run_server(port=8050,debug=True)