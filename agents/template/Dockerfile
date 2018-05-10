FROM openjdk:alpine
ARG clientname
ARG clientfile
LABEL maintainer=pascalwhoop
LABEL name=powertac-client-$clientname

#docker usually acts mostly on the root filepath, as it's common for only one process to run inside of a container.
WORKDIR /powertac

#download the client
#RUN wget http://www.powertac.org/wiki/images/c/c1/AgentUDE17.zip && \
#	unzip AgentUDE17.zip && \
#	rm AgentUDE17.zip

COPY $clientfile agent.jar
#copy config and start the client
COPY broker.properties ./
COPY init.sh ./

#making a log folder that holds a subfolder with the name of the container content
RUN mkdir -p /log/$clientname && ln -s /log/$clientname /powertac/log

CMD ./init.sh
