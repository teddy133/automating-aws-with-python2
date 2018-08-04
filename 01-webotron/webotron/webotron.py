import boto3
import click
from botocore.exceptions import ClientError


session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "webotron deploys a website to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 BUckets"
    for bucket in s3.buckets.all():
      print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "Help list on the objects"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """ Raising the limits """
    try:
        s3_bucket = s3.create_bucket(Bucket=bucket, CreateBucketConfiguration={'LocationConstraint': session.region_name})

        policy = """
        {
          "Id": "Policy1533357798500",
          "Version": "2012-10-17",
          "Statement": [{
          "Sid": "Stmt1533357790398",
          "Action": "s3:*",
          "Effect": "Allow",
          "Resource": "arn:aws:s3:::{}/*",
          "Principal": {
            "AWS": [
              "*"
                ]
              }
            }
          ]
        }
        """.format(s3_bucket)
        policy = policy.strip()
        pol = s3_bucket.Policy()
        pol.put(Policy=policy)
        ws = new_bucket.Website()
        ws.put(WebsiteConfiguration={"ErrorDocument": {"Key": "error.html"}, "IndexDocument": {"Suffix": "index.html"}})
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            s3_bucket = s3.Bucket(bucket)
            print(s3_bucket)
        else:
            raise e


if __name__ == '__main__':
    cli()
