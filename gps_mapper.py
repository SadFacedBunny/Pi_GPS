import pandas as pd

drives = pd.read_csv("GPS_DRIVES.csv")
drives = drives.query("drive_name in ['GPS_DRIVE1','GPS_DRIVE2']")

import plotly.express as px
print(drives)

fig = px.line_mapbox(drives, lat="lat", lon="lon", color="drive_name", zoom=10, height=800)

fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=13, mapbox_center_lat = 49.736, mapbox_center_lon = 12.128,
    margin={"r":0,"t":0,"l":0,"b":0})

fig.show()


