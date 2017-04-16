from G6reader import *
import RPi.GPIO as GPIO


RR = Read_RFID()
c = 'r'
while c == 'r' :
	c = raw_input('Read(r) or End(e): ')
	if c=='e':
		print'End!!'
		break
	else:
		#print'Read!!'
		print RR.get_uid()



