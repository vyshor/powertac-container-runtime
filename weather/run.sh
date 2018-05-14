
#instantiates a container from the just built image and exposes the two ports.
docker run --name powertac-weather  -v data:/data -e NB_UID=1000 -e NB_GID=1000 pascalwhoop/powertac-weather
