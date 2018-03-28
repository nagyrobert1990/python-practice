import httplib2
import json

API_KEY = "26ac1863d12d4352a00241f9ba73361e"

def get_actual_weather_data(city, country_code):
    my_httplib2 = httplib2.Http(".cache")
    resp, content = my_httplib2.request("https://api.weatherbit.io/v2.0/current?city=" + city + "," + country_code + "&key=26ac1863d12d4352a00241f9ba73361e")
    utf8content = content.decode("utf-8")
    data = json.loads(utf8content)
    return data["data"]

def get_temperature_from_data(data):
    return data[0]["temp"]

def get_icon_from_data(data):
    return data[0]["weather"]["icon"]

def get_cities_from_file():
    city_list = []
    data = json.load(open('cities_hungary.json', encoding='utf8'))
    for city in data:
        city_list.append(city["city_name"])
    return city_list

if __name__ == "__main__":
    my_data = get_actual_weather_data("Miskolc", "HU")
    print(my_data)
    print(get_temperature_from_data(my_data))
    print(get_icon_from_data(my_data))