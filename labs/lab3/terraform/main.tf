
terraform {
  required_version = ">= 1.3.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
provider "aws" {
  region = "us-east-1"
}

# 1) Public S3 bucket with no versioning/encryption
resource "aws_s3_bucket" "public_assets" {
  bucket = "demo-public-assets-example-llmsec"
  acl    = "private"
  tags = { Purpose = "demo" }
}

resource "aws_s3_bucket_versioning" "public_assets" {
  bucket = aws_s3_bucket.public_assets.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "public_assets" {
  bucket = aws_s3_bucket.public_assets.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "public_assets" {
  bucket = aws_s3_bucket.public_assets.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# 2) Security group open to world
resource "aws_security_group" "open_sg" {
  name        = "open-sg"
  description = "Restricted inbound"
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["203.0.113.0/24"]
  }
  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["203.0.113.0/24"]
  }
}

# 3) Overly permissive IAM policy
resource "aws_iam_policy" "admin_policy" {
  name   = "AdminPolicy"
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action   = ["s3:ListBucket", "s3:GetObject"],
      Effect   = "Allow",
      Resource = [
        aws_s3_bucket.public_assets.arn,
        "${aws_s3_bucket.public_assets.arn}/*"
      ]
    }]
  })
}
