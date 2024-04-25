import boto3
import os

s3_client = boto3.client('s3')
input_bucket = os.getenv('fhe-bucket/Inputs')
output_bucket = os.getenv('fhe-bucket/Outputs')

def read_numbers(bucket):
    nums = []
    response = s3_client.list_objects_v2(Bucket=bucket)
    for obj in response['Contents']:
        data = s3_client.get_object(Bucket=bucket, Key=obj['Key'])
        nums.extend(map(int, data['Body'].read().decode('utf-8').split()))
    return nums

def write_sum(bucket, total):
    s3_client.put_object(Bucket=bucket, Key='result.txt', Body=str(total))

def main():
    nums = read_numbers(input_bucket)
    total = sum(nums)
    write_sum(output_bucket, total)

if __name__ == "__main__":
    main()