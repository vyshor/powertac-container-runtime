FROM openjdk:alpine
LABEL maintainer=pascalwhoop
LABEL name=powertac-grpc-adapter
###########################################

#adding all the needed dependencies, as alpine is a bloody lightweight
RUN apk add --no-cache git maven wget unzip protobuf

#getting proper glibc
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.27-r0/glibc-2.27-r0.apk && \
    apk add glibc-2.27-r0.apk

#docker usually acts mostly on the root filepath, as it's common for only one process to run inside of a container.
WORKDIR /powertac

#download the client
RUN mkdir -p powertac-grpc-adapter && \
    git clone https://github.com/pascalwhoop/sample-broker powertac-grpc-adapter

#copy config and start the client
WORKDIR /powertac/powertac-grpc-adapter
RUN apk add --no-cache bash

RUN mkdir -p /.m2
COPY settings.xml /root/.m2/

COPY broker.properties ./
COPY init.sh ./

#making a log folder that holds a subfolder with the name of the container content
RUN mkdir -p /log/powertac-grpc-adapter && ln -s /log/powertac-grpc-adapter /powertac/powertac-grpc-adapter/log

CMD ./init.sh
