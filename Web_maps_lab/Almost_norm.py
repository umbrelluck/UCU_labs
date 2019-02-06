import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='specify_your_app_name_here', timeout=3)
from geopy.extra.rate_limiter import RateLimiter


def readFile(year, path="locations.list"):
    diction = {}
    count = 0
    with open(path, "r", errors="replace") as input_file:
        for line in input_file:
            while count < 15:
                count += 1
                continue
            if year in line:
                tmp = line.strip().split("\t")
                try:
                    ind = tmp[-1].index("(")
                    place = tmp[-1][:ind]
                except ValueError:
                    place = tmp[-1]
                ind = tmp[0].index("(")
                if place in diction:
                    diction[place].append(tmp[0][:ind])
                else:
                    diction[place] = [tmp[0][:ind]]
    return diction
    # leng = 0
    # for key in diction:
    #     leng += len(diction[key])
    # return leng


if __name__ == "__main__":
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)
    year = input("Enter your year: ")
    places = readFile(year)

    mapMov = folium.Map(tiles="Mapbox Control Room")
    fg_USA = folium.FeatureGroup(name="USA")
    fg_UA = folium.FeatureGroup(name="UA")
    fg_world = folium.FeatureGroup(name="Whole world")

    for loc in places:
        try:
            location = geolocator.geocode(loc)
            if location is None:
                continue
            films = ''.join(elem + " --- " for elem in places[loc])
            fg_world.add_child(
                folium.Marker(location=[location.latitude, location.longitude], popup=films, icon=folium.Icon()))
        except Exception:
            continue
    fg_pp = folium.FeatureGroup(name="Population")
    fg_pp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {
        'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties'][
            'POP2005'] < 20000000 else 'red'}))

    # mapMov.add_child(fg_USA)
    # mapMov.add_child(fg_UA)
    mapMov.add_child(fg_world)
    mapMov.add_child(fg_pp)
    mapMov.save('Map_movies_new.html')
