# Produces a page with stock price graph and company select box, using Plotly Dash
# IMPORTANT:
# MAY HAVE TO RUN THE FOLLOWING FIRST IN THE PROJECT DIRECTORY TO SET THE PYTHON ENVIRONMENT:
#   source env/bin/activate
# run locally with:  gunicorn graph:server --reload -b :8000
# Note: there are two unrelated demos going on here, 
# 1) flask_restful endpoints demo
# 2) Plot.ly Dash demo graph
# TODO: how to properly run debug mode? is "development" same as debug mode?

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import os
import json
from nltk import FreqDist
import my_nlp

# TODO: in a real production app, i would ideally want to load this data
# from either the local server or AWS S3

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

app = dash.Dash('app')
server = app.server
api = Api(server)

class HelloWorld(Resource):
    def get(self):
        test_records = [{"id": 1, "name": "david"}, {"id": 2, "name": "Will"}]
        return test_records

    def post(self):
        json_data = request.get_json(force=True)
        # Do a NLP operation on the payload (Frequency distribution of words)
        # In Postman, do a POST with "raw" and JSON (application/json) and make the 
        # payload like this: { "id": 1, "payload": "Here is some text to process."}
        payload = json_data['payload']
        print(my_nlp.distfreq(payload))
        return {"foo":"bar"}

api.add_resource(HelloWorld, '/hello')

# Shows how to get secrets
server.secret_key = os.environ.get('secret_key', 'secret')

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

app.title = "Plot.ly Dash app running in gunicorn"
app.layout = html.Div([
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'},
            {'label': 'Coke', 'value': 'COKE'}
        ],
        value='TSLA'
    ),
    dcc.Graph(id='my-graph')
], className="container")

@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    dff = df[df['Stock'] == selected_dropdown_value]
    return {
        'data': [{
            'x': dff.Date,
            'y': dff.Close,
            'line': {
                'width': 3,
                'shape': 'spline'
            }
        }],
        'layout': {
            'margin': {
                'l': 30,
                'r': 20,
                'b': 30,
                't': 20
            }
        }
    }


# TODO: do i need this? there's a line like this in wsgi.py also, not sure which is needed
if __name__ == '__main__':
    app.run_server(debug=True)


