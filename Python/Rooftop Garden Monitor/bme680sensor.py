import time 
import board
import busio
import adafruit_bme680
from ISStreamer.Streamer import Streamer

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
 
# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Garden"
BUCKET_NAME = ":partly_sunny: Room Temperature"
BUCKET_KEY = "temp1"
ACCESS_KEY = "ist_PFR-1Wmt2MR4uRnUGgUnWlmZ113RMDeA"
# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1012
MINUTES_BETWEEN_READS = 1
METRIC_UNITS = False
# ---------------------------------

# OR create library object using our Bus SPI port
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#bme_cs = digitalio.DigitalInOut(board.D10)
#bme680 = adafruit_bme680.Adafruit_BME680_SPI(spi, bme_cs)

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
while True:
        humidity = format(bme680.humidity, ".1f")
        pressure = format(bme680.pressure, ".1f")
        temp_c = bme680.temperature
        print(f"Temp - {temp_c}")
        if METRIC_UNITS:
                streamer.log(SENSOR_LOCATION_NAME + "Temperature(C)", temp_c)
        else:
                temp_f = format(temp_c * 9.0 / 5.0 + 32.0, ".1f")
                streamer.log(SENSOR_LOCATION_NAME + " Temperature(F)", temp_f)
        streamer.log(SENSOR_LOCATION_NAME + "Humidity(%)", humidity)
        streamer.log(SENSOR_LOCATION_NAME + "Pressure(hPA)", pressure)
        streamer.flush()
        time.sleep(60*MINUTES_BETWEEN_READS)