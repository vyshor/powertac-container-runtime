FROM google/cloud-sdk:alpine
RUN apk --update add openjdk7-jre
RUN gcloud components install app-engine-java kubectl
WORKDIR /powertac-docker
RUN git clone https://github.com/pascalwhoop/powertac-kubernetes
