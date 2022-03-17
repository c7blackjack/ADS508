import boto3
import sagemaker
import pandas as pd

client = boto3.client('s3')

resp = client.list_buckets()