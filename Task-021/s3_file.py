import boto3

s3 = boto3.resource('s3')

s3.Bucket("bdmindbender12345").put_object(Key="Nissan_Image.jpg", Body="/home/fieldemployee/Desktop/exterior_02-1440x960.jpg")

s3.Bucket("bdmindbender12345").download_file(Key="exterior_02-1440x960.jpg", Filename="Nissan_Image.jpg")





#BUCKET_NAME = 'bdmindbender12345'
#KEY = 'exterior_02-1440x960.jpg'

#session = boto3.Session(aws_access_key_id ="AKIAIJAHRB7PNRQ24OAQ",
#aws_secret_access_key = "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")
#obj = s3.Object(BUCKET_NAME,KEY)
#body = obj.get()['Body'].read()
