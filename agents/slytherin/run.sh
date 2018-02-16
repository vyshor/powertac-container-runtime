#!/usr/bin/env bash
NAME=tac-agent-slytherin
docker rm $NAME
docker run --name $NAME pascalwhoop/powertac-client-slytherin_v1:1.0
