import pandas as pd
import plotly.express as px  # (version 4.7.0)

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("data/dummy_data.csv")

df.reset_index(inplace=True)
print(df[:5])

day_types = ["Push", "Pull", "Legs"]
compounds = ["Bench Press", "Deadlift", "Back Squat", "OHP", "Barbell Row", "Front Squat"]

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([
    html.H1("Lifting Dashboard", style={'text-align': 'center'}),
    dcc.Dropdown(id="slct_impact",
                 options=[{"label": x, "value":x} for x in day_types],
                 value="Push",
                 multi=False,
                 style={'width': "40%"}
                 ),
    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='weight_progression', figure={})
])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='weight_progression', component_property='figure')],
    [Input(component_id='slct_impact', component_property='value')]
)
def update_graph(option_slctd):
#    print(option_slctd)
#    print(type(option_slctd))
    container = "Selected day-type: {}".format(option_slctd)
    dff = df.copy()
    dff = dff[dff['Day Type'] == option_slctd]
    fig = px.line(
        data_frame=dff,
        x='Date',
        y='Weight',
        template='plotly_dark'
    )
    return container, fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
