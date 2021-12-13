import pandas as pd
import requests
# import json
import folium
import os

os.chdir('women_mach_learn')
data = pd.read_csv("Water_Main_Breaks.csv")
print(data.head())

response = requests.get("https://services6.arcgis.com/bdPqSfflsdgFRVVM/arcgis/rest/services/Water_Main_Breaks/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json")
print(response.status_code)

data2 = response.json()
print(str(data2)[:1000])

# data2 = pd.io.json.json_normalize(data2["features"])
# FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead
data2 = pd.json_normalize(data2["features"])
data2.rename(columns={
    'attributes.FID': 'FID',
    'attributes.TNT_NAME': 'TNT_NAME',
    'attributes.date': 'date',
    'attributes.fullDate': 'fullDate',
    'attributes.lat': 'lat',
    'attributes.leakClasss': 'leakClass',
    'attributes.location': 'location',
    'attributes.lon': 'lon',
    'attributes.month': 'month',
    'attributes.week': 'week',
    'attributes.weekday': 'weekday',
    'attributes.year': 'year',
    'geometry.x': 'x',
    'geometry.y': 'y'}, inplace=True)
print(data2.head())

breaks_map = folium.Map(location=[43.0493, -76.1455], zoom_start=12)
# print(type(breaks_map))
# breaks_map
breaks_map.save("E:/xampp/htdocs/temp/python_folium/women_mach_learn1.html")
# http://localhost/temp/python_folium/women_mach_learn1.html

for index, row in data2.iterrows():
  folium.features.CircleMarker([row["lat"],
  row["lon"]], radius=7, fill_color="blue",
  fill_opacity=0.3,
  popup="Location: " +
  str(row['location'])).add_to(breaks_map)

breaks_map.save("E:/xampp/htdocs/temp/python_folium/women_mach_learn2.html")
# http://localhost/temp/python_folium/women_mach_learn2.html
