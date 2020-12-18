# import json 
# from kafka import SimpleProducer
# from kafka import KafkaClient 

# TOPIC = 'aerodata'

# # with open("AeroData.json") as f:
# # 	# print(f.read())
# # 	flightdata = json.load(f)
# f = open("AeroData.json").readlines()
# file = json.loads(f)
# # kafka = KafkaClient("localhost:9099")
# # producer = SimpleProducer(kafka)

# # producer.send_messages(TOPIC, json.dumps(f).encode('utf-8'))
# print(json.dumps(f).encode('utf-8'))

#--------------------------------------------------------------------------------------------
import requests, json
from kafka import SimpleProducer
from kafka import KafkaClient 

TOPIC = 'aerodata'

#url = "https://aerodatabox.p.rapidapi.com/aircrafts/reg/PH-BXO"

kafka = KafkaClient("localhost:9099")
producer = SimpleProducer(kafka)

headers = {
   'x-rapidapi-key': KEY ACCESS,
  'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
  }


list_reg = ["N709SW","N710SW","N723SW","N760SW","N404WN", "N405WN","N406WN","N408WN","N409WN","N410WN"]

for i in list_reg:
	url = "https://aerodatabox.p.rapidapi.com/aircrafts/reg/"+i 

	response = requests.request("GET", url, headers=headers)

	data = json.loads(json.dumps(response.text))

	producer.send_messages(TOPIC, data.encode('utf-8'))
	print(data)
