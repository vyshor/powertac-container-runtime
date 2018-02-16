FROM openjdk:alpine
LABEL maintainer=pascalwhoop
LABEL name=powertac-server

#adding all the needed dependencies, as alpine is a bloody lightweight
RUN apk add --no-cache bash vim git maven python

#docker usually acts mostly on the root filepath, as it's common for only one process to run inside of a container.
WORKDIR /powertac

#download the server-distribution from github
RUN mkdir data && \
	git clone -b release-1.4.3 https://github.com/powertac/server-distribution

#build once, so the downloading of the maven archives doesn't happen every time we instantiate a new docker container
RUN cd server-distribution && \
	mvn -Pcli


WORKDIR /powertac/server-distribution
COPY bootstrap-data.xml ./
COPY init.sh ./
COPY server.properties ./
#COPY weather.xml ./
EXPOSE 8080 61616

#and start it up
CMD /powertac/server-distribution/init.sh
