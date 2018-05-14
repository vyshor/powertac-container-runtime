IMAGE=pascalwhoop/powertac-client-ude17
if [ $# -eq 0 ]
  then
      tag='latest'
  else
    tag=$1
fi
docker build --tag ${IMAGE}:${tag} ./
