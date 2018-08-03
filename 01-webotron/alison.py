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
for bucket in s3.buckets.all():
    print(bucket)
    
ec2_client = session.client('ec2')
get_ipython().run_line_magic('save', 'ipthonSesson.py 1-10')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cat', 'ipthonSesson.py')
get_ipython().run_line_magic('save', 'alison.py')
get_ipython().run_line_magic('save', 'alison.py 1-*')
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipthonSesson.py **')
get_ipython().run_line_magic('save', 'ipthonSesson.py *')
get_ipython().run_line_magic('save', 'alison.py 1-100')
