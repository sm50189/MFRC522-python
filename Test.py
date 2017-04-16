from G6reader import *
import RPi.GPIO as GPIO

def main():
	#GPIO.setmode(GPIO.BOARD)
	#GPIO.setup(36, GPIO.OUT)
	#GPIO.setup(38, GPIO.OUT)
	#GPIO.setup(40, GPIO.OUT)
	#GPIO.setup(35, GPIO.OUT)
	#GPIO.setup(37, GPIO.OUT)
	
	#GPIO.output(36, GPIO.LOW)
	#GPIO.output(38, GPIO.LOW)
	#GPIO.output(40, GPIO.LOW)
	#GPIO.output(35, GPIO.LOW)
	#GPIO.output(37, GPIO.LOW)

	RR = Read_RFID()
	c = 'r'
	while c == 'r' :
		c = raw_input('Read(r) or End(e): ')
		if c=='e':
			RR.end_read()
			print'End!!'
			break
		else:
			#print'Read!!'
			#for i in [16,20,21,19,26]:
			for i in [36,38]:
				GPIO.output(i, GPIO.HIGH)
				print RR.get_uid()
				GPIO.output(36, GPIO.LOW)
				GPIO.output(38, GPIO.LOW)
				#GPIO.output(21, GPIO.LOW)
				#GPIO.output(19, GPIO.LOW)
				#GPIO.output(26, GPIO.LOW)
		

main()


