#!/usr/bin/python
import piUSBReader
import time
import time
import os
import logging
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import datetime

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
			data = {}
			data['Time'] = "3.15 PM"
			data['Place'] = "0"   ## 0: Wardrobe  1:Person  2:Suitcase
			if tmp==card1:
				data['ItemID'] = "1"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
			if tmp==card2:
				data['ItemID'] = "2"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
			if tmp==card3:
				data['ItemID'] = "3"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
			if tmp==card4:
				data['ItemID'] = "4"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
			if tmp==card5:
				data['ItemID'] = "5"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
			if tmp==card6:
				data['ItemID'] = "6"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
			if tmp==card7:
				data['ItemID'] = "7"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
			if tmp==card8:
				data['ItemID'] = "8"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
			if tmp==card9:
				data['ItemID'] = "9"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
			if tmp==card10:
				data['ItemID'] = "10"
				data['Name'] = "XXXXX"
				json_data = json.dumps(data)
				pimqttclient.mqttPublish("wardrobe/tag",json_data)
