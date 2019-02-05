
# imports flask website framework
from flask import Flask, render_template

# imports the modules for the sensor
from bmp280 import BMP280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# Date and time    
import datetime

# CPU temperature
from gpiozero import CPUTemperature

# variables set up - Flask
app = Flask(__name__)

# variables set up - Sensor
bus=SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

def cpu_temperature():
    cpu = CPUTemperature()
    cpu_temp = cpu.temperature
    cpu_temp = str(cpu_temp)
    return(cpu_temp)

def get_temp():
    temperature = bmp280.get_temperature()
    temperature = round(temperature)
    temperature = temperature -2
    temperature = str(temperature)
    return(temperature)

def get_pressure():
    pressure = bmp280.get_pressure()
    pressure = round(pressure)
    pressure = str(pressure)
    return(pressure)

def time_now():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now=str(now)
    return(now)

@app.route('/')
def get():
    temp = get_temp()
    pressure = get_pressure()
    now = time_now()
    cpu_temp = cpu_temperature()
    return render_template('flask_temp.html',temp=temp,pressure=pressure,cpu_temp=cpu_temp,now=now)