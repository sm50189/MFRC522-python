import RPi.GPIO as GPIO
try:
	state = 'l'
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(36, GPIO.OUT)
	GPIO.output(36, GPIO.LOW)
	while state == 'l' or state == 'h':
		state = raw_input("State? LOW = 'l' HI = 'h':")
		if state == 'l':
			print'Go LOW'
			GPIO.output(36, GPIO.LOW)
		elif state == 'h':
			print'Go HIGH'
			GPIO.output(36, GPIO.HIGH)
		else:
			print'Break'
			break
except KeyboardInterrupt:
	GPIO.cleanup()
	print'Clean and End'
finally:
	GPIO.cleanup()
	print'Clean and End'