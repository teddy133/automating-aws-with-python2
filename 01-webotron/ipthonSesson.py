# coding: utf-8
session = boto3.Session(profile_name='pythonAutomation')
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
new_bucket = s3.create_bucket(Bucket='automatingawsrobin--lastOf3')
new_bucket = s3.create_bucket(Bucket='Automatingawsrobin--lastOf3')
get_ipython().run_line_magic('history', '')
new_bucket = s3.create_bucket(Bucket='Automatingawsrobin--lastOf3', CreateBucketConfiguration={'LocationCOnstraint': 'us-east-2'})
new_bucket = s3.create_bucket(Bucket='Automatingawsrobin--lastOf3', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
new_bucket = s3.create_bucket(Bucket='automatingawsrobin--lastof3', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
