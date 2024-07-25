import tkinter as tk
import requests
import json
from datetime import datetime

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def showWeather():
    api_key = "afc6adb7ffbfa53c9c59c26918fb5480"  # Replace with your OpenWeatherMap API key
    city_name = city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    response = requests.get(weather_url)
    weather_info = response.json()

    tfield.delete("1.0", "end")

    if weather_info['cod'] == 200:
        kelvin = 273

        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather = f"\nWeather in {city_name}:\nTemperature (Celsius): {temp}°\nFeels like (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed:.2f} km/h\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloudiness: {cloudy}%\nDescription: {description}"
    else:
        weather = f"\nWeather for '{city_name}' not found!\nPlease enter a valid city name."

    tfield.insert("1.0", weather)

# Initialize Window
root = tk.Tk()
root.geometry("400x500")  # Adjusted window height for better UI
root.resizable(0, 0)
root.title("Weather App")

# Header Label
header_label = tk.Label(root, text="Weather App", font=("Arial", 18))
header_label.pack(pady=10)

# City Input
city_label = tk.Label(root, text='Enter City Name:', font=("Arial", 14))
city_label.pack(pady=5)

city_value = tk.StringVar()
city_entry = tk.Entry(root, textvariable=city_value, font=("Arial", 14), width=20)
city_entry.pack(pady=5)

# Check Weather Button
check_weather_button = tk.Button(root, text="Check Weather", font=("Arial", 14), bg='lightblue', fg='black',
                                 activebackground="teal", padx=10, pady=5, command=showWeather)
check_weather_button.pack(pady=10)

# Weather Output
weather_label = tk.Label(root, text="Weather Information:", font=("Arial", 14))
weather_label.pack(pady=5)

tfield = tk.Text(root, width=46, height=10, font=("Arial", 12))
tfield.pack()

root.mainloop()