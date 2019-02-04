import folium

map = folium.Map(tiles="Mapbox Bright")
map.add_child(folium.Marker(location=[49.817545, 24.023932], popup="Хіба я тут!", icon=folium.Icon()))
map.save("Map1.html")
