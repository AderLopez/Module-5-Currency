#import url lib and json libraries:
import urllib.request
import json

def country(name):
    print(name)
    url = f"https://restcountries.com/v3.1/alpha?codes={name}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    #print(result)
    return result