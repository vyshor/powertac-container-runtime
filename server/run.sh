#!/usr/bin/env bash

docker rm powertac
#instantiates a container from the just built image and exposes the two ports.
docker run --name powertac  -v data:/powertac/data -e NB_UID=1000 -e NB_GID=1000 -p 8080:8080 -p 61616:61616 pascalwhoop/powertac-server
