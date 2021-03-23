from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather")
root.iconbitmap('C:/Users/Ghanendra/Desktop/gk.ico')
root.geometry("600x100")

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=97FA9A4F-6FAE-4353-8951-D0025835E51E
def Ziplookup():
   # zip.get()
   # zipLbl = Label(root, text=zip.get())
   # zipLbl.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=97FA9A4F-6FAE-4353-8951-D0025835E51E")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"  # green
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "USG":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        lbl = Label(root, text=city + " Air Quality " + str(quality) + " - " + category, font=("Helvetica", 20),
                    background=weather_color)
        lbl.grid(row=1, column=0, columnspan=2)

    except EXCEPTION as e:
        api = "Error...."





zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zb = Button(root, text="Lookup Zipcode", command=Ziplookup)
zb.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()

#[{"DateObserved":"2021-02-03 ","HourObserved":7,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV","Latitude":36.206,"Longitude":-115.223,"ParameterName":"O3","AQI":32,"Category":{"Number":1,"Name":"Good"}},{"DateObserved":"2021-02-03 ","HourObserved":7,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV","Latitude":36.206,"Longitude":-115.223,"ParameterName":"PM2.5","AQI":16,"Category":{"Number":1,"Name":"Good"}},{"DateObserved":"2021-02-03 ","HourObserved":7,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV","Latitude":36.206,"Longitude":-115.223,"ParameterName":"PM10","AQI":12,"Category":{"Number":1,"Name":"Good"}}]