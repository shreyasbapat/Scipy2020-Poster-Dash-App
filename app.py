import dash

app = dash.Dash(__name__)

server = app.server # the Flask app

import os

import dash
import dash_core_components as dcc
import dash_html_components as html

import pickle

with open('trajectory.pkl', 'rb') as input:
    obj = pickle.load(input)

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
                    html.A('Contact', href='mailto:shreyas@einsteinpy.org', className="waves-effect waves-light btn white-text"),
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
    html.H6(
        children='Lets Visualize Advancement of Perihelion',
        style={'text-align': 'center'}
        ),

    dcc.Graph(
        id='Perihelion',
        figure=obj.fig,
    ),
    html.Div(
    [
    html.P(
        children="The above geodesic was the biggest question in late 1800s and 1900s.\
         No one was sure why thes type of orbits should appear. Even Sir Isaac Newton knew about\
         such a problem in his theory. Later, Prof. Einstein's theory of general relativity came and solved everything for us.\
         This is a very niche example usecase of EinsteinPy, you can do much much more. ",
        style={'width': '80%', 'text-align': 'center', 'vertical-align': 'middle', 'margin-left':'10%'},
    ),
    html.H4(
            children='About EinsteinPy',
            style={'text-align': 'center'}
            ),
    html.P(
        children="EinsteinPy is an open source pure Python package dedicated to problems arising in General Relativity and gravitational physics, such as geodesics plotting for Schwarzschild, Kerr and Kerr Newman space-time model, calculation of Schwarzschild radius, calculation of Event Horizon and Ergosphere for Kerr space-time. Symbolic Manipulations of various tensors like Metric, Riemann, Ricci, Ricci Scalar, Weyl, Schouten, Stress-Energy-Momentum, Einstein and Christoffel Symbols is also possible using the library. EinsteinPy also features Hypersurface Embedding of Schwarzschild space-time, which will soon lead to modelling of Gravitational Lensing! It is released under the MIT license. ",
        style={'width': '80%', 'text-align': 'center', 'vertical-align': 'middle', 'margin-left':'10%'},
    ),
    ],
    className="row",
    ),

    html.H4(
        children='How we started EinsteinPy?',
        style={'text-align': 'center'}
        ),
    html.A('EinsteinPy Blog', href='https://blog.shreyasb.dev/Kickstarting-EinsteinPy-Part-1/', className="waves-effect waves-light btn white-text", style={'margin-left': '45%'}),

    html.H4(
        children='Example Notebooks on Binder',
        style={'text-align': 'center'}
        ),

    html.A('Run Binder', href='https://beta.mybinder.org/v2/gh/einsteinpy/einsteinpy/0.3.x?filepath=index.ipynb', className="waves-effect waves-light btn white-text", style={'margin-left': '45%'}),
    html.P(
        children="The example notebooks cover a wide variety of topics related to the library like symbolic manipulations, shadow of a black hole, hypersurface of a black hole, Frame dragging etc. Go and check them out now!",
        style={'width': '80%', 'text-align': 'center', 'vertical-align': 'middle', 'margin-left':'10%'},
    ),

    html.H4(
        children='Conventional Poster',
        style={'text-align': 'center'}
        ),
    html.A('PDF Poster', href='https://shreyasb.dev/vishakha/one.pdf', className="waves-effect waves-light btn white-text", style={'margin-left': '45%'}),
    html.P(
        children="Are you fond of conventional posters? Do you like PDF style posters and are not enjoying this? Okay, I got you covered.",
        style={'width': '80%', 'text-align': 'center', 'vertical-align': 'middle', 'margin-left':'10%'},
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
