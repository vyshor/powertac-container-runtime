#!/usr/bin/env bash
NAME=powertac-grpc-adapter
docker rm $NAME
cur_dir=`pwd`
docker run --net host -v $cur_dir/log:/powertac/broker-adapter/log --name $NAME pascalwhoop/powertac-grpc-adapter:1.0
