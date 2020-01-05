from __future__ import print_function

import os
import json
import urllib
import boto3

print('Loading function')

print('AWS_ACCESS_KEY_ID: ', os.environ.get('AWS_ACCESS_KEY_ID'))
print('AWS_SECRET_ACCESS_KEY: ', os.environ.get('AWS_SECRET_ACCESS_KEY'))
#print('AWS_S3_ENDPOINT_URL: ', os.environ.get('AWS_S3_ENDPOINT_URL'))
#s3_endpoint_url = os.environ.get('AWS_S3_ENDPOINT_URL')

s3_endpoint_url = 'http://minio:9000'
#http://boto3.readthedocs.io/en/latest/reference/services/s3.html#client
s3 = boto3.client('s3', endpoint_url=s3_endpoint_url)


def lambda_handler(event, context):

    print(event)
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    print('==== bucket information =====')
    print(bucket_name)
    print('=============================')


    #https://github.com/bloomberg/chef-bcs/blob/master/cookbooks/chef-bcs/files/default/s3-example-boto3.py
    print('==== your bucket list ====')
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        print(bucket.get('Name'))

    print('==== file list in bucket ====')
    # https://github.com/boto/boto3/issues/134
    AWS_S3_BUCKET_NAME = 'test'
    s3_resource = boto3.resource('s3', endpoint_url=s3_endpoint_url)
    bucket = s3_resource.Bucket(AWS_S3_BUCKET_NAME)
    result = bucket.meta.client.list_objects(Bucket=bucket.name, Delimiter='/')
    for o in result.get('Contents'):
        print(o.get('Key'))


    print('==== uploaded file ====')
    for rec in event['Records']:
        print(rec['s3']['object']['key'])
    print('=============================')

    print("Received event: " + json.dumps(event, indent=2))

