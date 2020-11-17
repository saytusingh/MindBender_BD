import requests
from kafka import SimpleProducer
from kafka import KafkaClient

TOPIC = "flights"

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

querystring = {"query":"Stockholm"}

headers = {
    'x-rapidapi-key': "2b8b8aff91msh40899076aa199f5p1d5c2fjsnc1eb2ae5414d",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
text = response.text

kafka = KafkaClient("localhost:9099")
producer = SimpleProducer(kafka)
producer.send_messages(TOPIC, text.encode('utf-8'))
