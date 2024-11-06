#import url lib and json libraries:
import urllib.request
import json

def get_weathers(latitude, longitude):
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid=4389ff17f08ecf9f478e9a96f5da7950"
    request = urllib.request.urlopen(weather_url)
    result = json.loads(request.read())
    return result