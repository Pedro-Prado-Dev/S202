import threading
import time
import random
from pymongo import MongoClient
from datetime import datetime, timedelta
import json
import os

def update_alarm_status(sensor_name, alarm_status):
    client = MongoClient('localhost', 27017)
    db = client['bancoiot']
    collection = db['sensores']
    
    query = {'nomeSensor': sensor_name}
    new_values = {'$set': {'sensorAlarmado': alarm_status}}
    collection.update_one(query, new_values)

def generate_temperature(sensor_name):
    while True:
        temperature = random.uniform(30, 40)  
        print(f"{sensor_name}: {temperature} C°")
        
        update_database(sensor_name, temperature)
        
        if temperature > 38:
            print(f"Atenção! Temperatura muito alta! Verificar Sensor {sensor_name}!")
            update_alarm_status(sensor_name, True)
            break
        
        time.sleep(2) 

def update_database(sensor_name, temperature):
    client = MongoClient('localhost', 27017)
    db = client['bancoiot']
    collection = db['sensores']
    
    query = {'nomeSensor': sensor_name}
    new_values = {
        '$set': {
            'valorSensor': temperature,
            'timestamp': datetime.now() 
        }
    }
    collection.update_one(query, new_values, upsert=True)

def get_sensor_data_last_hour(sensor_name):
    client = MongoClient('localhost', 27017)
    db = client['bancoiot']
    collection = db['sensores']
    
    one_hour_ago = datetime.now() - timedelta(hours=1)
    
    query = {
        'nomeSensor': sensor_name,
        'timestamp': {'$gte': one_hour_ago}
    }
    result = collection.find(query)

    data = [(data['timestamp'].strftime('%Y-%m-%d %H:%M:%S'), data['valorSensor']) for data in result]
    
    folder_name = 'JSON'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    filename = os.path.join(folder_name, f"{sensor_name}_data_last_hour.json")
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
    
    return data

threads = []
sensor_names = ['Sensor1', 'Sensor2', 'Sensor3']

for sensor_name in sensor_names:
    thread = threading.Thread(target=generate_temperature, args=(sensor_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for sensor_name in sensor_names:
    sensor_data = get_sensor_data_last_hour(sensor_name)
    print(f"Dados do Sensor {sensor_name} nas últimas horas:")
    for timestamp, temperature in sensor_data:
        print(f"{timestamp}: {temperature} C°")
