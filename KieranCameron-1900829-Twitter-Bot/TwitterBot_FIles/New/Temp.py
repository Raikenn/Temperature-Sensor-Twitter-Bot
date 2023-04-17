import RGB1602
import math
import Adafruit_DHT
import time
import requests
colourR = 64
colourG = 128
colourB = 64

lcd=RGB1602.RGB1602(16,2)
lcd.setCursor(0, 0)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 23

while True:
		humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
		if humidity is not None and temperature is not None:
			report = {}
			report["value1"] = temperature
			report["value2"] = humidity
			#removed the private key due this making this a public repository
			requests.post("https://maker.ifttt.com/trigger/Tweet_MyTemp/with/key/INSERT PRIVATE KEY HERE", data=report)
			#lcd.printout("temp={0:0.1f}C \n Humidity={1:0.1f}% ".format(temperature, humidity))
			lcd.setCursor(0, 0)
			lcd.printout("temp={0:0.1f}C".format(temperature))
			lcd.setCursor(0, 1)
			lcd.printout("Humidity={1:0.1f}%".format(humidity))
			time.sleep(10);
			lcd.clear();	
		else:
			lcd.printout("Gathering Data");
			

			time.sleep(30);		
			lcd.clear();











