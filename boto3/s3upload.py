import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file(r"C:\Users\Avinash Kumar\OneDrive\Desktop\hello.txt" , 'avinashkumar07', 'hello.txt')