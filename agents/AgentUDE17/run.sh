NAME=powertac-agent-ude
docker kill $NAME
docker rm $NAME
docker run -d --net host --name $NAME -v powertac:/powertac pascalwhoop/powertac-client-ude17:latest
tail -f log/broker1.trace
