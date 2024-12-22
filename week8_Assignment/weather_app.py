import requests

def get_weather(city_name, api_key):
    # Define the URL for the weather API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract the weather information
        main = data['main']
        weather = data['weather'][0]
        
        # Display the weather information
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print("City not found or API request failed!")

def main():
    # Get the city name from the user
    city_name = input("Enter the city name: ")
    
    # Use your OpenWeatherMap API key here
    api_key = "your_api_key_here"
    
    # Call the function to get the weather data
    get_weather(city_name, api_key)

if __name__ == "__main__":
    main()
