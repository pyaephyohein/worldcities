token = open("src/.mapbox_token").read()

import pandas as pd
us_cities = pd.read_csv("src/worldcities.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lng", hover_name="city", hover_data=["city", "city_ascii", "lat" ,"lng" ,"country", "population"], color_discrete_sequence=["fuchsia"], zoom=3, height=1000)
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.update_mapboxes(domain_column=500)
fig.show()