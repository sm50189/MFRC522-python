from G6reader import *
import RPi.GPIO as GPIO
import time

RR = Read_RFID()
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(18, GPIO.OUT)
#GPIO.output(18, GPIO.LOW)
c = 'r'

class Busout(object):
	def __init__(self,*args):
		self._bus = args
		for i in self._bus:
			GPIO.setup(i,GPIO.OUT)
	
	def write(self,value):
		mask = 1
		for i in self._bus:
			GPIO.output(i,value&mask)
			mask = mask*2
		
bus = Busout(18,16)		
class chip_select():
	def __init__(self,bus,value):
		self._bus = bus
		self._value = value
	
	def __enter__(self):
		print'Enter read card number',self._value
		self._bus.write(self._value)
		time.sleep(0.1)
	
	def __exit__(self,type,value,traceback):
		print'Finish read card number',self._value
		time.sleep(1)
try:
	while c == 'r' :
		c = raw_input('Read(r) or End(e): ')
		if c =='e':
			RR.end_read()
			print'End!!'
			break
		elif c == 'r':
			#print'Read!!'
			#GPIO.output(24, GPIO.LOW)
			#print RR.get_uid()
			#GPIO.output(24, GPIO.HIGH)
			#GPIO.output(40, GPIO.LOW)
			with chip_select(bus,1) as cs:
				print RR.get_uid()
			with chip_select(bus,2) as cs:
				print RR.get_uid()
			with chip_select(bus,3) as cs:
				print RR.get_uid()
			with chip_select(bus,4) as cs:
				print RR.get_uid()
				
		else:
			c = 'r'
			continue
except KeyboardInterrupt:
	RR.end_read()
	#GPIO.cleanup()
	print'Clean and End'
finally:
	pass
	#RR.end_read()
	#GPIO.cleanup()
	#print'Clean and End'



