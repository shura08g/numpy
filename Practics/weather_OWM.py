import pyowm

city = input("What city?:")

owm = pyowm.OWM('908cc54421daceca47117407ada157af')

# observation = owm.weather_at_place('London,uk')
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print(w)

print("In " + city + " now temperature: " + str(temperatureKiev))

w.get_wind()
w.get_humidity()
w.get_temperature('celsius')
