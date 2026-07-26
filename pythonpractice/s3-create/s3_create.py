#!/usr/bin/env python3
"""Create an S3 bucket using boto3.

Usage:
  python s3_create.py --bucket my-unique-bucket-name --region us-west-2
"""
import argparse
import sys
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name: str, region: str = None, acl: str = None) -> bool:
    try:
        if region and region != "us-east-1":
            s3 = boto3.client("s3", region_name=region)
            create_kwargs = {
                "Bucket": bucket_name,
                "CreateBucketConfiguration": {"LocationConstraint": region},
            }
        else:
            s3 = boto3.client("s3")
            create_kwargs = {"Bucket": bucket_name}

        if acl:
            create_kwargs["ACL"] = acl

        s3.create_bucket(**create_kwargs)
        print(f"Bucket created: {bucket_name}")
        print(f"Bucket URL: https://{bucket_name}.s3.amazonaws.com/")
        return True
    except ClientError as e:
        print(f"Failed to create bucket: {e}")
        return False


def parse_args():
    parser = argparse.ArgumentParser(description="Create an S3 bucket")
    parser.add_argument("--bucket", "-b", required=True, help="Bucket name (must be globally unique)")
    parser.add_argument("--region", "-r", default=None, help="AWS region, e.g. us-west-2")
    parser.add_argument("--acl", help="Canned ACL for the bucket, e.g. private or public-read")
    return parser.parse_args()


def main():
    args = parse_args()

    ok = create_bucket(args.bucket, args.region, args.acl)
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
