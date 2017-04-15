from G6reader import Read_RFID as RR

c = 'r'
while c == 'r' :
	c = raw_input('Read(r) or End(e): ')
	if c=='e':
		print'End!!'
		break
	else:
		print'Read!!'
		RR.get_uid


