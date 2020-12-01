import requests 
from kafka import SimpleProducer
from kafka import KafkaClient 

TOPIC = "southwest"

url = "https://southwest.p.rapidapi.com/flights/ATL/LGA/2020-12-01"

querystring = {"currency":"USD","adults":"1","seniors":"0"}


headers = {
    'x-rapidapi-key': "2b8b8aff91msh40899076aa199f5p1d5c2fjsnc1eb2ae5414d",
    'x-rapidapi-host': "southwest.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

text = response.text

kafka = KafkaClient("localhost:9099")
producer = SimpleProducer(kafka)

producer.send_messages(TOPIC, text.encode('utf-8'))
