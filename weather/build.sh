#building an image locally, based on jdk-alpine (a lightweight image base with java)
#this command builds an image and labels it. It uses the "Dockerfile" which is the default file name
#!/usr/bin/env bash
if [ $# -eq 0 ]
  then
      tag='latest'
  else
    tag=$1
fi

docker build --tag pascalwhoop/powertac-weather:$tag ./
