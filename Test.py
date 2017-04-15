from G6reader import *

c = 'r'
while c == 'r' :
	c = raw_input('Read(r) or End(e): ')
	if c=='e':
		print'End!!'
		break
	else:
		print'Read!!'
		print Read_RFID.get_uid


