import opencage
import phonenumbers
from myphone import number
from phonenumbers import geocoder, carrier
from pprint import pprint  # Import the pprint module
from opencage.geocoder import OpenCageGeocode
import folium

default_region = "IN"
pepnumber = phonenumbers.parse(number, default_region)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_pro = phonenumbers.parse(number, default_region)
print(carrier.name_for_number(service_pro, "en"))

key = '5a7a3a47c39e4670b5b5af66358864bc'
geocoder = OpenCageGeocode(key)
query = str(location)

try:
    results = geocoder.geocode(query)
    pprint(results)  # Use pprint to print results in a readable format
except UnicodeEncodeError as e:
    print(f"UnicodeEncodeError: {e}")


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

mymap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(mymap)

mymap.save("mylocation2.html")