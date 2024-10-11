import folium
import webbrowser
import os

m = folium.Map([37.55305, 126.92461], zoom_start=12)

folium.Marker(
    location=[37.55305, 126.92461],
    tooltip="Click me!",
    popup="Unv.Hongik",
    icon=folium.Icon(icon="cloud"),
).add_to(m)

folium.Marker(
    location=[37.55305, 126.92461],
    tooltip="Click me!",
    popup="Unv.Hongik",
    icon=folium.Icon(color="green"),
).add_to(m)

path = './data/test3.html'
m.save(path)
webbrowser.open(os.path.realpath(path))


# 위도: 37.55305
# 경도: 126.92461