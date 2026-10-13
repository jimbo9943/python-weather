from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Leicester City"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(f"\nRequest URL: {request_url}\n")

    weather_data = requests.get(request_url).json()

    return weather_data
    
if __name__ ==  "__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease input a city name: ")

    # check for empty strings or string with only spaces
    # This step is not required here
    if not bool(city.strip()):                      # Not working here!!!!
        city = "Leicester City"
        
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)