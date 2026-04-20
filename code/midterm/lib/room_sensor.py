#room_sensor.py

class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light
        
    def show_info(self):
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")
        
    def comfort_level(self):
        temp = self.temperature
        hum = self.humidity
        
        if (temp >= 20 and temp <=26) and (hum >=40 and hum <= 60):
            return "Comfortable"
        elif (temp >= 30) and (hum >= 70):
            return "Waring"
        else:
            return "Normal"
        
    def light_status(self):
        lig = self.light
        
        if lig < 200:
            return "Dark"
        else:
            return "Bright"
        