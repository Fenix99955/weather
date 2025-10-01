from flask import Flask, render_template, request, make_response
import requests

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['X-Frame-Options'] = 'ALLOWALL'
    return response

@app.route("/", methods=["GET"])
def index():
    city = request.args.get("city", "Kolkata")  # Default city
    weather_data = None
    error = None
    try:
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=15d647987f3b46c29df112844252409&q={city}&aqi=yes")
        data = response.json()
        if "error" in data:
            error = data["error"].get("message", "Unknown error")
        else:
            weather_data = {
                "temp_c": data["current"]["temp_c"],
                "condition_text": data["current"]["condition"]["text"],
                "feelslike_c": data["current"]["feelslike_c"],
                "location": f"{data['location']['name']}, {data['location']['region']}, {data['location']['country']}",
                "localtime": data["location"]["localtime"],
                "humidity": data["current"]["humidity"],
                "wind_kph": data["current"]["wind_kph"],
                "pressure_mb": data["current"]["pressure_mb"],
                "cloud": data["current"]["cloud"],
                "precip_mm": data["current"]["precip_mm"],
                "uv": data["current"]["uv"],
                "co": data["current"]["air_quality"].get("co", "N/A"),
                "no2": data["current"]["air_quality"].get("no2", "N/A"),
                "o3": data["current"]["air_quality"].get("o3", "N/A"),
                "so2": data["current"]["air_quality"].get("so2", "N/A"),
                "pm2_5": data["current"]["air_quality"].get("pm2_5", "N/A"),
                "pm10": data["current"]["air_quality"].get("pm10", "N/A"),
                "us_epa_index": data["current"]["air_quality"].get("us-epa-index", "N/A"),
                "gb_defra_index": data["current"]["air_quality"].get("gb-defra-index", "N/A"),
                "icon": data["current"]["condition"]["icon"],
            }
    except Exception as e:
        error = str(e)

    return render_template(
        "index.html",
        error=error,
        **(weather_data or {})
    )

if __name__ == "__main__":
    app.run(debug=True)
