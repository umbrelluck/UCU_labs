import folium
import geocoder


def find(where, what, loc, fg_USA, fg_UA, fg_world):
    try:
        loc = list(map(float, loc))
    except:
        return None
    if "USA" in where or "US" in where:
        fg_USA.add_child(
            folium.Marker(location=[loc[0], loc[1]], popup=what, icon=folium.Icon(icon_color="#008000")))
    elif "UA" in where:
        fg_UA.add_child(
            folium.Marker(location=[loc[0], loc[1]], popup=what, icon=folium.Icon(icon_color="#FFFF00")))
    else:
        fg_world.add_child(
            folium.Marker(location=[loc[0], loc[1]], popup=what, icon=folium.Icon()))


def createMap(year):
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
                    loc = geocoder.yandex(tmp[-2])
                    assert loc is not None
                    find(tmp[-2], tmp[0], loc.latlng, fg_USA, fg_UA, fg_world)
                    count += 1
                else:
                    loc = geocoder.yandex(tmp[-1])
                    assert loc is not None
                    find(tmp[-1], tmp[0], loc.latlng, fg_USA, fg_UA, fg_world)
                    count += 1
            if count >= 1000000:
                break
        except EOFError:
            break
        except UnicodeDecodeError:
            pass
        except AttributeError:
            pass
        except AssertionError:
            pass
    input_file.close()
    mapMov.add_child(fg_USA)
    mapMov.add_child(fg_UA)
    mapMov.add_child(fg_world)
    mapMov.save('Map_movies2.html')


def getLocation(place):
    return geocoder.yahoo(place)


if __name__ == "__main__":
    year = input("Enter you year: ")
    createMap(year)
