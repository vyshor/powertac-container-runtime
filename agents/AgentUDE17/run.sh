NAME=tac-agent-ude
docker rm $NAME
docker run --name $NAME pascalwhoop/powertac-client-ude17:1.0
