import boto3
import click


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

if __name__ == '__main__':
    cli()
