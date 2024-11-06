#import url lib and json libraries:
import urllib.request
import json


def iss_loc():
    #Find the ISS(International Space shuttle) located
    #The url provide the latitude and longitude:
    url = "http://api.open-notify.org/iss-now.json"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    #print (result)

    latitude = result['iss_position']['latitude']
    longitude = result['iss_position']['longitude']

    #Will pass this latitude and longitude to google map:
    url_1 = f"https://www.google.ca/maps/place/"+latitude+"+"+longitude
    print(url_1)


    #weather API KEY: 4389ff17f08ecf9f478e9a96f5da7950

    #Find the distance between Cambrian College() us and the ISS:
    #ISS is not above a country api (country code)
    #The flag of the country

    #Time permit
    #Reverse Geolocation - to the country from the latidude and longitude
    return latitude, longitude,url_1