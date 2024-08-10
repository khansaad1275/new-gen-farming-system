import random
import requests
from datetime import datetime, timedelta, timezone

# Constants for sensor value ranges
MOISTURE_DISCONNECTED = 1000
MOISTURE_DRY_MIN = 600
MOISTURE_DRY_MAX = 999
MOISTURE_HUMID_MIN = 370
MOISTURE_HUMID_MAX = 599
MOISTURE_WATER = 369

# API Setup
API_KEY = '983860240e83fc557cfbb368da63aa60'  # Your API key
LOCATION = 'Surat'  # Farm location

# Generate random moisture value
def generate_moisture_value():
    return random.randint(200, 700)

# Check moisture suitability
def check_moisture(moisture_value):
    suitability = {'wheat': False, 'rice': False}

    if MOISTURE_HUMID_MIN <= moisture_value <= MOISTURE_HUMID_MAX:
        suitability['wheat'] = True  # Wheat likes moderate moisture
    if moisture_value <= MOISTURE_WATER:
        suitability['rice'] = True  # Rice needs wet conditions

    return suitability

# Fetch weather data
def fetch_weather_forecast():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    forecast_data = response.json()
    return forecast_data

# Analyze weather and irrigation
def analyze_weather_and_irrigation(moisture_value, forecast_data):
    rain_expected = False
    weather_description = forecast_data['weather'][0]['main'].lower()

    if 'rain' in weather_description:
        rain_expected = True
        rain_time = datetime.fromtimestamp(forecast_data['dt'], timezone.utc)  # Updated for timezone-aware UTC
        print(f"Rain soon: {rain_time.strftime('%Y-%m-%d %H:%M:%S')}. No need to water.")
    
    if not rain_expected:
        optimal_watering_time = datetime.now() + timedelta(days=1)
        print(f"Water tomorrow: {optimal_watering_time.strftime('%Y-%m-%d %H:%M:%S')}.")

# Main function
def main():
    moisture_value = generate_moisture_value()
    print(f"Moisture Value: {moisture_value}")

    suitability = check_moisture(moisture_value)
    print(f"Wheat OK? {'Yes' if suitability['wheat'] else 'No'}")
    print(f"Rice OK? {'Yes' if suitability['rice'] else 'No'}")

    forecast_data = fetch_weather_forecast()

    if not suitability['wheat']:
        print("Wheat needs water soon.")
        analyze_weather_and_irrigation(moisture_value, forecast_data)
    
    if not suitability['rice']:
        print("Rice needs water soon.")
        analyze_weather_and_irrigation(moisture_value, forecast_data)

if __name__ == "__main__":
    main()