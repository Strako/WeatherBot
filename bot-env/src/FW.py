# Imports request and json parse library
import requests
import json

class FetchWeather:
    KELVIN_TO_CELCIUS = 273.15 #Constat for unit conversion
    temp = 0


    @staticmethod
    def getWeather(state):
        w_url = "https://api.openweathermap.org/data/2.5/weather?q=" + state +"&appid=c5b301810a55cb0bbfc76fd009e4d5a5"#url
        w_resp= requests.get(w_url)#make request like Curl
        w_data = w_resp.json()#Parse the http request into JSON
        return w_data

    @staticmethod
    def getTemp(w_data):
        temp = (w_data['main']['temp']) - FetchWeather.KELVIN_TO_CELCIUS #Converts the retrieved temp from K to C
        return temp

    @staticmethod
    def replaceChar(state):#Replace all de blank spaces in a string with '+' sign and returns it
        resultState = ""
        for i in state:
            if i != " ":
                resultState += i
            else:
                resultState += "+"
        return resultState
