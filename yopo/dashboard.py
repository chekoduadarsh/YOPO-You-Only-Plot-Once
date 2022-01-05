"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
from dash import dash_table
from dash import dcc
import plotly.express as px
import json 
from dash import html
import dash_daq as daq
from dash.dependencies import Input, Output, State
import string
import random
import dash_trich_components as dtc
import urllib.parse
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


#yolo_plot_df = pd.DataFrame()

def dashboardApp(df, dash_app):
    """Create a Plotly Dash dashboard."""    

    dropdowns = []



    plot_theme = "plotly_dark"
    tab_style = {
        'borderBottom': '1px solid #d6d6d6',
        'padding': '6px',
        'fontWeight': 'bold',
        'backgroundColor': 'black',
        'color': 'white',
    }

    dropdown_style = {
        'fontWeight': 'bold',
        'backgroundColor': 'black',
        'color': 'white',
    }

    tab_selected_style = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#119DFF',
        'color': 'white',
        'padding': '6px'
    }

    
    not_mandatory_font_style = {"color":"blue"}
    mandatory_font_style = {"color":"red"}
    mandatory_div_style = { "margin-left": "1%", "width":"48%", "display":"inline-grid"}
    only_mandatory_div_style = { "margin-left": "1%", "width":"98%", "margin-right": "1%","display":"inline-grid"}
    not_mandatory_div_style = {"margin-left": "2%", "border-spacing":"2px",  "width":"48%", "display":"inline-grid"}
    left_indent_style = {"margin-left": "1%",}

    
    for column in df.columns:
        dropdowns.append({"label":column, "value":column})
    barmode = [{"label":"stack", "value":"stack"},{"label":"group", "value":"group"}]

    regressioon_Algos = [{"label":"Ordinary least squares", "value":"ols"},
                        {"label":"Locally WEighted Scatterplot Smoothing", "value":"lowess"},
    #                    {"label":"5-Point Moving Averages", "value":"rolling"},
    #                    {"label":"5-point Exponentially Weighted Moving Average", "value":"ewm"},
                        {"label":"Expanding Mean", "value":"expanding"},]
    # Custom HTML layout

    # Create Layout
    dash_app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1',  children=[

        dcc.Tab(label='DataFrame View', value='tab-1' , style=tab_style, selected_style=tab_selected_style, children = [    
            create_data_table(df)
        ]),
        dcc.Tab(label='Basic Plots', value='tab-basic' , style=tab_style, selected_style=tab_selected_style, children = [           
            dcc.Tabs(id="tabs-basic",  children=[
                dcc.Tab(label='Scatter Plot', value='tab-2' , style=tab_style, selected_style=tab_selected_style, children = [

                    html.Div( id='input-scatter-mandatory', style = mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-x-scatter', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-scatter', options=dropdowns,placeholder='Enter Y axis Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),

                    html.Div( id='input-scatter-not-mandatory',style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-scatter', options=dropdowns, placeholder='Enter Color axis Value'),
                    dcc.Dropdown(id='input-size-scatter', options=dropdowns, placeholder='Enter Size axis Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),
                
                    
                    dbc.Button(id='submit-button-scatter',  color="success" ,n_clicks=0, children='Submit', style = left_indent_style),

                    html.Div(id='output-state-scatter', children = [], style = left_indent_style),
                ]),

                dcc.Tab(label='Line Plot', value='tab-3' , style=tab_style, selected_style=tab_selected_style, children = [

                    html.Div( id='input-line-mandatory',style = mandatory_div_style,  children = [  
                    dcc.Dropdown(id='input-x-line', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-line', options=dropdowns, placeholder='Enter Y axis Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),

                    html.Div( id='input-line-not-mandatory',style = not_mandatory_div_style,  children = [                    
                    dcc.Dropdown(id='input-color-line', options=dropdowns, placeholder='Enter Color axis Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),
                

                    dbc.Button(id='submit-button-line', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-line', children = [],style = left_indent_style),
                ]),

                dcc.Tab(label='Bar Graph', value='tab-4' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-bar-mandatory',style = mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-x-bar', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-bar', options=dropdowns, placeholder='Enter Y axis Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),
                    html.Div( id='input-bar-not-mandatory',style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-bar', options=dropdowns, placeholder='Enter Color axis Value'),
                    dcc.Dropdown(id='input-barmode-bar', options=barmode, placeholder='Enter BarMode'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-bar', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-bar', children = [],style = left_indent_style),
                ]),

               dcc.Tab(label='Pie Chart', value='tab-pie' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-pie-mandatory',style = mandatory_div_style,  children = [  
                    dcc.Dropdown(id='input-x-pie', options=dropdowns, placeholder='Enter X axis Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),
                    html.Div( id='input-pie-not-mandatory',style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-names-pie', options=dropdowns, placeholder='Enter names Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-pie', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-pie', children = [], style = left_indent_style),
                ]),
                dcc.Tab(label='Tree Map', value='tab-6' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-tree-mandatory',style = mandatory_div_style,  children = [  
                    dcc.Dropdown(id='input-x-tree', options=dropdowns, placeholder='Enter Tree Path', multi=True),
                    dcc.Dropdown(id='input-value-tree', options=dropdowns, placeholder='Enter Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),
                    html.Div( id='input-tree-not-mandatory',style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-tree', options=dropdowns, placeholder='Enter Color Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-tree', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-tree', children = [], style = left_indent_style),
                ]),

                dcc.Tab(label='Sunburst Chart', value='tab-7' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-sunburst-mandatory',style = mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-x-sun', options=dropdowns, placeholder='Enter Chart Path', multi=True),
                    dcc.Dropdown(id='input-value-sun', options=dropdowns, placeholder='Enter Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),
                    html.Div( id='input-sunburst-not-mandatory',style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-sun', options=dropdowns, placeholder='Enter Color Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-sun', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-sun', children = [], style = left_indent_style),
                ]),
            ]),
        ]),
        dcc.Tab(label='Statistical Plots', value='tab-stat' , style=tab_style, selected_style=tab_selected_style, children = [           
            dcc.Tabs(id="tabs-stat", children=[
                dcc.Tab(label='Box Plot', value='tab-8' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-box-mandatory',style = mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-x-box', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-box', options=dropdowns, placeholder='Enter Y axis Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),
                    html.Div( id='input-box-not-mandatory', style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-box', options=dropdowns, placeholder='Enter Color axis Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-box', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-box', children = [], style = left_indent_style),
                ]),

                dcc.Tab(label='Histogram', value='tab-9' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-hist-madatory',style = mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-x-hist', options=dropdowns, placeholder='X axis value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),
                    html.Div( id='input-hist-not-madatory', style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-hist', options=dropdowns, placeholder='Enter Color Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-hist', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-hist', children = [],style = left_indent_style),
                ]),


                dcc.Tab(label='HeatMap', value='tab-10' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-heatmap-mandatory',style = mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-x-heat', options=dropdowns, placeholder='X axis value'),
                    dcc.Dropdown(id='input-y-heat', options=dropdowns, placeholder='Y axis value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),
                    html.Div( id='input-heatmap-not-mandatory', style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-heat', options=dropdowns, placeholder='Enter Color Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-heat', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-heat', children = [],style = left_indent_style),
                ]),

                dcc.Tab(label='Violin Plot', value='tab-11' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-violin-mandatory',style = mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-x-violin', options=dropdowns, placeholder='X axis value'),
                    dcc.Dropdown(id='input-y-violin', options=dropdowns, placeholder='Y axis value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),
                    html.Div( id='input-violoin-not-mandatory', style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-violin', options=dropdowns, placeholder='Enter Color Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-violin', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-violin', children = [],style = left_indent_style),
                ]),
            ]),
        ]),
        dcc.Tab(label='Geological Plots', value='tab-geo' , style=tab_style, selected_style=tab_selected_style, children = [  
             dcc.Tabs(id="geo-stat", children=[    
                 #dcc.Tab(label='Map Choropleth Plot', value='tab-map-choropleth' , style=tab_style, selected_style=tab_selected_style, children = [   


                 #]),
                dcc.Tab(label='Map Density Heatmap', value='tab-map-density' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-map-density-mandatory',style = mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-map-density-lat', options=dropdowns, placeholder='Enter Latitude Value'),
                    dcc.Dropdown(id='input-map-density-lon', options=dropdowns, placeholder='Enter Longitude Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),

                    html.Div( id='input-map-density-not-mandatory', style = not_mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-map-density-mag', options=dropdowns, placeholder='Enter Magnitude Value'),
                    dcc.Input(id='input-map-density-radius', placeholder='Enter radius Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-map-density', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-map-density', children = [],style = left_indent_style),


                 ]),
                dcc.Tab(label='Line on Maps Heatmap', value='tab-map-line' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-map-line-mandatory',style = mandatory_div_style, children= [  
                    dcc.Dropdown(id='input-map-line-location', options=dropdowns, placeholder='Enter Loaction Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),

                    html.Div( id='input-map-line-not-mandatory', style = not_mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-map-line-color', options=dropdowns, placeholder='Enter Color Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-map-line', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-map-line', children = [],style = left_indent_style),

                 ]),
                dcc.Tab(label='Scatterplot on Maps', value='tab-map-scatter' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-map-scatter-mandatory',style = mandatory_div_style, children= [  
                    dcc.Dropdown(id='input-map-scatter-location', options=dropdowns, placeholder='Enter Loaction Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    #dcc.Dropdown(id='input-map-scatter-lat', options=dropdowns, placeholder='Enter Latitude Value'),
                    #dcc.Dropdown(id='input-map-scatter-lon', options=dropdowns, placeholder='Enter Longitude Value'), #disabled due to mapbox token
                    ]),

                    html.Div( id='input-map-scatter-not-mandatory', style = not_mandatory_div_style, children = [  
                    dcc.Dropdown(id='input-map-scatter-color', options=dropdowns, placeholder='Enter Color Value'),
                    dcc.Dropdown(id='input-map-scatter-size', options=dropdowns, placeholder='Enter Size Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-map-scatter', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-map-scatter', children = [],style = left_indent_style),

                 ]),
             ]),
        ]) ,         
        dcc.Tab(label='Financial Charts ', value='tab-fin' , style=tab_style, selected_style=tab_selected_style, children = [  
             dcc.Tabs(id="tabs-fin", children=[    
                dcc.Tab(label='Candlestick Chart', value='tab-candlestick' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-candlestick-mandatory',style = only_mandatory_div_style, children= [  
                    dcc.Dropdown(id='input-candlestick-date', options=dropdowns, placeholder='Enter Date Value'),
                    dcc.Dropdown(id='input-candlestick-open', options=dropdowns, placeholder='Enter Open Value'),
                    dcc.Dropdown(id='input-candlestick-high', options=dropdowns, placeholder='Enter High Value'),
                    dcc.Dropdown(id='input-candlestick-low', options=dropdowns, placeholder='Enter Low Value'),
                    dcc.Dropdown(id='input-candlestick-close', options=dropdowns, placeholder='Enter Close Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-candlestick', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-candlestick', children = [],style = left_indent_style),
                 ]),
                 dcc.Tab(label='OHLC Chart', value='tab-ohlc' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-ohlc-mandatory',style = only_mandatory_div_style, children= [  
                    dcc.Dropdown(id='input-ohlc-date', options=dropdowns, placeholder='Enter Date Value'),
                    dcc.Dropdown(id='input-ohlc-open', options=dropdowns, placeholder='Enter Open Value'),
                    dcc.Dropdown(id='input-ohlc-high', options=dropdowns, placeholder='Enter High Value'),
                    dcc.Dropdown(id='input-ohlc-low', options=dropdowns, placeholder='Enter Low Value'),
                    dcc.Dropdown(id='input-ohlc-close', options=dropdowns, placeholder='Enter Close Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),

                    dbc.Button(id='submit-button-ohlc', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-ohlc', children = [],style = left_indent_style),
                 ]),
            ]),
        ]) ,  
        dcc.Tab(label='Scientific Charts ', value='tab-sci' , style=tab_style, selected_style=tab_selected_style, children = [  
             dcc.Tabs(id="tabs-sci", children=[    
                dcc.Tab(label='Ternary Plots', value='tab-ternary' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-ternary-mandatory',style = mandatory_div_style, children= [  
                    dcc.Dropdown(id='input-a-ternary', options=dropdowns, placeholder='Enter A corner Value'),
                    dcc.Dropdown(id='input-b-ternary', options=dropdowns,placeholder='Enter B corner Value'),
                    dcc.Dropdown(id='input-c-ternary', options=dropdowns,placeholder='Enter C corner Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),

                    html.Div( id='input-ternary-not-mandatory', style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-ternary', options=dropdowns, placeholder='Enter Color Value'),
                    dcc.Dropdown(id='input-size-ternary', options=dropdowns, placeholder='Enter Size Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),
                

                    dbc.Button(id='submit-button-ternary', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-ternary', children = [],style = left_indent_style),
                 ]),
                dcc.Tab(label='Polar Charts', value='tab-polar' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-polar-mandatory',style = mandatory_div_style, children= [  
                    dcc.Dropdown(id='input-r-polar', options=dropdowns, placeholder='Enter R Value'),
                    dcc.Dropdown(id='input-theta-polar', options=dropdowns,placeholder='Enter Theta Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),

                    html.Div( id='input-polar-not-mandatory', style = not_mandatory_div_style, children = [                    
                    dcc.Dropdown(id='input-color-polar', options=dropdowns, placeholder='Enter Color Value'),
                    dcc.Dropdown(id='input-size-polar', options=dropdowns, placeholder='Enter Size Value'),
                    dcc.Dropdown(id='input-symbol-polar', options=dropdowns, placeholder='Enter Symbol Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),
                

                    dbc.Button(id='submit-button-polar', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-polar', children = [],style = left_indent_style),
                 ]),
                dcc.Tab(label='Streamtube', value='tab-streamtube' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-streamtube-mandatory',style = only_mandatory_div_style, children= [  
                    dcc.Dropdown(id='input-x-streamtube', options=dropdowns, placeholder='Enter X Value'),
                    dcc.Dropdown(id='input-y-streamtube', options=dropdowns,placeholder='Enter Y Value'),                                  
                    dcc.Dropdown(id='input-z-streamtube', options=dropdowns, placeholder='Enter Z Value'),
                    dcc.Dropdown(id='input-u-streamtube', options=dropdowns, placeholder='Enter U Value'),
                    dcc.Dropdown(id='input-v-streamtube', options=dropdowns, placeholder='Enter V Value'),
                    dcc.Dropdown(id='input-w-streamtube', options=dropdowns, placeholder='Enter W Value'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),
                

                    dbc.Button(id='submit-button-streamtube', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-streamtube', children = [],style = left_indent_style),
                 ]),
            ]),
        ]) , 
        dcc.Tab(label='Trend Line', value='tab-trend' , style=tab_style, selected_style=tab_selected_style, children = [           
            dcc.Tabs(id="tabs-trend", children=[
                dcc.Tab(label='Regressions', value='tab-8' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-12', children = [  
                    dcc.Dropdown(id='input-x-regscatter', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-regscatter', options=dropdowns, placeholder='Enter Y axis Value'),
                    dcc.Dropdown(id='input-reg-regscatter', options=regressioon_Algos, placeholder='Enter Regression Algorithmm'),
                    html.P("* Mandatory Inputs",style = mandatory_font_style),
                    ]),

                    html.Div( id='input-20', children = [                    
                    dcc.Dropdown(id='input-color-regscatter', options=dropdowns, placeholder='Enter Color axis Value'),
                    dcc.Dropdown(id='input-size-regscatter', options=dropdowns, placeholder='Enter Size axis Value'),
                    html.P("* Optional Inputs", style = not_mandatory_font_style),
                    ]),
                

                    dbc.Button(id='submit-button-regscatter', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

                    html.Div(id='output-state-regscatter', children = [],style = left_indent_style),

                ]),
            ]),
        ]),
        dcc.Tab(label='Custom Plots', value='tab-custom' , style=tab_style, selected_style=tab_selected_style, children = [         
            html.Div( id='input-custom-mandatory',children= [  
            dcc.Textarea(id='input-custom-code', placeholder="use variable 'df' as datta frame and export plotly figure to variable 'fig'", style={"margin-left": "1%", "width":"98%", "margin-right": "1%", 'height': 300}),
            ]),
            dbc.Button(id='submit-button-custom', n_clicks=0, children='Submit', color="success" ,style = left_indent_style),

            html.Div(id='output-state-custom', children = [],style = left_indent_style),
        ]),
    ]),
    html.Div(id='tabs-content')
    ])  
    @dash_app.callback(Output('output-state-scatter', 'children'),
              Input('submit-button-scatter', 'n_clicks'),
              State('input-x-scatter', 'value'),
              State('input-y-scatter', 'value'),
              State('input-color-scatter', 'value'),
              State('input-size-scatter', 'value'))
    def update_scatterplot(n_clicks, input1, input2, input3, input4): 
        if str(input1) in df.columns and str(input2) in df.columns:
            if (input4 is None) and (input3 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input4 is None) and not(input3 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), color=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )    

            if not(input4 is None) and (input3 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), size=str(input4),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not(input4 is None) and not(input3 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), color=str(input3), size=str(input4),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

    @dash_app.callback(Output('output-state-line', 'children'),
              Input('submit-button-line', 'n_clicks'),
              State('input-x-line', 'value'),
              State('input-y-line', 'value'),
              State('input-color-line', 'value'))
    def update_lineplot(n_clicks, input1, input2, input3): 
        input4 = None
        if str(input1) in df.columns and str(input2) in df.columns:
            if (input4 is None) and (input3 is None):
                fig = px.line(df, x=str(input1), y=str(input2),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input4 is None) and not(input3 is None):
                fig = px.line(df, x=str(input1), y=str(input2), color=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )    

            if not(input4 is None) and (input3 is None):
                fig = px.line(df, x=str(input1), y=str(input2), size=str(input4),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not(input4 is None) and not(input3 is None):
                fig = px.line(df, x=str(input1), y=str(input2), color=str(input3), size=str(input4),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

    @dash_app.callback(Output('output-state-bar', 'children'),  
              Input('submit-button-bar', 'n_clicks'),
              State('input-x-bar', 'value'),
              State('input-y-bar', 'value'),
              State('input-color-bar', 'value'),
              State('input-barmode-bar', 'value'))
    def update_barplot(n_clicks, input1, input2, input3, input4): 
        if str(input1) in df.columns and str(input2) in df.columns:
            if (input4 is None) and (input3 is None):
                fig = px.bar(df, x=str(input1), y=str(input2),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input4 is None) and not(input3 is None):
                fig = px.bar(df, x=str(input1), y=str(input2), color=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )    

            if not(input4 is None) and (input3 is None):
                fig = px.bar(df, x=str(input1), y=str(input2), barmode=str(input4),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not(input4 is None) and not(input3 is None):
                fig = px.bar(df, x=str(input1), y=str(input2), color=str(input3), barmode=str(input4),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"
    
    @dash_app.callback(Output('output-state-pie', 'children'),  
              Input('submit-button-pie', 'n_clicks'),
              State('input-x-pie', 'value'),
              State('input-names-pie', 'value'))
    def update_pieplot(n_clicks, input1, input2): 
        input4 = None
        if str(input1) in df.columns:
            if (input2 is None):
                fig = px.pie(df, values=str(input1),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not (input2 is None):
                fig = px.pie(df, values=str(input1), names=str(input2),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

    @dash_app.callback(Output('output-state-tree', 'children'),  
              Input('submit-button-tree', 'n_clicks'),
              State('input-x-tree', 'value'),
              State('input-color-tree', 'value'),              
              State('input-value-tree', 'value'))
    def update_treeplot(n_clicks, input1, input2, input3): 
        if not input1 is None:
            if set(input1).issubset(df.columns):
                if (input2 is None) and (input3 is None):
                    fig = px.treemap(df, path=input1,template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )
                if not (input2 is None) and (input3 is None):
                    fig = px.treemap(df, path=input1, color=str(input2),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )
                if (input2 is None) and not(input3 is None):
                    fig = px.treemap(df, path=input1, values=str(input3),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )
                if not (input2 is None) and not(input3 is None):
                    fig = px.treemap(df, path=input1, color=str(input2), values=str(input3),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

    
    @dash_app.callback(Output('output-state-sun', 'children'),  
              Input('submit-button-sun', 'n_clicks'),
              State('input-x-sun', 'value'),
              State('input-color-sun', 'value'),              
              State('input-value-sun', 'value'))
    def update_sunplot(n_clicks, input1, input2, input3): 
        if not input1 is None:
            if set(input1).issubset(df.columns):
                if (input2 is None) and (input3 is None):
                    fig = px.sunburst(df, path=input1,template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )
                if not (input2 is None) and (input3 is None):
                    fig = px.sunburst(df, path=input1, color=str(input2),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )
                if (input2 is None) and not(input3 is None):
                    fig = px.sunburst(df, path=input1, values=str(input3),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )
                if not (input2 is None) and not(input3 is None):
                    fig = px.sunburst(df, path=input1, color=str(input2), values=str(input3),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"


    @dash_app.callback(Output('output-state-box', 'children'),  
              Input('submit-button-box', 'n_clicks'),
              State('input-x-box', 'value'),
              State('input-y-box', 'value'),
              State('input-color-box', 'value'))
    def update_barplot(n_clicks, input1, input2, input3): 
        input4 = None
        if str(input1) in df.columns and str(input2) in df.columns:
            if (input4 is None) and (input3 is None):
                fig = px.box(df, x=str(input1), y=str(input2),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input4 is None) and not(input3 is None):
                fig = px.box(df, x=str(input1), y=str(input2), color=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )    

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"
    
    @dash_app.callback(Output('output-state-hist', 'children'),  
              Input('submit-button-hist', 'n_clicks'),
              State('input-x-hist', 'value'),
              State('input-color-hist', 'value'))
    def update_histogram(n_clicks, input1, input2): 
        if not input1 is None:
            if input1 in df.columns:
                if (input2 is None):
                    fig = px.histogram(df, x=str(input1),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )
                if not (input2 is None):
                    fig = px.histogram(df, x=str(input1), color=str(input2),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

  
    @dash_app.callback(Output('output-state-heat', 'children'),  
              Input('submit-button-heat', 'n_clicks'),
              State('input-x-heat', 'value'),
              State('input-y-heat', 'value'),
              State('input-color-heat', 'value'))
    def update_heatplot(n_clicks, input1, input2, input3): 
        input4 = None
        if not(input1 is None) and not(input2 is None):
            if str(input1) in df.columns and str(input2) in df.columns:
                if (input4 is None) and (input3 is None):
                    fig = px.density_heatmap(df, x=str(input1), y=str(input2),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )
                if (input4 is None) and not(input3 is None):
                    fig = px.density_heatmap(df, x=str(input1), y=str(input2), z=str(input3),template = plot_theme)
                    return dcc.Graph(
                            id='graph-1-tabs',
                            figure=fig
                        )    

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"
   
     
    @dash_app.callback(Output('output-state-violin', 'children'),  
              Input('submit-button-violin', 'n_clicks'),
              State('input-x-violin', 'value'),
              State('input-y-violin', 'value'),
              State('input-color-violin', 'value'))
    def update_violinplot(n_clicks, input1, input2, input3): 
        if not(input1 is None):
            if str(input1) in df.columns:
                    if not(input1 is None) and (input3 is None) and (input2 is None):
                        fig = px.violin(df, y=str(input1),template = plot_theme)
                        return dcc.Graph(
                                id='graph-1-tabs',
                                figure=fig
                            )
                    if not(input1 is None) and (input3 is None) and not(input2 is None):
                        fig = px.violin(df, y=str(input1), x = str(input2),template = plot_theme)
                        return dcc.Graph(
                                id='graph-1-tabs',
                                figure=fig
                            )
                    if not(input1 is None) and not(input3 is None) and (input2 is None):
                        fig = px.violin(df, y=str(input1), color=str(input3),template = plot_theme)
                        return dcc.Graph(
                                id='graph-1-tabs',
                                figure=fig
                            )
                    if not(input1 is None) and not(input3 is None) and not(input2 is None):
                        fig = px.violin(df, y=str(input1), x = str(input2), color=str(input3),template = plot_theme)
                        return dcc.Graph(
                                id='graph-1-tabs',
                                figure=fig
                            )                                                                                                             
        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

    @dash_app.callback(Output('output-state-regscatter', 'children'),
              Input('submit-button-regscatter', 'n_clicks'),
              State('input-x-regscatter', 'value'),
              State('input-y-regscatter', 'value'),
              State('input-color-regscatter', 'value'),
              State('input-size-regscatter', 'value'),              
              State('input-reg-regscatter', 'value'))
    def update_regscatterplot(n_clicks, input1, input2, input3, input4, input5): 
        if str(input1) in df.columns and str(input2) in df.columns:
            if (input4 is None) and (input3 is None) and not(input5 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), trendline=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input4 is None) and not(input3 is None) and not(input5 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), color=str(input3), trendline=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )    

            if not(input4 is None) and (input3 is None) and not(input5 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), size=str(input4), trendline=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not(input4 is None) and not(input3 is None) and not(input5 is None):
                fig = px.scatter(df, x=str(input1), y=str(input2), color=str(input3), size=str(input4), trendline=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

    
    @dash_app.callback(Output('output-state-map-line', 'children'),  
              Input('submit-button-map-line', 'n_clicks'),
              State('input-map-line-location', 'value'),
              State('input-map-line-color', 'value'))
    def update_maplineplot(n_clicks, input1, input2): 
        if str(input1) in df.columns:
            if (input2 is None):
                fig = px.line_geo(df, locations=str(input1),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not (input2 is None):
                fig = px.line_geo(df, locations=str(input1), color=str(input2),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

    
    @dash_app.callback(Output('output-state-map-scatter', 'children'),  
              Input('submit-button-map-scatter', 'n_clicks'),
              State('input-map-scatter-location', 'value'),
              State('input-map-scatter-color', 'value'),
              State('input-map-scatter-size', 'value'))
    def update_mapscatterplot(n_clicks, input1, input2, input3): 
        input4 = None
        input5 = None  #disabled due to mapbox token
        if str(input1) in df.columns and (input4 is None) and (input5 is None):
            if (input2 is None) and (input3 is None):
                fig = px.scatter_geo(df, locations=str(input1),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not (input2 is None) and (input3 is None):
                fig = px.scatter_geo(df, locations=str(input1), color=str(input2),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

            if (input2 is None) and not(input3 is None):
                fig = px.scatter_geo(df, locations=str(input1), size=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not (input2 is None) and not(input3 is None):
                fig = px.scatter_geo(df, locations=str(input1), color=str(input2), size=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

        if str(input4) in df.columns and str(input5) in df.columns and (input1 is None):

            if (input2 is None) and (input3 is None):
                fig = px.scatter_mapbox(df, lat=str(input4),lon=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not (input2 is None) and (input3 is None):
                fig = px.scatter_mapbox(df, lat=str(input4),lon=str(input5), color=str(input2),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

            if (input2 is None) and not(input3 is None):
                fig = px.scatter_mapbox(df, lat=str(input4),lon=str(input5), size=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not (input2 is None) and not(input3 is None):
                fig = px.scatter_mapbox(df, lat=str(input4),lon=str(input5), color=str(input2), size=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

    @dash_app.callback(Output('output-state-map-density', 'children'),  
              Input('submit-button-map-density', 'n_clicks'),
              State('input-map-density-lat', 'value'),
              State('input-map-density-lon', 'value'),
              State('input-map-density-mag', 'value'),
              State('input-map-density-radius', 'value'))
    def update_mapdensityplot(n_clicks, input1, input2, input3, input4): 
        if str(input1) in df.columns and str(input2) in df.columns:
            if (input3 is None) and (input4 is None):
                fig = px.density_mapbox(df, lat=str(input1), lon=str(input2), zoom=0, mapbox_style="stamen-terrain",template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not (input3 is None) and (input4 is None):
                fig = px.density_mapbox(df,  lat=str(input1), lon=str(input2), z=str(input3), zoom=0, mapbox_style="stamen-terrain",template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

            if (input3 is None) and not(input4 is None):
                fig = px.density_mapbox(df, lat=str(input1), lon=str(input2), radius=float(input4), zoom=0, mapbox_style="stamen-terrain",template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not (input3 is None) and not(input4 is None):
                fig = px.density_mapbox(df, lat=str(input1), lon=str(input2), z=str(input3), radius=float(input4), zoom=0, mapbox_style="stamen-terrain",template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"
 
    @dash_app.callback(Output('output-state-candlestick', 'children'),  
              Input('submit-button-candlestick', 'n_clicks'),
              State('input-candlestick-date', 'value'),
              State('input-candlestick-open', 'value'),
              State('input-candlestick-high', 'value'),
              State('input-candlestick-low', 'value'),
              State('input-candlestick-close', 'value'))
    def update_candlestick(n_clicks, input1, input2, input3, input4, input5): 
        if str(input1) in df.columns and str(input2) in df.columns and str(input3) in df.columns and str(input4) in df.columns and str(input5) in df.columns:
            print("FIGURE")
            fig = go.Figure(data=[go.Candlestick(x=df[str(input1)],
                        open=df[str(input2)],
                        high=df[str(input3)],
                        low=df[str(input4)],
                        close=df[str(input5)])])
            return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"
 
    @dash_app.callback(Output('output-state-ohlc', 'children'),  
              Input('submit-button-ohlc', 'n_clicks'),
              State('input-ohlc-date', 'value'),
              State('input-ohlc-open', 'value'),
              State('input-ohlc-high', 'value'),
              State('input-ohlc-low', 'value'),
              State('input-ohlc-close', 'value'))
    def update_ohlcstick(n_clicks, input1, input2, input3, input4, input5): 
        if str(input1) in df.columns and str(input2) in df.columns and str(input3) in df.columns and str(input4) in df.columns and str(input5) in df.columns:
            print("FIGURE")
            fig = go.Figure(data=[go.Ohlc(x=df[str(input1)],
                        open=df[str(input2)],
                        high=df[str(input3)],
                        low=df[str(input4)],
                        close=df[str(input5)])])
            return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

 
    @dash_app.callback(Output('output-state-ternary', 'children'),
              Input('submit-button-ternary', 'n_clicks'),
              State('input-a-ternary', 'value'),
              State('input-b-ternary', 'value'),
              State('input-c-ternary', 'value'),
              State('input-color-ternary', 'value'),
              State('input-size-ternary', 'value'))
    def update_ternaryplot(n_clicks, input1, input2, input3, input4, input5): 
        if str(input1) in df.columns and str(input2) in df.columns and str(input3) in df.columns:
            if (input4 is None) and (input5 is None):
                fig = px.scatter_ternary(df, a=str(input1), b=str(input2), c=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input4 is None) and not(input5 is None):
                fig = px.scatter_ternary(df, a=str(input1), b=str(input2), c=str(input3), size=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )    

            if not(input4 is None) and (input5 is None):
                fig = px.scatter_ternary(df, a=str(input1), b=str(input2), c=str(input3), color=str(input4),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not(input4 is None) and not(input3 is None):
                fig = px.scatter_ternary(df, a=str(input1), b=str(input2), c=str(input3), color=str(input4), size=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

  
    @dash_app.callback(Output('output-state-polar', 'children'),
              Input('submit-button-polar', 'n_clicks'),
              State('input-r-polar', 'value'),
              State('input-theta-polar', 'value'),
              State('input-color-polar', 'value'),
              State('input-color-polar', 'value'),
              State('input-symbol-polar', 'value'))
    def update_polarplot(n_clicks, input1, input2, input3, input4, input5): 
        if str(input1) in df.columns and str(input2) in df.columns:
            if (input4 is None) and (input5 is None):
                fig = px.scatter_polar(df, r=str(input1), theta=str(input2),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input3 is None) and not(input4 is None) and (input5 is None):
                fig = px.scatter_polar(df, r=str(input1), theta=str(input2), size=str(input4),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )    

            if not(input3 is None) and (input4 is None) and (input5 is None):
                fig = px.scatter_polar(df, r=str(input1), theta=str(input2), color=str(input3),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not(input3 is None) and not(input4 is None) and (input5 is None):
                fig = px.scatter_polar(df, r=str(input1), theta=str(input2), color=str(input3), size=str(input4),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input4 is None) and not(input5 is None):
                fig = px.scatter_polar(df, r=str(input1), theta=str(input2), symbol=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if (input3 is None) and not(input4 is None) and not(input5 is None):
                fig = px.scatter_polar(df, r=str(input1), theta=str(input2), size=str(input4), symbol=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )    

            if not(input3 is None) and (input4 is None) and not(input5 is None):
                fig = px.scatter_polar(df, r=str(input1), theta=str(input2), color=str(input3), symbol=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )
            if not(input3 is None) and not(input4 is None) and not(input5 is None):
                fig = px.scatter_polar(df, r=str(input1), theta=str(input2), color=str(input3), size=str(input4), symbol=str(input5),template = plot_theme)
                return dcc.Graph(
                        id='graph-1-tabs',
                        figure=fig
                    )

        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"

 
    
    @dash_app.callback(Output('output-state-streamtube', 'children'),
              Input('submit-button-streamtube', 'n_clicks'),
              State('input-x-streamtube', 'value'),
              State('input-y-streamtube', 'value'),
              State('input-z-streamtube', 'value'),
              State('input-u-streamtube', 'value'),
              State('input-v-streamtube', 'value'),
              State('input-w-streamtube', 'value'))
    def update_streamtubeplot(n_clicks, input1, input2, input3, input4, input5, input6): 
        if str(input1) in df.columns and str(input2) in df.columns and str(input3) in df.columns and str(input4) in df.columns and str(input5) in df.columns and str(input6) in df.columns:
            fig = go.Figure(data=go.Streamtube(x = df[input1], y = df[input2], z = df[input3], u = df[input4], v = df[input5], w = df[input6]))
            return dcc.Graph(
                    id='graph-1-tabs',
                    figure=fig
                )
        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"


    
    @dash_app.callback(Output('output-state-custom', 'children'),
              Input('submit-button-custom', 'n_clicks'),
              State('input-custom-code', 'value'))
    def update_customplot(n_clicks, input1): 
        if not(input1 is None):
            df
            _locals = locals()
            exec(input1, globals(),_locals)
            return dcc.Graph(
                    id='graph-1-tabs',
                    figure=_locals["fig"]
            )
        return  "Fill the required fields and click on 'Submit' to generate the graph you want!!"
     
    return dash_app


   

def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=300
    )
    return table