import folium
import webbrowser
import os
import time

m = folium.Map((45.5236, -122.6750), tiles="cartodb positron")
path = './data/test2.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
time.sleep(0.5)