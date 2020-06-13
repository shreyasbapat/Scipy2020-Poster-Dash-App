# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime
from copy import deepcopy

currentYear = datetime.now().year
external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css',
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, assets_external_path='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js')
app.title = 'SciPy 2020: EinsteinPy'
app.layout = html.Div(
    children=[
    html.Nav(children=[
        html.Div([
            html.A('EinsteinPy', className="brand-logo  black-text", href='#'),
            html.Ul([
                html.Li([
                    html.A('Main Website', href='#', className="black-text"),
                ]),
                html.Li([
                    html.A('Blog', href='#', className="black-text"),
                ]),
                html.Li([
                    html.A('Documentation', href='#', className="black-text"),
                ]),
                html.Li([
                    html.A('Paper', href='#', className="black-text"),
                ]),
                html.Li([
                    html.A('Chatroom', href='#', className="black-text"),
                ]),
                html.Li([
                    html.A('Contact', href='#', className="waves-effect waves-light btn white-text"),
                ]),
            ],
            className="right hide-on-med-and-down  black-text"
            )
        ],
        className="nav-wrapper grey lighten-4")
        ]),
    html.H1(
        children='EinsteinPy : Python for General Relativity',
        style={'text-align': 'center'}
        ),

    dcc.Markdown('Created by [Shreyas Bapat](https://shreyasb.com)'),
    dcc.Markdown('Find out more about the data, get the code, or help improve this figure on [GitHub](https://github.com/gschivley/climate-life-events)')

    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
