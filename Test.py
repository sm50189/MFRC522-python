from G6reader import *
import RPi.GPIO as GPIO

def main():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(20, GPIO.OUT)
	GPIO.setup(21, GPIO.OUT)
	GPIO.setup(19, GPIO.OUT)
	GPIO.setup(26, GPIO.OUT)
	
	GPIO.output(16, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(21, GPIO.LOW)
	GPIO.output(19, GPIO.LOW)
	GPIO.output(26, GPIO.LOW)

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
			for i in [16,20]:
				GPIO.output(i, GPIO.HIGH)
				print RR.get_uid(i)
				GPIO.output(16, GPIO.LOW)
				GPIO.output(20, GPIO.LOW)
				#GPIO.output(21, GPIO.LOW)
				#GPIO.output(19, GPIO.LOW)
				#GPIO.output(26, GPIO.LOW)
		

main()


