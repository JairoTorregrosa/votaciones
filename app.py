from http import server
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
              size="pop", color="continent", hover_name="country",
                log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(host='0.0.0.0')

    