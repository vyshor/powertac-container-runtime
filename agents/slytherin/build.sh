#!/usr/bin/env bash
VERSION=1.0
IMAGE=pascalwhoop/powertac-client-slytherin_v1

docker build --tag ${IMAGE}:${VERSION} ./
