#!/usr/bin/env python
import time
import sys

class piUSBReader:
	def __init__(self):
		print "RFID USB reader class Initiated "
		self.card1 = "001277"        
		self.card2 = "001349"         
		self.card3 = "001168"        
		self.card4 = "003940"        
		self.card5 = "001166"   
		
	def detectTagscontinously(self):
		print "Detect Tags Continously "
		with open('/dev/tty0', 'r') as tty:
			while True:
				RFID_input = tty.readline().rstrip()
				#print RFID_input[0]
				tmp=str(RFID_input)
				#print tmp
				if tmp==self.card1:
					print "Card 1 detected "
				if tmp==self.card2:
					print "Card 2 detected "
				if tmp==self.card3:
					print "Card 3 detected "
				if tmp==self.card4:
					print "Card 4 detected "
				if tmp==self.card5:
					print "Card 5 detected "
if __name__ == '__main__':
	piUSBReader=piUSBReader()
	piUSBReader.detectTagscontinously()
