mkdir -p cache
docker run -d --name mvn-cache --rm -v cache:/cache --net=host pascalwhoop/powertac-maven-proxy
