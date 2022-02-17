from dash import Dash, html, dcc, Input, Output
import altair as alt
import numpy as np
import pandas as pd



# Read in global data
df = pd.DataFrame({
'city' : ['Calgary','Edmonton','Ottawa','Toronto','Vancouver','Victoria','Winnipeg','Montreal'],
'rent_for_one_person' : [852.13, 867.61, 973.04, 1513.37, 1458.08, 1094.24, 752.15, 811.25],
'transportation_public': [122.4, 114.66, 132.68, 161.55, 121.26, 112.91, 118.73, 108.84],
'grocery_for_one_person': [264.62, 252.76, 255.04, 320.84, 309.81, 300.18, 239.9, 294.17],
'entertainment': [268.54, 253.03, 246.92, 274.79, 272.69, 271.41, 242.0, 239.99],
'fitness': [119.49, 104.79, 122.63, 144.16, 89.38, 75.52, 104.8, 77.2],
'utility_bills': [219.95, 243.96, 173.29, 168.38, 135.84, 158.71, 161.73, 132.37],
'shopping': [255.77, 258.11, 287.04, 278.8, 288.83, 292.16, 239.43, 258.76],
'monthly_salary': [3370.22, 2909.53, 3311.32, 2682.07, 2992.85, 2665.73, 2358.51, 2488.06],
'monthly_saving': [1267.32, 814.6, 1120.68, -179.82, 316.97, 360.59, 499.76, 565.49]
})

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