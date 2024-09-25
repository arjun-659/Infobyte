import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For weather icons
import io
import urllib.request

# Fetch weather data from OpenWeatherMap API
def fetch_weather_data(location, unit, api_key):
    unit_param = "metric" if unit == "Celsius" else "imperial"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={unit_param}"
    response = requests.get(url)
    return response.json()

# Display weather info in the GUI
def display_weather_info(data, unit):
    if data["cod"] != 200:
        messagebox.showerror("Error", f"Error: {data['message']}")
        return

    city = f"{data['name']}, {data['sys']['country']}"
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description'].title()

    # Display weather info
    result_var.set(f"Location: {city}\nTemperature: {temp}°{unit[0]}\nHumidity: {humidity}%\nCondition: {description}")

    # Fetch and display weather icon
    icon_code = data['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    icon_data = urllib.request.urlopen(icon_url).read()
    icon_image = Image.open(io.BytesIO(icon_data))
    icon_photo = ImageTk.PhotoImage(icon_image)
    icon_label.config(image=icon_photo)
    icon_label.image = icon_photo  # Keep reference to avoid garbage collection

# Handle the search button click
def search_weather():
    location = location_var.get()
    unit = unit_var.get()
    if not location:
        messagebox.showerror("Input Error", "Please enter a location.")
        return

    api_key = "9761be57143a399184e0fc5992c60a2d"  # Replace with your API key

    # Fetch and display weather data
    weather_data = fetch_weather_data(location, unit, api_key)
    display_weather_info(weather_data, unit)

# Set up the GUI window
root = tk.Tk()
root.title("Advanced Weather App")
root.geometry("400x400")

# Variables for user inputs
location_var = tk.StringVar()
unit_var = tk.StringVar(value="Celsius")
result_var = tk.StringVar()

# GUI Layout
tk.Label(root, text="Enter City or ZIP Code:").pack(pady=5)
tk.Entry(root, textvariable=location_var).pack(pady=5)

tk.Label(root, text="Select Unit:").pack(pady=5)
tk.Radiobutton(root, text="Celsius", variable=unit_var, value="Celsius").pack()
tk.Radiobutton(root, text="Fahrenheit", variable=unit_var, value="Fahrenheit").pack()

tk.Button(root, text="Get Weather", command=search_weather).pack(pady=10)

tk.Label(root, text="Weather Info:").pack(pady=5)
tk.Label(root, textvariable=result_var, justify="left").pack(pady=5)

# Icon label for displaying weather icon
icon_label = tk.Label(root)
icon_label.pack()

root.mainloop()