name="yopo"

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
from yopo.dashboard import dashboard


dash_app = JupyterDash(
    external_stylesheets=[
        'https://fonts.googleapis.com/css?family=Lato',
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
    ],
    name='dash-app-1',
)

dash_app.layout = html.Div()

def dash_app_run(df,mode):
    global dash_app
    dash_app = dashboard(df,dash_app)
    dash_app.run_server(mode=mode)

def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()