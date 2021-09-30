# Snowplow Enriched S3 Sinker

### Introduction

This project gives your a **Kinesis Firehose** that consumes **Snowplow Enriched events** from a **Kinesis Data Stream** and drops them in your nominated **S3 bucket**.

Kinesis Firehose has the ability to transform records using a lambda function. This project also deploys a lambda function, that can transform Snowplow enriched events to JSON.

Kinesis Firehose has the ability to aggregate records for upto 15 minutes or until the data volume reaches to a threshold of 128 MB. This project uses maximum threshold for both time and volume. It also GZIPs the data before they are delivered to S3.

### How to use?

Navigate to `scripts/deploy.sh` in this project and replace the values of following variables with your value.
```bash
export StackName="snowplow-enriched-s3-sinker-local"
export BucketName="snowplow-enriched-test-local"
export DataStreamName="snowplow-enriched-good-local"
```

Make sure your terminal has necessary AWS Authentication setup through either of the followings;
1. AWS CLI credentials are stored in `$HOME/.aws/credentials` file. If you use a profile, your terminal has `AWS_PROFILE` variable with your profile name (e.g. `export AWS_PROFILE=<profile-name>`).
1. AWS credentials are available in your terminal as following variables:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_SECURITY_TOKEN (optional)
    - AWS_SESSION_TOKEN (optional)

**Important:** The default deployment region for this project is `ap-southeast-2`. To change that, navigate to `aws/docker-compose.yml` in this project.
