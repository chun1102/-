import plotly
import plotly.graph_objs as go
import pandas as pd

pd.set_option('display.width', 200)
pd.set_option('display.max_column', 20)
df = pd.read_csv('dataset/2014-1.csv')
lats = df['pickup_latitude'].tolist()
lngs = df['pickup_longitude'].tolist()
data = [
    go.Scattermapbox(
        lat=lats[:100],
        lon=lngs[:100],
        mode='makers',
        maker=go.scattermapbox.Marker(
            size=9
        )
    )
]
layout = go.Layout(
autosize=True,
hovermode='closest',
mapbox=go.layout.Mapbox(
accesstoken='pk.eyJ1Ijoid2VpaGFuMDUyNSIsImEiOiJjanVtNDN6bHkwN3NiNDRwZ2VmbXF3a291In0.ToEAI9lcYJqON1FXCUBNmw',
bearing=0,
center=go.layout.mapbox.Center(
lat=40.757140,
lon=-73.914617
),
pitch=0,
zoom=10
),
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='Mapbox.html')