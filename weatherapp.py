import tkinter as tk
from tkinter import messagebox
import requests
import time

def getWeather(event=None):
    city = textfield.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    try:
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=0b7750b56a52f51168cb044133a8e185"
        json_data = requests.get(api).json()

        if json_data.get("cod") != 200:
            messagebox.showerror("Error", json_data.get("message", "City not found!"))
            return

        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = f"{condition}\n{temp}°C"
        final_data = (
            f"Max Temp: {max_temp}°C\n"
            f"Min Temp: {min_temp}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}"
        )

        label1.config(text=final_info)
        label2.config(text=final_data)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Initialize Tkinter Window
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.configure(bg="#87CEEB")  # Light blue background

# Fonts and Styles
font_title = ("Helvetica", 24, "bold")
font_input = ("Helvetica", 18)
font_data = ("Helvetica", 14)

# Title Label
title_label = tk.Label(canvas, text="Weather App", font=font_title, bg="#87CEEB", fg="#1F1F1F")
title_label.pack(pady=10)

# Text Input
textfield = tk.Entry(canvas, justify='center', font=font_input, width=20, relief="ridge", bd=4)
textfield.pack(pady=15)
textfield.focus()
textfield.bind('<Return>', getWeather)

# Weather Information Labels
label1 = tk.Label(canvas, font=font_title, bg="#87CEEB", fg="#000080")  # Main condition
label1.pack(pady=10)
label2 = tk.Label(canvas, font=font_data, bg="#87CEEB", fg="#2F4F4F", justify="left")  # Additional details
label2.pack(pady=10)

# Button
search_button = tk.Button(canvas, text="Get Weather", command=getWeather, font=("Helvetica", 14), bg="#4682B4", fg="white", relief="raised")
search_button.pack(pady=15)

# Footer
footer_label = tk.Label(canvas, text="Powered by OpenWeatherMap", font=("Helvetica", 10), bg="#87CEEB", fg="#696969")
footer_label.pack(side="bottom", pady=10)

canvas.mainloop()
