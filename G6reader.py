#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal

class Read_RFID:
	def get_uid(self):
		print 'Waiting for RFIDtag'
		# return uid in RFID
		rfid_uid = []
		# rfid_uid = [128,15,177,88]
		MIFAREReader = MFRC522.MFRC522()
		hex_uid = ''

		while True:
			(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

			# If a card is found
			if status == MIFAREReader.MI_OK:
				print "RFIDtag detected"
            # Get the UID of the card
			(status,uid) = MIFAREReader.MFRC522_Anticoll()
            # If we have the UID, continue
			if status == MIFAREReader.MI_OK:
				rfid_uid = uid
				break

        ###################
        # changes uid to hex number but on string
		for i in range(len(rfid_uid)):
			rfid_uid[i] = format(rfid_uid[i],'02x')

		for i in range(len(rfid_uid)):
			hex_uid = hex_uid + rfid_uid[i]
		return rfid_uid

		#return hex_uid
	def end_read(self):
		GPIO.cleanup()