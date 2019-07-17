#!/usr/bin/python
import piUSBReader
import time
import time
import os
import logging
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

## Custom pi packages
import pimqtt

card1 = "001277"        
card2 = "001349"         
card3 = "001168"        
card4 = "003940"        
card5 = "001166"
card6 = "003574"
card7 = "014333"
card8 = "001495"
card9 = "003589"
card10 = "001429"   
		
def run_test(self, params, packet):
	print(packet.payload)
	print("run_test executed ")
	respDict = json.loads(packet.payload)

	
pimqttclient = pimqtt.pimqttClient("pihome","atfgrotan9mr4-ats.iot.eu-central-1.amazonaws.com")
pimqttclient.mqttConfigureCertificates()
pimqttclient.mqttConfiguration()
pimqttclient.mqttConnect()
pimqttclient.mqttSubscribe("run/test",run_test)

piUSBReader=piUSBReader.piUSBReader()
	
counter=1
testData = {}

print "Detect Tags Continously "
					
while True:
	time.sleep(5)
	with open('/dev/tty0', 'r') as tty:
		while True:
			RFID_input = tty.readline().rstrip()
			print RFID_input[0]
			tmp=str(RFID_input)
			print tmp
			if tmp==card1:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':1,'Time':'3:15:21PM' }")
			if tmp==card2:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':2,'Time':'3:15:18PM' }")
			if tmp==card3:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':3,'Time':'3:15:12PM' }")
			if tmp==card4:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':4,'Time':'3:15:01PM' }")
			if tmp==card5:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':5,'Time':'3:15:23PM' }")
			if tmp==card6:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':6,'Time':'3:15:11PM' }")
			if tmp==card7:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':7,'Time':'3:15:12PM' }")
			if tmp==card8:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':8,'Time':'3:15:30PM' }")
			if tmp==card9:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':9,'Time':'3:15:45PM' }")
			if tmp==card10:
				pimqttclient.mqttPublish("suitcase/tag","{'ItemID':10,'Time':'3:15:25PM' }")
