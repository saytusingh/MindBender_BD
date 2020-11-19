from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer
from kafka import KafkaClient

ACCESS_TOKEN = "1322200647123587072-Ik1FWV3tCuNHKdfGdyc2mWL0Yl66pl"
TOKEN_SECRET = "M4hg3P365xO9J5YmgCkWhgQix81tCP5PFq44Yg52xNtfR"
CONSUMER_KEY = "CKSvqwiMXACGMVs9oLZd0hPUl"
CONSUMER_SECRET = "40ZEQzxmDkBYE5dFSoCyE9cAe1KvKy7Pdd2FjYmesi9qpUhhVc"
TOPIC = "tweets"


class StdOutListener(StreamListener):
  def on_data(self, data):
    producer.send_messages(TOPIC, data.encode('utf-8'))
    print(data)
    return True
  def on_error(self, status):
      print(status)

kafka = KafkaClient("localhost:9099")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
stream = Stream(auth, l)
stream.filter(track=TOPIC)
