#4_p.7_6

sensors = {
    'dht11': {
        'temperature': 23,
        'temp_unit': "Celsius",
        'humidity': 47
        },
    'bh1750': {
        'illuminance' : 450,
        'illumi_unit': "Lux"
        }
    }
    
print(sensors['dht11'])
print(sensors['bh1750'])