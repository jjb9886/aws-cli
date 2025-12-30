# AWS Resource Listing with Python

This repository contains Python scripts using `boto3` to list AWS resources.

## Features

- **EC2**: Lists instances and their state.  
- **Lightsail**: Lists instances and basic details.  
- **S3**: Lists buckets.  

All scripts use an IAM user with **read-only permissions**, following AWS least privilege best practices.

## Required Permissions

- `AmazonEC2ReadOnlyAccess`  
- `AmazonLightsailReadOnlyAccess`  
- `AmazonS3ReadOnlyAccess`  

## Security

- Credentials are loaded securely via the AWS CLI.  
- No resources are modified by these scripts.

