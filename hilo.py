from G6reader import *
import RPi.GPIO as GPIO
import time

try:
	RR = Read_RFID()
	state = '1'
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(38, GPIO.OUT)
	GPIO.setup(40, GPIO.OUT)
	GPIO.output(38, GPIO.HIGH)
	GPIO.output(40, GPIO.HIGH)
	while state == '1' or state == '2':
		state = raw_input("Reader? 1 = '1' 2 = '2':")
		if state == '1':
			print'1 Go LOW'
			GPIO.output(38, GPIO.LOW)
			time.sleep(1)
			print RR.get_uid()
			GPIO.output(38, GPIO.HIGH)
		elif state == '2':
			print'2 Go LOW'
			GPIO.output(40, GPIO.LOW)
			time.sleep(1)
			print RR.get_uid()
			GPIO.output(40, GPIO.HIGH)
		else:
			print'Break'
			break
except KeyboardInterrupt:
	GPIO.cleanup()
	print'Clean and End'
finally:
	GPIO.cleanup()
	print'Clean and End'