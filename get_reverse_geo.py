#import url lib and json libraries:
import urllib.request
import json

def address(latitude, longitude):
    Api_key ="bdc_7df9dcb6123345da81e83e2a78d3c236"
    url = f"https://api-bdc.net/data/reverse-geocode?latitude={latitude}&longitude={longitude}&localityLanguage=en&key={Api_key}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    return result