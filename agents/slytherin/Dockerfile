FROM openjdk:alpine
LABEL maintainer=pascalwhoop
LABEL name=powertac-client-slytherin_v1

#adding all the needed dependencies, as alpine is a bloody lightweight
RUN apk add --no-cache git maven

#docker usually acts mostly on the root filepath, as it's common for only one process to run inside of a container.
WORKDIR /powertac

#download the client
RUN git clone -b socket-grpc https://github.com/pascalwhoop/broker-adapter

#copy config and start the client
WORKDIR /powertac/sample-broker
RUN ls && mvn clean package


COPY broker.properties ./
COPY init.sh ./
EXPOSE 1234

CMD ./init.sh
