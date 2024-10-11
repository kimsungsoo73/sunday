import folium.map
import folium
import webbrowser
import os

m = folium.map([37.55305, 126.92461], zoom_start=12)

folium.Circle(
    location=[37.55305, 126.92461],
    radius = 2000,
    color = 'RED',
    fill = False,
    tooltip="Click me!"
    # popup="Unv.Hongik",
    # icon=folium.Icon(icon="cloud"),
).add_to(m)

folium.CircleMarker(
    location=[37.55305, 126.92461],
    radius = 50,
    color = '#abcdef',
    fill = True,
    fillcolor = '#abcdef',
    tooltip="홍대 입구!"
    # popup="Unv.Hongik",
    # icon=folium.Icon(color="green"),
).add_to(m)

path = './data/test3.html'
m.save(path)
webbrowser.open(os.path.realpath(path))


# 위도: 37.55305
# 경도: 126.92461