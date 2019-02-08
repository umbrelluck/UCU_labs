import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='specify_your_app_name_here', timeout=3)
from geopy.extra.rate_limiter import RateLimiter

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)


def find(where, what, loc, fg_USA, fg_UA, fg_world):
    if "USA" in where or "US" in where:
        fg_USA.add_child(
            folium.Marker(location=[loc.latitude, loc.longitude], popup=what, icon=folium.Icon(icon_color="#008000")))
    elif "UA" in where:
        fg_UA.add_child(
            folium.Marker(location=[loc.latitude, loc.longitude], popup=what, icon=folium.Icon(icon_color="#FFFF00")))
    else:
        fg_world.add_child(
            folium.Marker(location=[loc.latitude, loc.longitude], popup=what, icon=folium.Icon()))


def createMap(year, geolocator):
    mapMov = folium.Map(tiles="Mapbox Control Room")
    input_file = open("locations.list", "rb")
    fg_USA = folium.FeatureGroup(name="USA")
    fg_UA = folium.FeatureGroup(name="UA")
    fg_world = folium.FeatureGroup(name="Whole world")
    count = 0
    while True:
        try:
            line = input_file.readline()
            if year in str(line):
                tmp = line.strip().split(b"\t")
                tmp = [elem.decode("UTF-8") for elem in tmp]
                if tmp[-1].endswith(")"):
                    loc = geolocator.geocode(tmp[-2])
                    find(tmp[-2], tmp[0], loc, fg_USA, fg_UA, fg_world)
                    count += 1
                else:
                    loc = geolocator.geocode(tmp[-1])
                    find(tmp[-1], tmp[0], loc, fg_USA, fg_UA, fg_world)
                    count += 1
            if count >= 50:
                break
        except EOFError:
            break
        except AttributeError:
            pass
    input_file.close()
    mapMov.add_child(fg_USA)
    mapMov.add_child(fg_UA)
    mapMov.add_child(fg_world)
    mapMov.save('Map_movies.html')


def getLcation(place):
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    return geolocator.geocode(place)


if __name__ == "__main__":
    year = input("Enter you year: ")
    createMap(year, geolocator)
