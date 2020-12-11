import boto3 
import botocore
from boto3.s3.transfer import S3Transfer 

BUCKET_NAME = 'saytusingh-enhance-it'



s3 = boto3.resource(service_name = 's3', region = 'us-west-2')
s3.meta.client.upload_file(Filename = '../../Desktop/Nissan_Image.jpg', Bucket = BUCKET_NAME, Key = 'lituation'+"/"+'Nissan_Image.jpg')