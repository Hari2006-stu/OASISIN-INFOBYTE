import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = "70be5b4595236b3992b2721e61668f41"
    
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            city_name = data['name']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            condition = data['weather'][0]['description'].title()

            result_label.config(
                text=f"City: {city_name}\nTemperature: {temp}°C\nHumidity: {humidity}%\nCondition: {condition}"
            )
        else:
            messagebox.showerror("Error", f"City not found!\n({data.get('message', 'Unknown error')})")
    
    except Exception as e:
        messagebox.showerror("Network Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("320x250")
root.config(bg="#e3f2fd")

title_label = tk.Label(root, text="🌤️ Weather App", font=("Arial", 16, "bold"), bg="#e3f2fd")
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter City Name (e.g., Chennai or Chennai,IN):", font=("Arial", 10), bg="#e3f2fd")
city_label.pack()

city_entry = tk.Entry(root, width=25, font=("Arial", 12))
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=get_weather)
get_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e3f2fd", justify="left")
result_label.pack(pady=10)

root.mainloop()