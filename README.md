# 🌾 Plant Disease Detection & Irrigation Management System 🌱

This project is designed to help farmers by using AI-based plant disease detection and smart irrigation management, leveraging weather forecasts and soil moisture data.

## 🚀 Features

1. **Plant Disease Detection**:
   - Utilizes the `MobileNetV2` model fine-tuned for plant disease identification.
   - Identifies common diseases in wheat and rice with high accuracy.

2. **Smart Irrigation Management**:
   - Randomly generates soil moisture values to simulate sensor data.
   - Checks moisture levels to determine if crops (wheat/rice) need water.
   - Fetches real-time weather forecasts using OpenWeatherMap API.
   - Advises on the best time for irrigation based on moisture and weather data.

## 🛠️ Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/plant-disease-irrigation.git
   cd plant-disease-irrigation
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your API Key**:
   - Replace the placeholder API key in the script with your OpenWeatherMap API key.

4. **Run the Program**:
   ```bash
   python main.py
   ```

## 📊 How It Works

1. **Disease Detection**:
   - The script loads images from the `images/` directory.
   - It classifies each image, predicting the disease and confidence level.

2. **Irrigation Management**:
   - The system generates a random soil moisture value.
   - It evaluates whether the soil moisture is adequate for wheat or rice.
   - Based on the weather forecast, it advises on the optimal time to irrigate.

## 📋 Example Output

```
Moisture Value: 520
Wheat OK? Yes
Rice OK? No
Rice needs water soon.
Water tomorrow: 2024-08-11 08:00:00.
```

## 🌍 Future Enhancements

- **Integrate Real-Time Sensor Data**: Replace the random generator with actual sensor inputs.
- **Expand Crop Variety**: Include more crops and associated diseases.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
