format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output

print(f"{format_output}---START---{format_reset}")

# dictionary of cities with their weather predictions

forecast = {"London": {"Temperature": 5, "Unit1": "Deg", "Weather Conditions": "Windy", "Wind Speed": 30, "Unit2": "m/h", "Humidity": "15%" },
            "Leeds": {"Temperature": 10, "Unit1": "Deg", "Weather Conditions": "Rainy", "Wind Speed": 7, "Unit2": "m/h", "Humidity": "20"},
            "Manchester": {"Temperature": 2, "Unit1": "Deg", "Weather Conditions": "Snowing", "Wind Speed": 20, "Unit2": "m/h", "Humidity": "30%"},
            "Brighton": {"Temperature": 15, "Unit1": "Deg", "Weather Conditions": "Sunny", "Wind Speed": 17, "Unit2": "m/h", "Humidity": "10%"},
            "Las Palmas": {"Temperature": 25, "Unit1": "Deg", "Weather Conditions": "Very Sunny", "Wind Speed": 3, "Unit2": "m/h", "Humidity": "30%"}
}

#emojis to use in my app
sun_emoji = "\U0001F31E"
freezing_emoji = "🥶"

print("Welcome to the Most Accurate Weather App there is. Type in the city to find out our recommendations")
user_input = (input("Choose a city:   ")).strip()
#strip(removes all extra spaces user adds to avoid errors)

# function to display weather conditions based on a city that user inputs
#  using if statement makes sure it only shows 1 option, if I use for loop it would iterate through the whole dictionary
# function checks if a city is the dictionary, then checks for temperature and if it's > 20 deg is gives one recommendation, it it's lower- another recommendation

def weather(city):
    if city in forecast:
        temperature = forecast[city]["Temperature"]
        unit1 = forecast[city]["Unit1"]
        weather_conditions = forecast[city]["Weather Conditions"]
        wind_speed = forecast[city]["Wind Speed"]
        unit2 = forecast[city]["Unit2"]
        humidity = forecast[city]["Humidity"]
        if temperature > 20:
            print(f"The current temperature in {city} is {temperature}{unit1}. It is {weather_conditions}. Wind speed is {wind_speed}{unit2}. Humidity is {humidity}. Planning holidays? This is the best place to go! {sun_emoji}")
        else:
            print(f"The current temperature in {city} is {temperature}{unit1}. It is {weather_conditions}. Wind speed is {wind_speed}{unit2}. Humidity is {humidity}. We recommend you pack your hats and gloves for your trip!!!! {freezing_emoji}")
    else:
        print(f"Sorry. We don't have {city} in our databse yet")

weather(user_input)
print("Thank you for using our Weather App! Have a great day!")