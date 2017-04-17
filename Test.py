from G6reader import *
import RPi.GPIO as GPIO
import time

RR = Read_RFID()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.output(40, GPIO.HIGH)
GPIO.output(38, GPIO.LOW)
c = 'r'

class chip_select():
	def __init__(self,port_num):
		self._port_num = port_num
	
	def __enter__(self):
		print'Go LOW'
		GPIO.output(self._port_num,GPIO.LOW)
		time.sleep(1)
	
	def __exit__(self,type,value,traceback):
		print'Go HIGH'
		GPIO.output(self._port_num,GPIO.HIGH)
		time.sleep(1)
		print "exit"
try:
	while c == 'r' :
		c = raw_input('Read(r) or End(e): ')
		if c =='e':
			RR.end_read()
			print'End!!'
			break
		elif c == 'r':
			#print'Read!!'
			with chip_select(38) as cs:
				print RR.get_uid()
			with chip_select(40) as cs:
				print RR.get_uid()
			#GPIO.output(24, GPIO.LOW)
			#print RR.get_uid()
			#GPIO.output(24, GPIO.HIGH)
			#GPIO.output(40, GPIO.LOW)
		else:
			c = 'r'
			continue
except KeyboardInterrupt:
	RR.end_read()
	#GPIO.cleanup()
	print'Clean and End'
#finally:
	#RR.end_read()
	#GPIO.cleanup()
	#print'Clean and End'



