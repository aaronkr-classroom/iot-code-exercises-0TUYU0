#main.py

from room_sensor import RoomSensor

kitchen = RoomSensor("Kitchen", 31, 72, 180)
bedroom = RoomSensor("Bedroom", 26, 60, 100)
balcony = RoomSensor("Balcony", 35, 80, 220)

sensors = [kitchen, bedroom, balcony]

for sensor in sensors:
    sensor.show_info()
    print(f"Comfort Level: {sensor.comfort_level()}")
    print(f"Light Status: {sensor.light_status()}")
    print("--------------------------")
    print()
