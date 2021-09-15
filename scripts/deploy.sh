#!/usr/bin/env bash

set -u

die () { echo "$1" >&2; exit 1; }

export StackName="snowplow-enriched-s3-sinker-local"
export BucketName="snowplow-enriched-test-local"
export DataStreamName="snowplow-enriched-good-local"

# Prepare lambda package
echo "Starting lambda package"
docker-compose build package
if ! docker-compose run --rm package; then
  die "Failed to package lambda"
fi

# Deploy stack.
echo "Starting deployment of the stack $StackName"
docker-compose -f aws/docker-compose.yml build package
if ! docker-compose -f aws/docker-compose.yml run --rm package; then
  die "Failed to package stack $StackName"
fi
docker-compose -f aws/docker-compose.yml build deploy
if ! docker-compose -f aws/docker-compose.yml run --rm deploy; then
  die "Failed to deploy stack $StackName"
fi
