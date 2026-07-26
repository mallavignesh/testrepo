#!/usr/bin/env python3
"""Delete an S3 bucket using boto3.

Usage:
  python s3_delete.py --bucket my-bucket-name --region us-west-2
  python s3_delete.py --bucket my-bucket-name --region us-west-2 --force
"""
import argparse
import sys
import boto3
from botocore.exceptions import ClientError


def empty_bucket(s3_resource, bucket_name: str) -> bool:
    try:
        bucket = s3_resource.Bucket(bucket_name)
        bucket.objects.all().delete()
        bucket.object_versions.all().delete()
        return True
    except ClientError as e:
        print(f"Failed to empty bucket {bucket_name}: {e}")
        return False


def delete_bucket(bucket_name: str, region: str = None, force: bool = False) -> bool:
    try:
        if region:
            s3 = boto3.resource("s3", region_name=region)
            client = boto3.client("s3", region_name=region)
        else:
            s3 = boto3.resource("s3")
            client = boto3.client("s3")

        if force:
            print(f"Emptying bucket before delete: {bucket_name}")
            if not empty_bucket(s3, bucket_name):
                return False

        client.delete_bucket(Bucket=bucket_name)
        print(f"Deleted bucket: {bucket_name}")
        return True
    except ClientError as e:
        print(f"Failed to delete bucket: {e}")
        return False


def parse_args():
    parser = argparse.ArgumentParser(description="Delete an S3 bucket")
    parser.add_argument("--bucket", "-b", required=True, help="Bucket name to delete")
    parser.add_argument("--region", "-r", default=None, help="AWS region for the S3 client")
    parser.add_argument("--force", action="store_true", help="Delete all objects in the bucket before removing the bucket")
    return parser.parse_args()


def main():
    args = parse_args()
    ok = delete_bucket(args.bucket, args.region, args.force)
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
