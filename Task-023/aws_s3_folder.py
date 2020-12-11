import boto3
import botocore
from boto3.s3.transfer import S3Transfer

BUCKET_NAME = 'enhance-it' 
KEY = 'Nissan_Image.jpg' 

s3 = boto3.resource(service_name = 's3')
s3.meta.client.upload_file(Filename = '../../Desktop/Nissan_Image.jpg', Bucket = BUCKET_NAME, Key ='lituation'+"/"+'Nissan_Image.jpg')