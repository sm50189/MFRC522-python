from G6reader import *
import RPi.GPIO as GPIO


RR = Read_RFID()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(40, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
c = 'r'

class chip_select():
	def __init__(self,port_num):
		self._port_num = port_num
	
	def __enter__(self):
		GPIO.output(self._port_num,GPIO.LOW)
	
	def __exit__(self,type,value,traceback):
		GPIO.output(self._port_num,GPIO.HIGH)
while c == 'r' :
	c = raw_input('Read(r) or End(e): ')
	if c =='e':
		RR.end_read()
		print'End!!'
		break
	elif c == 'r':
		#print'Read!!'
		with chip_select(24) as cs:
			print RR.get_uid()
		#GPIO.output(24, GPIO.LOW)
		#print RR.get_uid()
		#GPIO.output(24, GPIO.HIGH)
		#GPIO.output(40, GPIO.LOW)
		with chip_select(40) as cs:
			print RR.get_uid()
	else:
		c = 'r'
		continue



