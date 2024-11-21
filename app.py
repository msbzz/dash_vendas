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

df_data['City'].value_counts().index 

#============ Layout ================#

app.layout = html.Div(
    children=[

      html.H5('Cidades'),
      dcc.Checklist(df_data['City'].value_counts().index,
                    df_data['City'].value_counts().index,
                    id='check-city')  

    ]
)

#============ CallBacks ================#



#============ Run server ================#

if __name__ == "__main__":
    app.run_server(port=8050,debug=True)