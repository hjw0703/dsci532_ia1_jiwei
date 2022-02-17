from dash import Dash, html, dcc, Input, Output
import altair as alt
import numpy as np
import pandas as pd



# Read in global data
df = pd.read_csv('~/mds/block5/DSCI_532_IA1/cost_of_living_processed.csv')
df = df[df['country'] == 'Canada']

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='rent_for_one_person',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in df.columns])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(df).mark_bar().encode(
    y='city',
    x=xcol)
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)