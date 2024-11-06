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
    return render_template("Module_5_currency.html")

