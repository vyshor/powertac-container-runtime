#!/usr/bin/env bash

docker rm powertac
#instantiates a container from the just built image and exposes the two ports.
#docker run -d --name powertac  -v powertac:/powertac -e NB_UID=1000 -e NB_GID=1000 -p 8080:8080 -p 61616:61616 vy6shor/powertac-server
docker run --name powertac  -e NB_UID=1000 -e NB_GID=1000 --net host vyshor/powertac-server
