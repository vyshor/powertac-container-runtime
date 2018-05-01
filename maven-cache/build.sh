#!/usr/bin/env bash
if [ $# -eq 0 ]
  then
      tag='latest'
  else
    tag=$1
fi
IMAGE=pascalwhoop/powertac-maven-proxy

docker build --tag ${IMAGE}:${tag} ./
