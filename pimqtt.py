#!/usr/bin/python
import time
import os
import logging
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
    
##python aws-iot-device-sdk-python/samples/basicPubSub/basicPubSub.py -e atfgrotan9mr4-ats.iot.eu-central-1.amazonaws.com -r root-CA.crt -c pla_hackathon_raspberry_generic.cert.pem -k pla_hackathon_raspberry_generic.private.key%

def run_customCallback(self, params, packet):
	print("run_testfunction executed ")
	print(packet.payload)
	respDict = json.loads(packet.payload)
	print(respDict["message"])
	
class pimqttClient:
	def __init__(self,mqttClient,endPoint):
		self.mqttClient = AWSIoTMQTTClient(mqttClient) 
		self.mqttClient.configureEndpoint(endPoint,8883)
		print("pimqttClient Initialization successfull ")
	
	def mqttConfigureCertificates(self):
		self.mqttClient.configureCredentials("/home/pi/iot/python/root-CA.crt", "/home/pi/iot/python/pla_hackathon_raspberry_generic.private.key","/home/pi/iot/python/pla_hackathon_raspberry_generic.cert.pem" )
   
	def mqttConfiguration(self):
		self.mqttClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
		self.mqttClient.configureDrainingFrequency(2) # Draining: 2 Hz
		self.mqttClient.configureConnectDisconnectTimeout(10) # 10 sec
		self.mqttClient.configureMQTTOperationTimeout(5) # 5 sec

	def mqttConnect(self):
		self.mqttClient.connect()
		print("pimqttClient Connection successfully ")

	def mqttSubscribe(self, topic,customCallback):
		self.mqttClient.subscribe(topic, 1, customCallback)

	def mqttunSubscribe(self, topic):
		self.mqttClient.unsubscribe(topic)

	def mqttPublish(self, topic , payload):
		self.mqttClient.publish(topic, payload, 0)

	def mqttDisconnect(self):
		self.mqttClient.disconnect()
		print("pimqttClient Disconnected successfully ")
			
if __name__ == "__main__":
	### Use this to test the Mqtt connection
	pimqttclient = pimqttClient("pihome","atfgrotan9mr4-ats.iot.eu-central-1.amazonaws.com")
	pimqttclient.mqttConfigureCertificates()
	pimqttclient.mqttConfiguration()
	pimqttclient.mqttConnect()
	pimqttclient.mqttDisconnect()
	pimqttclient.mqttConnect()
	pimqttclient.mqttSubscribe("run/sub",run_customCallback)
	count=1
	testData = {}
	while True:
		time.sleep(5)
		testData['count'] = count
		jtestData = json.dumps(testData)
		pimqttclient.mqttPublish("run/pub",jtestData)
		print("Publish Test Data "+ str(count))
		count=count+1
		
