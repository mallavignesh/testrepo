#!/usr/bin/env python3
"""Upload a local file to an S3 bucket using boto3.

Usage:
  python s3_upload.py --bucket my-bucket-name --file ./local-file.txt --key uploaded-file.txt --region us-west-2
"""
import argparse
import os
import sys
import boto3
from botocore.exceptions import ClientError


def upload_file(bucket_name: str, file_path: str, object_name: str = None, region: str = None, acl: str = None) -> bool:
    if not os.path.isfile(file_path):
        print(f"Local file not found: {file_path}")
        return False

    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        if region:
            s3 = boto3.client("s3", region_name=region)
        else:
            s3 = boto3.client("s3")

        extra_args = {}
        if acl:
            extra_args["ACL"] = acl

        if extra_args:
            s3.upload_file(file_path, bucket_name, object_name, ExtraArgs=extra_args)
        else:
            s3.upload_file(file_path, bucket_name, object_name)

        print(f"Uploaded {file_path} to s3://{bucket_name}/{object_name}")
        return True
    except ClientError as e:
        print(f"Failed to upload file: {e}")
        return False


def parse_args():
    parser = argparse.ArgumentParser(description="Upload a file to an S3 bucket")
    parser.add_argument("--bucket", "-b", required=True, help="Target bucket name")
    parser.add_argument("--file", "-f", required=True, help="Path to the local file to upload")
    parser.add_argument("--key", "-k", help="S3 object key (defaults to local file name)")
    parser.add_argument("--region", "-r", default=None, help="AWS region for the S3 client")
    parser.add_argument("--acl", help="Canned ACL for the uploaded object, e.g. private or public-read")
    return parser.parse_args()


def main():
    args = parse_args()
    ok = upload_file(args.bucket, args.file, args.key, args.region, args.acl)
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
