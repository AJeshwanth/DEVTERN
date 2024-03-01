import streamlit as st
import requests
import api
def fetch_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    st.title("Weather App")

    city_name = st.text_input("Enter the name of the city:", "New York")
    api_key = api.apikey

    if st.button("Get Weather"):
        weather_data = fetch_weather(city_name, api_key)
        if weather_data["cod"] == 200:
            st.success("Weather data fetched successfully!")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Description: {weather_data['weather'][0]['description'].capitalize()}")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            st.error(f"Error: {weather_data['message']}")

if __name__ == "__main__":
    main()
