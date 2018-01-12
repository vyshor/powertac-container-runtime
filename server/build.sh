#building an image locally, based on jdk-alpine (a lightweight image base with java)
#this command builds an image and labels it. It uses the "Dockerfile" which is the default file name
docker build --tag powertac/server-distribution ./
