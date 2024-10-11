import folium
import webbrowser
import os
import time

# m = folium.Map(location=[37.5564234, 126.9723937], zoom_start = 14)
# m = folium.Map(location=(37.5564234, 126.9723937), zoom_start = 14)
m = folium.Map(location=([37.5564234, 126.9723937]), zoom_start = 14)
path = './data/test1.html'
webbrowser.open(os.path.realpath(path))
m.save(path)
time.sleep(0.5)