#main.py

from room_sensor import RoomSensor

kitchen = RoomSensor("Kitchen", 31, 72, 180)
bedroom = RoomSensor("Bedroom", 26, 60, 100)
balcony = RoomSensor("Balcony", 35, 80, 220)

sensors = [kitchen, bedroom, balcony]
com = 0
nor = 0
war = 0

for sensor in sensors:
    if (sensor.comfort_level() == "Comfortable"):
        com += 1
    elif (sensor.comfort_level() == "Normal"):
        nor += 1
    if (sensor.comfort_level() == "Waring"):
        war += 1
        
    sensor.show_info()
    print(f"Comfort Level: {sensor.comfort_level()}")
    print(f"Light Status: {sensor.light_status()}")
    print("--------------------------")
    print()
    
print(f"Comfortable: {com}")
print(f"Normal: {nor}")
print(f"Waring: {war}")


