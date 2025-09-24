import requests


API_KEY = "443fbe3e73bc3a649a19edc65c16c9fd"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273
    print(f"Weather: {weather}")
    print(f"Temperature: {round(temperature)} celsius")
else:
    print("An error occurred.")
