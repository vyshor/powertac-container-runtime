#!/usr/bin/env bash
VERSION=1.0
IMAGE=pascalwhoop/powertac-grpc-adapter

docker build --tag ${IMAGE}:${VERSION} ./
