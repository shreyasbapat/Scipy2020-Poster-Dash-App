import dash

app = dash.Dash(__name__)

server = app.server # the Flask app

import os

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css',
    'https://use.fontawesome.com/releases/v5.0.10/css/all.css',
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, assets_external_path='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js')
server = app.server
app.title = 'SciPy 2020: EinsteinPy'
app.layout = html.Div(
    children=[
    html.Nav(children=[
        html.Div([
            html.A([
                html.Img(src="https://raw.githubusercontent.com/einsteinpy/einsteinpy.org/master/img/wordmark.png", style={'height':'10%', 'width':'180px'}),
            ],
            className="brand-logo  black-text", href='#'),
            html.Ul([
                html.Li([
                    html.A('Main Website', href='https://einsteinpy.org', className="black-text"),
                ]),
                html.Li([
                    html.A('Blog', href='https://blog.einsteinpy.org', className="black-text"),
                ]),
                html.Li([
                    html.A('Documentation', href='https://docs.einsteinpy.org', className="black-text"),
                ]),
                html.Li([
                    html.A('Paper', href='https://arxiv.org/abs/2005.11288', className="black-text"),
                ]),
                html.Li([
                    html.A('Chatroom', href='https://chat.einsteinpy.org', className="black-text"),
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
    html.H4(
        children='Welcome to SciPy 2020 Poster on',
        style={'text-align': 'center'}
        ),
    html.Div(
    [
        html.Img(src="https://raw.githubusercontent.com/einsteinpy/einsteinpy.org/master/img/wordmark.png", style={'text-align':'center', 'vertical-align':'middle'}),
    ],
    className="row",
    style={'text-align':'center'}
    ),
    html.H4(
        children='Python for General Relativity',
        style={'text-align': 'center'}
        ),



    html.Footer(
    [
        html.Div(
        [
            html.Div(
            [
                html.Div(
                [
                    html.Img(src="https://raw.githubusercontent.com/einsteinpy/einsteinpy.org/master/img/wordmark.png", style={'text-align':'center', 'width':'300px'}),
                    html.P(
                        ["EinsteinPy is an open source pure Python package dedicated to problems arising in General Relativity and gravitational physics, such as geodesics plotting for Schwarzschild, Kerr and Kerr Newman space-time model, calculation of Schwarzschild radius, calculation of Event Horizon and Ergosphere for Kerr space-time. Symbolic Manipulations of various tensors like Metric, Riemann, Ricci, Ricci Scalar, Weyl, Schouten, Stress-Energy-Momentum, Einstein and Christoffel Symbols is also possible using the library. EinsteinPy also features Hypersurface Embedding of Schwarzschild space-time, which will soon lead to modelling of Gravitational Lensing! It is released under the MIT license."],
                        className="grey-text text-darken-2",
                        style={'text-align':'justify'}
                    ),
                ],
                className="col l6 s12",
                ),
                html.Div(
                [
                    html.H5(
                        children='Important Links',
                        className='grey-text text-darken-3'
                        ),
                    html.Ul([
                        html.Li([
                            html.A('Website', href='https://einsteinpy.org'),
                        ]),
                        html.Li([
                            html.A('Blog', href='https://blog.einsteinpy.org'),
                        ]),
                        html.Li([
                            html.A('Documentation', href='https://docs.einsteinpy.org'),
                        ]),
                        html.Li([
                            html.A('Paper', href='https://arxiv.org/abs/2005.11288'),
                        ]),
                        html.Li([
                            html.A('Chatroom', href='https://chat.einsteinpy.org'),
                        ]),
                        html.Li([
                            html.A('Riot room', href='https://riot.einsteinpy.org'),
                        ]),
                    ],
                    className="grey-text text-darken-3"
                    ),
                    html.H5(
                        children='Summer of Codes',
                        className='grey-text text-darken-3'
                        ),
                    html.Ul([
                        html.Li([
                            html.A('GSoC 2020', href='https://openastronomy.org/gsoc/gsoc2020/'),
                        ]),
                        html.Li([
                            html.A('SOCIS 2019', href='https://blog.einsteinpy.org/2019-04-21-Selection-in-SOCIS-2019/'),
                        ]),
                    ],
                    className="grey-text text-darken-3"
                    ),
                ],
                className="col l4 offset-l2 s12",
                ),
            ],
            className="row",
            ),
        ],
        className="container",
        ),
        html.Div(
        [
            html.Div(
            [
            "© 2020 Shreyas Bapat & The EinsteinPy Project",
            html.A(
            ["Shreyas Bapat"],
            className="grey-text text-lighten-4 right",
            href="https://shreyasb.com"
            )
            ],
            className="container"
            ),
        ],
        className="footer-copyright grey darken-1",
        ),
    ],
    className="page-footer grey lighten-3",
    ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
