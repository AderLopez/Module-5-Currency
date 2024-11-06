#Importing necessary libraries
import urllib.request
import json

def printing_weather():
    #Requesting weather information 
    #After updating the coordinates to cambrian college and adding the API key we have the following:
    #&units=metric, adding it after longitude, retrieves the temperature in Celsius
    Api_key = "4389ff17f08ecf9f478e9a96f5da7950"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=46.529116&lon=-80.939017&units=metric&appid={Api_key}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    print(result)
    #print(f'The current weather is: {data_json['weather']}')

    #Creating variables to be printed:
    description = result['weather'][0]['description']
    temperature = result['main']['temp']

    #print(f'The weather for today has: {description}')
    #print(f'The temperature for today is :{temperature} C')

    #Passing the variables to be shown in HTML
    return description, temperature