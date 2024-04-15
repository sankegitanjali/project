import requests


APP_KEY = '44af14e920c5e9bf9d69cbd777bee0b3'
city_name = input("Enter the name of the city: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={APP_KEY}'

response = requests.get(url)
print(response)

#<Response [200]> successfully
#<Response [404]> error



if response.status_code == 200:
    weather_data = response.json()
    #print(weather_data)
    weather_disc = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']  - 273.15
    print(temp)

#Display weather info
    print(f'Weather in {city_name}: {round(temp, 2)} °C with {weather_disc}')
else: 
    print(f'City name {city_name} is not found or incorrect')
