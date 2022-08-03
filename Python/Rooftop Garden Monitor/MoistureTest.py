import time
from board import SCL, SDA
import busio
from ISStreamer.Streamer import Streamer
from adafruit_seesaw.seesaw import Seesaw

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Garden"
BUCKET_NAME = ":partly_sunny: Room Temperature"
BUCKET_KEY = "temp1"
ACCESS_KEY = "ist_PFR-1Wmt2MR4uRnUGgUnWlmZ113RMDeA"
# ---------------------------------


i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()
    # read temperature from the temperature sensor
    temp_c = ss.get_temp()
    print("temp: " + str(temp_c) + " moisture: " + str(touch))
    streamer.log(SENSOR_LOCATION_NAME + "Temperature(C)", temp_c)
    streamer.log(SENSOR_LOCATION_NAME + "Moisture", touch)
    time.sleep(1)