# For same account buckets' synchronisation

import boto3

def create_replication_rule(bucket_name_source, bucket_arn_destination):
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Define the replication configuration
    replication_config = {
        'Role': 'arn:aws:iam::ACCOUNT_ID:role/YOUR_ROLE',  # Replace with your IAM role ARN
        'Rules': [
            {
                'Filter': {
                    'Prefix': ''
                },
                'Status': 'Enabled',
                'Priority': 1,
                # Delete Marker Replication helps to sync delete from source to destination bucket
                'DeleteMarkerReplication': {
                    'Status': 'Enabled'
                },
                'Destination': {
                    'Bucket': bucket_arn_destination,
                }
            }
        ]
    }

    # Put the replication configuration
    response = s3_client.put_bucket_replication(
        Bucket=bucket_name_source,
        ReplicationConfiguration=replication_config
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Replication rule created successfully.")
    else:
        print("Error creating replication rule.")

if __name__ == "__main__":
    source_bucket = 'source-bucket-name'
    destination_bucket_arn = 'arn:aws:s3:::destination-bucket-name'

    create_replication_rule(source_bucket, destination_bucket_arn)
