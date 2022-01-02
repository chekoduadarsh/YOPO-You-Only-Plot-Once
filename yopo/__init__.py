import json
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import request
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import string
import os
import random
from jupyter_dash import JupyterDash
from yopo.dashboard import dashboardApp
import requests
from pyngrok import ngrok


def dashboard(input=pd.DataFrame(),mode="inline",port=8050, tunnel = ""):
    if tunnel.lower() == "ngrock":
        tunnel = ngrok.connect(port)
        dash_app = JupyterDash(
        external_stylesheets=[
            'https://fonts.googleapis.com/css?family=Lato',
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
        ],
        name='dash-app-1',
        )

        dash_app.layout = html.Div()
        dash_app = dashboardApp(input,dash_app)
        dash_app.run_server(mode=mode,port=port)
    else:
        dash_app = JupyterDash(
        external_stylesheets=[
            'https://fonts.googleapis.com/css?family=Lato',
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
        ],
        name='dash-app-1',
        server_url=tunnel.public_url,
        )

        dash_app.layout = html.Div()
        dash_app = dashboardApp(input,dash_app)
        dash_app.run_server(mode=mode,port=port)

def kill_dashboard(host="localhost", port=8050):
    shutdown_url = "http://{host}:{port}/_shutdown_{token}".format(
        host=host, port=port, token=JupyterDash._token
    )
    try:
        response = requests.get(shutdown_url)
    except Exception as e:
        print(e)
