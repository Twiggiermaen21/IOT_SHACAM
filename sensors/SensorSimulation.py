import random
import time
import json
import paho.mqtt.client as mqtt

# MQTT Server Parameters
MQTT_CLIENT_ID = "simulated_python_sensor"
MQTT_BROKER = "172.31.128.1"
MQTT_PORT = 1883

# Helper function to generate sensor names by removing everything after '_ID'
def get_sensor_name(sensor_key):
    # Find the position of '_ID' and return only the part before it
    if '_ID' in sensor_key:
        return sensor_key.split('_ID')[0]  # Split the string at '_ID' and return the first part
    return sensor_key  # In case '_ID' is not found, return the original name

# Function to generate a set of simulated sensor data for the kitchen
def generate_sensor_data_kitchen():
    sensor_data_kitchen = {
        "occupancy_sensor_ID1": random.choice([0, 1]),
        "humidity_sensor_ID2": round(random.uniform(30.0, 70.0), 2),
        "temperature_sensor_ID3": round(random.uniform(10.0, 30.0), 2),
        "air_quality_sensor_ID4": random.randint(0, 100),
        "smoke_detector_ID5": random.choice([0, 1]),
        "carbon_monoxide_sensor_ID8": round(random.uniform(0.0, 2.0), 2)
    }
    return sensor_data_kitchen

# Function to generate a set of simulated sensor data for the living room
def generate_sensor_data_livingroom():
    sensor_data_livingroom = {
        "occupancy_sensor_ID9": random.choice([0, 1]),
        "humidity_sensor_ID10": round(random.uniform(30.0, 70.0), 2),
        "temperature_sensor_ID11": round(random.uniform(10.0, 30.0), 2),
        "air_quality_sensor_ID12": random.randint(0, 100),
        "smoke_detector_ID13": random.choice([0, 1]),

    }
    return sensor_data_livingroom

# Function to generate a set of simulated sensor data for the bedroom
def generate_sensor_data_bedroom():
    sensor_data_bedroom = {
        "occupancy_sensor_ID17": random.choice([0, 1]),
        "humidity_sensor_ID18": round(random.uniform(30.0, 70.0), 2),
        "temperature_sensor_ID19": round(random.uniform(10.0, 30.0), 2),
        "air_quality_sensor_ID20": random.randint(0, 100),
        "smoke_detector_ID21": random.choice([0, 1]),
    }
    return sensor_data_bedroom

# Function to generate a set of simulated sensor data for the bathroom
def generate_sensor_data_bathroom():
    sensor_data_bathroom = {
        "occupancy_sensor_ID23": random.choice([0, 1]),
        "humidity_sensor_ID24": round(random.uniform(30.0, 70.0), 2),
        "temperature_sensor_ID25": round(random.uniform(10.0, 30.0), 2),
        "air_quality_sensor_ID26": random.randint(0, 100),
        "smoke_detector_ID27": random.choice([0, 1]),
    }
    return sensor_data_bathroom

# Function to generate a set of simulated sensor data for the outside area
def generate_sensor_data_outside():
    sensor_data_outside = {
        "light_sensor_ID39": random.randint(0, 1000),
        "humidity_sensor_ID40": round(random.uniform(30.0, 70.0), 2),
        "temperature_sensor_ID41": round(random.uniform(-15.0, 30.0), 2),
        "air_quality_sensor_ID42": random.randint(0, 500),
        "motion_sensor_ID43": random.choice([0, 1]),
    }
    return sensor_data_outside

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Create an MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect

# Connect to the broker
try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"ALERT! Could not connect to MQTT Broker: {e}")

# Start the MQTT client loop in the background
client.loop_start()

# Publish each sensor data separately
while True:
    # Kitchen sensors
    sensor_data_kitchen = generate_sensor_data_kitchen()
    for sensor_key, value in sensor_data_kitchen.items():
        sensor_name = get_sensor_name(sensor_key)  # Removing everything after '_ID'
        client.publish(f"/smart_home/kitchen/{sensor_name}/{sensor_key}", json.dumps({sensor_key: value}, indent=4))
        time.sleep(1)

    # Living room sensors
    sensor_data_livingroom = generate_sensor_data_livingroom()
    for sensor_key, value in sensor_data_livingroom.items():
        sensor_name = get_sensor_name(sensor_key)  # Removing everything after '_ID'
        client.publish(f"/smart_home/livingroom/{sensor_name}/{sensor_key}", json.dumps({sensor_key: value}, indent=4))
        time.sleep(1)

    # Bedroom sensors
    sensor_data_bedroom = generate_sensor_data_bedroom()
    for sensor_key, value in sensor_data_bedroom.items():
        sensor_name = get_sensor_name(sensor_key)  # Removing everything after '_ID'
        client.publish(f"/smart_home/bedroom/{sensor_name}/{sensor_key}", json.dumps({sensor_key: value}, indent=4))
        time.sleep(1)

    # Bathroom sensors
    sensor_data_bathroom = generate_sensor_data_bathroom()
    for sensor_key, value in sensor_data_bathroom.items():
        sensor_name = get_sensor_name(sensor_key)  # Removing everything after '_ID'
        client.publish(f"/smart_home/bathroom/{sensor_name}/{sensor_key}", json.dumps({sensor_key: value}, indent=4))
        time.sleep(1)

    # Outside sensors
    sensor_data_outside = generate_sensor_data_outside()
    for sensor_key, value in sensor_data_outside.items():
        sensor_name = get_sensor_name(sensor_key)  # Removing everything after '_ID'
        client.publish(f"/smart_home/outside/{sensor_name}/{sensor_key}", json.dumps({sensor_key: value}, indent=4))
        time.sleep(1)
