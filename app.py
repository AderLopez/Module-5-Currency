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
@app.route('/', methods=['POST','GET'])
def Index():
    import Crytocurrency
    Crytocurrency.cryptocurrency()

    current_rate_btc,current_rate_jpy, current_date = Crytocurrency.Bitcoin_rate()
    return render_template("Module_5_currency.html",Current_date = current_date, Current_rate_BTC = current_rate_btc, Current_rate_JPY = current_rate_jpy )

