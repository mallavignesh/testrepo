# S3 Create Script

Small Python script to create an AWS S3 bucket using `boto3`.

Prerequisites
- Python 3.8+
- Install dependencies: `pip install -r requirements.txt`
- AWS credentials configured (environment variables or `~/.aws/credentials`)

Usage

```
python s3_create.py --bucket my-unique-bucket-name --region us-west-2
```

Upload a file

```
python s3_upload.py --bucket my-bucket-name --file ./local-file.txt --key remote-file.txt --region us-west-2
```

Delete a bucket

```
python s3_delete.py --bucket my-bucket-name --region us-west-2
```

Force delete a bucket and all objects

```
python s3_delete.py --bucket my-bucket-name --region us-west-2 --force
```

Options for creating a bucket
- `--bucket` / `-b`: Bucket name (required, must be globally unique)
- `--region` / `-r`: AWS region (default is `us-east-1` behavior)
- `--acl`: Optional canned ACL such as `private` or `public-read`

Options for uploading a file
- `--bucket` / `-b`: Target bucket name
- `--file` / `-f`: Local file path to upload
- `--key` / `-k`: S3 object key (defaults to the local file name)
- `--region` / `-r`: AWS region for the S3 client
- `--acl`: Optional canned ACL for the uploaded object, e.g. `private` or `public-read`

Options for deleting a bucket
- `--bucket` / `-b`: Bucket name to delete
- `--region` / `-r`: AWS region for the S3 client
- `--force`: Delete all objects in the bucket before removing the bucket

Notes
- Bucket names are global across AWS — pick a unique name.
- If you use `public-read` the bucket contents may be publicly accessible.
