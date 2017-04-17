from G6reader import *
import RPi.GPIO as GPIO

RR = Read_RFID()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)

#try:
print RR.get_uid()
GPIO.cleanup()
#except KeyboardInterrupt:
#	RR.end_read()
	#GPIO.cleanup()
#	print'Clean and End'


