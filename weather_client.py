import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "7239a449998f8efc32db810bd0f590c2"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
def get_cat_fact() -> Dict:
    response = requests.get("https://catfact.ninja/fact")
    return response.json()

def main():
    temp = get_weather("London")
    print(temp)
    print("\n")
    print(get_cat_fact())

if __name__ == "__main__":
    main()
