from flask import Flask
from flask import render_template
import RPi.GPIO as rpi 
import time

app= Flask(__name__)

led1= 25,23

rpi.setwarnings(False)
rpi.setmode(rpi.BCM)
rpi.setup(led1, rpi.OUT)
rpi.output(led1, 0)
print("Finished")

@app.route('/')
def index():
	return render_template('Temp_control.html')

@app.route('/A')
def led1on():
	rpi.output(led1,1)
	return render_template('Temp_control.html')
@app.route('/a')
def led1off():
	rpi.output(led1,0)
	return render_template('Temp_control.html')

if __name__=="__main__":
	print("start")
	app.run(debug=True, host='192.168.1.228')
