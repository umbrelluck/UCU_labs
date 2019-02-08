from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='myapplication',timeout=3)
location = geolocator.geocode("Chicago Illinois")
print(location.address)