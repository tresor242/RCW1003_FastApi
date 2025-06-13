import dash
from dash import html, dcc

app = dash.Dash(
    __name__,
    requests_pathname_prefix="/dashboard/"
)

app.layout = html.Div([
    html.Div([
        html.A('Accueil', href='/'),
        "|",
        html.A('Logout', href='/logout'),
    ], style={'marginTop': 25}),
    
    html.H2("Bar Graph"),
    dcc.Graph(
        id="exmpl-1",
        figure={
            "data": [
                {"x": [2, 5, 7], "y": [8, 3, 9], "type": "bar", "name": "exmp1"},
                {"x": [5, 3, 8], "y": [6, 2, 5], "type": "bar", "name": "exmp2"}
            ]
        }
    ),
    
    
    html.H2("Line Graph"),
    dcc.Graph(
        id="exmpl-2",
        figure={
            "data": [
                {"x": [8,10,14], "y": [13,8,1], "type": "line", "name": "exmp3"},
                {"x": [4,20,19], "y": [16,7,2], "type": "line", "name": "exmp4"}
            ]
        }
    ),
    
    
    html.H2("Scatter Graph"),
    dcc.Graph(
        id="exmpl-3",
        figure={
            "data": [
                {"x": [8,10,14,7], "y": [13,8,1,3], "type": "scatter","mode":"markers", "name": "exmp5"},
                {"x": [4,20,19], "y": [16,7,2], "type": "scatter","mode":"markers", "name": "exmp6"}
            ]
        }
    ),
    
    html.H2("Pie Chart"),
    dcc.Graph(
        id="exmpl-4",
        figure={
            "data": [
                {"labels": ["A","B","C","D"], "values": [13,8,1,3], "type": "pie","name": "exmp7"} 
            ]
        }
    ),
    
    
])

server = app.server
