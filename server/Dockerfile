FROM openjdk:alpine
LABEL maintainer=vyshor
LABEL name=powertac-server


#docker usually acts mostly on the root filepath, as it's common for only one process to run inside of a container.
WORKDIR /powertac
RUN mkdir data 

COPY bootstrap-data.xml ./
COPY init.sh ./
COPY server.properties ./
#assumes a built server jar is in the target folder of this project
COPY target/server-jar-1.8.0-SNAPSHOT.jar server.jar


EXPOSE 8080 61616
#and start it up
CMD "/powertac/init.sh"
