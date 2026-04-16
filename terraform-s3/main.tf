resource "aws_s3_bucket" "my_bucket" {
  bucket = "test-bucket-16042026"

  tags = {
    Name = "mybucket"
    Environment = "Dev"
  }
}