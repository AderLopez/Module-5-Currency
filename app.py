#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask,render_template, request
app = Flask(__name__)


#Import libraries for Assignment 3
import urllib.request
import json
from get_iss import iss_loc
from get_weather import get_weathers


#Normal path when not using a specific folder:
#@app.route("/")
#def hello():
#    return app.send_static_file("index.html")

#Line of code necessary to change the Path of the templates of HTML since coding in Visual Studio
app = Flask(__name__, template_folder='templates') 


#Calling the index.html that will be the home page.
@app.route('/')
def Index():
    return render_template("index.html")


#Assignment 3 new tab:
@app.route('/assignment_3')
def assignemt_3():
    
    #Importing the libraries necessary:
    from get_iss import iss_loc
    from get_weather import get_weathers
    from get_distance import distances
    from get_reverse_geo import address
    from get_country import country

    #Calling Iss_loc to get ISS latitude and longitude
    data = iss_loc()

    #Getting the latitude and longitude from data
    Iss_latitude, Iss_longitude, url_google = data

        #Additional method to obtain the information:
        #latitude, longitude = data[0],data[1]
    
        #Coordinates for Peru for testing:
        #Iss_latitude= -13.2577
        #Iss_longitude= -76.1413
    
    #Printing in the console the coordinates information:
    print(f"The ISS is located in: {Iss_latitude}, {Iss_longitude}")

    #Getting the weather on the ISS location:
    weather = get_weathers(Iss_latitude, Iss_longitude)

    #Weather is the jason variable that has Variables as temperature and description:
    temp_c = round (weather["main"]['temp'])
    description = weather ["weather"][0]["description"]
    #Printing the values in console as checking point:
    print(f'The temperature is: {temp_c}')
    print(f'The description is: {description}')


    #Calling Reverse Geolocation:
    add = address(Iss_latitude,Iss_longitude)

    #Analysis if the ISS is over water to get the flag of the country where it is:
    if(add["countryCode"] == ""):
        print("The ISS is over water")
        ISS_country = "the Ocean"
        flag_dynamic = "static/images/Ocean.jpg"
    else:
        #Location needs to be in lower case:
        location = add["countryCode"].lower()
        #Checkpoint to see the location
        print(f"The country Code is: {location}")
        flag_dynamic = country(location)[0]["flags"]["png"]
        #Checkpoint to see the flag link
        print(f'The link of the flag is the following: {flag_dynamic}')
        ISS_country = country(location)[0]["name"]["common"]
        #Checkpoint to see the country name
        print(f'The name of the country is: {ISS_country}')

    #Additional code to pass the flag of Peru for this code: 
    location = country("pe")
    flag_static = country("pe")[0]["flags"]["png"]


    #Find the distance between Cambrian College us and the ISS(Using stackoverflow):
    
    #Coordinates found online:
    Sudbury_latitude = 46.5290876
    Sudbury_longitude = -80.9433008

    #Calling the functions to measure the distance between Cambrian and ISS
    distance = distances(Sudbury_latitude, Sudbury_longitude,Iss_latitude, Iss_longitude)
    print(f"The distance between sudbury and ISS is: {distance} in Km")


    return render_template("assignment_3.html", Latitude = Iss_latitude, Longitude = Iss_longitude, Link = url_google,
                           Temperature = temp_c, Description = description,
                           Country_Name = ISS_country ,Flag_static = flag_static,Flag_dynamic = flag_dynamic,
                           Distance = distance )



#Calling the experience webpage
@app.route('/experience')
def experience():
    return render_template("experience.html")

#Calling the skills webpage
@app.route('/skills')
def skills():
    return render_template("skills.html")

#Calling the education webpage
@app.route('/education')
def education():
    return render_template("education.html")

#Calling the licenses webpage
@app.route('/licenses')
def licenses():
    return render_template("licenses.html")


#Calling the BMI calculator as post and get to calculate values taken from user input:
@app.route('/bmi', methods=['POST','GET'])
def bmi():
    
    #This first method evaluates the input from user and return two messages:
    if request.method == 'POST':
        
        #Import the BMI function to calculate the BMI
        import bmi

        #Values obtain from the user:
        height = request.form.get('height')  
        weight = request.form.get('weight') 

        #BMI function returns two values after given the height and weight
        bmi, message = bmi.bmi_calculator(float(weight), float(height))
        
        #Changing the BMI into a message to show in HMTL:
        bmi = f"Yor BMI is {bmi}"

        #Returning the two messages for the user with the calculation and evaluation of BMI.
        return render_template('bmi.html', bmi = bmi, message = message)
    
    #Normal Get request, when there is no information sent:
    elif request.method == 'GET':
      return render_template("bmi.html")


#Calling the weather webpage
@app.route('/weather')
def weather():
    
    #Importing the weather function from a .py file
    import weather 

    #Using the function I get the description for the day and temperature on celcius.
    description, temperature = weather.printing_weather()

    #Returning the variables to be shown in the Webpage in HTML
    return render_template("weather.html", description = description, temperature = temperature)

