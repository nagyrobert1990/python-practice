from flask import Flask, render_template, request
import helper_methods

app = Flask(__name__)


@app.route("/")
def hello():
    city_list =helper_methods.get_cities_from_file()
    return render_template("cities.html", cities = city_list)

@app.route("/city", methods=['GET'])
def get_weather_info():
    actual_city = request.args.get("city") 
    data = helper_methods.get_actual_weather_data(actual_city, "HU")
    temperature = helper_methods.get_temperature_from_data(data)
    icon_id = helper_methods.get_icon_from_data(data)
    return render_template("weather.html", city = actual_city, temperature = temperature, icon = icon_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0")