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


#yolo_plot_df = pd.DataFrame()

def dashboardApp(df, dash_app):
    """Create a Plotly Dash dashboard."""    

    dropdowns = []


    tab_style = {
    }


    plot_theme = "plotly_dark"

    tab_selected_style = {
    }



    
    for column in df.columns:
        dropdowns.append({"label":column, "value":column})
    barmode = [{"label":"stack", "value":"stack"},{"label":"group", "value":"group"}]

    regressioon_Algos = [{"label":"Ordinary least squares", "value":"ols"},
                        {"label":"Locally WEighted Scatterplot Smoothing", "value":"lowess"},
    #                    {"label":"5-Point Moving Averages", "value":"rolling"},
    #                    {"label":"5-point Exponentially Weighted Moving Average", "value":"ewm"},
                        {"label":"Expanding Mean", "value":"expanding"},]

    # Create Layout
    dash_app.layout = html.Div([

    dcc.Tabs(id="tabs", value='tab-1',  children=[

        dcc.Tab(label='DataFrame View', value='tab-1' , style=tab_style, selected_style=tab_selected_style, children = [    
            create_data_table(df)
        ]),
        dcc.Tab(label='Basic Plots', value='tab-basic' , style=tab_style, selected_style=tab_selected_style, children = [           
            dcc.Tabs(id="tabs-basic",  children=[
                dcc.Tab(label='Scatter Plot', value='tab-2' , style=tab_style, selected_style=tab_selected_style, children = [

                    html.Div( id='input-1', children = [  
                    dcc.Dropdown(id='input-x-scatter', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-scatter', options=dropdowns,placeholder='Enter Y axis Value'),
                    ]),

                    html.Div( id='input-2', children = [                    
                    dcc.Dropdown(id='input-color-scatter', options=dropdowns, placeholder='Enter Color axis Value'),
                    dcc.Dropdown(id='input-size-scatter', options=dropdowns, placeholder='Enter Size axis Value'),
                    ]),
                

                    html.Button(id='submit-button-scatter', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-scatter', children = []),
                ]),

                dcc.Tab(label='Line Plot', value='tab-3' , style=tab_style, selected_style=tab_selected_style, children = [

                    html.Div( id='input-3', children = [  
                    dcc.Dropdown(id='input-x-line', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-line', options=dropdowns, placeholder='Enter Y axis Value'),
                    ]),

                    html.Div( id='input-21', children = [                    
                    dcc.Dropdown(id='input-color-line', options=dropdowns, placeholder='Enter Color axis Value'),
                    ]),
                

                    html.Button(id='submit-button-line', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-line', children = []),
                ]),

                dcc.Tab(label='Bar Graph', value='tab-4' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-4', children = [  
                    dcc.Dropdown(id='input-x-bar', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-bar', options=dropdowns, placeholder='Enter Y axis Value'),
                    ]),
                    html.Div( id='input-22', children = [                    
                    dcc.Dropdown(id='input-color-bar', options=dropdowns, placeholder='Enter Color axis Value'),
                    dcc.Dropdown(id='input-barmode-bar', options=barmode, placeholder='Enter BarMode'),
                    ]),

                    html.Button(id='submit-button-bar', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-bar', children = []),
                ]),

                dcc.Tab(label='Pie Chart', value='tab-5' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-5', children = [  
                    dcc.Dropdown(id='input-x-pie', options=dropdowns, placeholder='Enter X axis Value'),
                    ]),
                    html.Div( id='input-23', children = [                    
                    dcc.Dropdown(id='input-names-pie', options=dropdowns, placeholder='Enter names Value'),
                    ]),

                    html.Button(id='submit-button-pie', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-pie', children = []),
                ]),

                dcc.Tab(label='Tree Map', value='tab-6' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-6', children = [  
                    dcc.Dropdown(id='input-x-tree', options=dropdowns, placeholder='Enter Tree Path', multi=True),
                    dcc.Dropdown(id='input-value-tree', options=dropdowns, placeholder='Enter Value'),
                    ]),
                    html.Div( id='input-24', children = [                    
                    dcc.Dropdown(id='input-color-tree', options=dropdowns, placeholder='Enter Color Value'),
                    ]),

                    html.Button(id='submit-button-tree', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-tree', children = []),
                ]),

                dcc.Tab(label='Sunburst Chart', value='tab-7' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-7', children = [  
                    dcc.Dropdown(id='input-x-sun', options=dropdowns, placeholder='Enter Chart Path', multi=True),
                    dcc.Dropdown(id='input-value-sun', options=dropdowns, placeholder='Enter Value'),
                    ]),
                    html.Div( id='input-25', children = [                    
                    dcc.Dropdown(id='input-color-sun', options=dropdowns, placeholder='Enter Color Value'),
                    ]),

                    html.Button(id='submit-button-sun', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-sun', children = []),
                ]),
            ]),
        ]),
        dcc.Tab(label='Statistical Plots', value='tab-stat' , style=tab_style, selected_style=tab_selected_style, children = [           
            dcc.Tabs(id="tabs-stat", children=[
                dcc.Tab(label='Box Plot', value='tab-8' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-8', children = [  
                    dcc.Dropdown(id='input-x-box', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-box', options=dropdowns, placeholder='Enter Y axis Value'),
                    ]),
                    html.Div( id='input-26', children = [                    
                    dcc.Dropdown(id='input-color-box', options=dropdowns, placeholder='Enter Color axis Value'),
                    ]),

                    html.Button(id='submit-button-box', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-box', children = []),
                ]),

                dcc.Tab(label='Histogram', value='tab-9' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-9', children = [  
                    dcc.Dropdown(id='input-x-hist', options=dropdowns, placeholder='X axis value'),
                    ]),
                    html.Div( id='input-27', children = [                    
                    dcc.Dropdown(id='input-color-hist', options=dropdowns, placeholder='Enter Color Value'),
                    ]),

                    html.Button(id='submit-button-hist', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-hist', children = []),
                ]),


                dcc.Tab(label='HeatMap', value='tab-10' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-10', children = [  
                    dcc.Dropdown(id='input-x-heat', options=dropdowns, placeholder='X axis value'),
                    dcc.Dropdown(id='input-y-heat', options=dropdowns, placeholder='Y axis value'),
                    ]),
                    html.Div( id='input-28', children = [                    
                    dcc.Dropdown(id='input-color-heat', options=dropdowns, placeholder='Enter Color Value'),
                    ]),

                    html.Button(id='submit-button-heat', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-heat', children = []),
                ]),

                dcc.Tab(label='Violin Plot', value='tab-11' , style=tab_style, selected_style=tab_selected_style, children = [    
                    
                    html.Div( id='input-11', children = [  
                    dcc.Dropdown(id='input-x-violin', options=dropdowns, placeholder='X axis value'),
                    dcc.Dropdown(id='input-y-violin', options=dropdowns, placeholder='Y axis value'),
                    ]),
                    html.Div( id='input-29', children = [                    
                    dcc.Dropdown(id='input-color-violin', options=dropdowns, placeholder='Enter Color Value'),
                    ]),

                    html.Button(id='submit-button-violin', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-violin', children = []),
                ]),
            ]),
        ]),
        dcc.Tab(label='Trend Line', value='tab-trend' , style=tab_style, selected_style=tab_selected_style, children = [           
            dcc.Tabs(id="tabs-trend", children=[
                dcc.Tab(label='Regressions', value='tab-8' , style=tab_style, selected_style=tab_selected_style, children = [   

                    html.Div( id='input-12', children = [  
                    dcc.Dropdown(id='input-x-regscatter', options=dropdowns, placeholder='Enter X axis Value'),
                    dcc.Dropdown(id='input-y-regscatter', options=dropdowns, placeholder='Enter Y axis Value'),
                    dcc.Dropdown(id='input-reg-regscatter', options=regressioon_Algos, placeholder='Enter Regression Algorithmm'),
                    ]),

                    html.Div( id='input-20', children = [                    
                    dcc.Dropdown(id='input-color-regscatter', options=dropdowns, placeholder='Enter Color axis Value'),
                    dcc.Dropdown(id='input-size-regscatter', options=dropdowns, placeholder='Enter Size axis Value'),
                    ]),
                

                    html.Button(id='submit-button-regscatter', n_clicks=0, children='Submit'),

                    html.Div(id='output-state-regscatter', children = []),

                ]),
            ]),
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

        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"


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

        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"



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

        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"
    
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
        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"

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

        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"

    
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

        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"


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

        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"
    
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

        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"

  
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

        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"
   
     
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
        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"
   
    @dash_app.callback(
        Output('toggle-switch-output', 'children'),
        Input('toggle-switch', 'value')
    )
    def update_output(value):
        return 'The switch is {}.'.format(value)



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

        return  "Fill the required fields and click on 'Submit' to generate teh graph you want!!"


   
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