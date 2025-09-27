from flask import Flask, render_template

import json
import requests
loc=str(input("enter location"))
response=requests.get("http://api.weatherapi.com/v1/current.json?key=15d647987f3b46c29df112844252409&q=%s&aqi=yes"%(loc))
data=response.json()

location=(data["location"]["name"],
          data["location"]["region"],
          data["location"]["country"],
          data["location"]["lat"],
          data["location"]["lon"],
          data["location"]["tz_id"],
          data["location"]["localtime_epoch"],
          data["location"]["localtime"])



#current[]
last_updated_epoch=data["current"]["last_updated_epoch"]
last_updated=data["current"]["last_updated"]
temp_c=data["current"]["temp_c"]
temp_f=data["current"]["temp_f"]
is_day=data["current"]["is_day"]


#current[condition][]
text=data["current"]["condition"]["text"]
icon=data["current"]["condition"]["icon"]
code=data["current"]["condition"]["code"]


#current[]
wind_mph=data["current"]["wind_mph"]
wind_kph=data["current"]["wind_kph"]
wind_degree=data["current"]["wind_degree"]
wind_dir=data["current"]["wind_dir"]
pressure_mb=data["current"]["pressure_mb"]
pressure_in=data["current"]["pressure_in"]
precip_mm=data["current"]["precip_mm"]
precip_in=data["current"]["precip_in"]
humidity=data["current"]["humidity"]
cloud=data["current"]["cloud"]
feelslike_c=data["current"]["feelslike_c"]
feelslike_f=data["current"]["feelslike_f"]
windchill_c=data["current"]["windchill_c"]
windchill_f=data["current"]["windchill_f"]
heatindex_c=data["current"]["heatindex_c"]
heatindex_f=data["current"]["heatindex_f"]
dewpoint_c=data["current"]["dewpoint_c"]
dewpoint_f=data["current"]["dewpoint_f"]
vis_km=data["current"]["vis_km"]
vis_miles=data["current"]["vis_miles"]
uv=data["current"]["uv"]
gust_mph=data["current"]["gust_mph"]
gust_kph=data["current"]["gust_kph"]


# current[airqualty][]
co=data["current"]["air_quality"]["co"]
no2=data["current"]["air_quality"]["no2"]
o3=data["current"]["air_quality"]["o3"]
so2=data["current"]["air_quality"]["so2"]
pm2_5=data["current"]["air_quality"]["pm2_5"]
pm10=data["current"]["air_quality"]["pm10"]
us_epa_index=data["current"]["air_quality"]["us-epa-index"]
gb_defra_index=data["current"]["air_quality"]["gb-defra-index"]

 
#current[]
short_rad=data["current"]["short_rad"]
diff_rad=data["current"]["diff_rad"]
dni=data["current"]["dni"]
gti=data["current"]["gti"]


print(location)




app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

if __name__== "__main__":
    app.run()
