import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MATERIA])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3("Data Entry Form", className="text-center mb-4"),
            
            dbc.Label("Name", className="mb-2"),
            dbc.Input(id="name", placeholder="Enter Name", required=True),
            html.Br(),
            
            dbc.Label("Age", className="mb-2"),
            dbc.Input(id="age", placeholder="Enter Age", type="number"),
            html.Br(),
            
            dbc.Label("Title", className="mb-2"),
            dbc.Input(id="title", placeholder="Enter Title", required=True),
            html.Br(),
            
            dbc.Label("Hometown", className="mb-2"),
            dbc.Input(id="hometown", placeholder="Enter Hometown"),
            html.Br(),
            
            dbc.Button("Submit", id="submit-btn", className="btn btn-primary mt-3 mb-4")
        ], md=6),
    ], justify="center"),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.H3("Confirmation", className="text-center mb-4"),
            html.Div(id="confirmation", className="text-center mb-4")
        ])
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.H3("Previous Entries", className="text-center mb-4"),
            dash_table.DataTable(id="table",
                                 columns=[{"name": "Name", "id": "name"},
                                          {"name": "Age", "id": "age"},
                                          {"name": "Title", "id": "title"},
                                          {"name": "Hometown", "id": "hometown"}],
                                 data=[],
                                 page_size=10,
                                 style_table={'height': '300px', 'overflowY': 'auto'},
                                 style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
                                 style_cell={
                                     'backgroundColor': 'rgb(250, 250, 250)',
                                     'whiteSpace': 'normal'}
                                 )
        ])
    ])
], fluid=True, className="mt-4")


@app.callback(
    [Output("confirmation", "children"),
     Output("table", "data")],
    [Input("submit-btn", "n_clicks")],
    [State("name", "value"),
     State("age", "value"),
     State("title", "value"),
     State("hometown", "value"),
     State("table", "data")]
)
def update_data(n, name, age, title, hometown, data):
    if not n:
        return dash.no_update, dash.no_update

    if not name or not title:
        return dbc.Alert("Name and Title are required!", color="danger"), dash.no_update

    entry = {"name": name, "age": age, "title": title, "hometown": hometown}
    data.append(entry)
    
    confirmation_msg = [
        html.Div(f"Name: {name}"),
        html.Div(f"Age: {age}"),
        html.Div(f"Title: {title}"),
        html.Div(f"Hometown: {hometown}")
    ]
    return confirmation_msg, data


if __name__ == "__main__":
    app.run_server(debug=True)
