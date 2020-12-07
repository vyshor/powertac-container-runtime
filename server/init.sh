#!/bin/sh
#java -jar target/server-war-1.8.0-SNAPSHOT-spring-boot.jar -server -Xmx1024m
if [ -z $BROKERS ]
  then
      BROKERS='slytherin_v1'
fi

mkdir -p /log/server && ln -s /log/server log

java -server -Xmx1024m -jar server.jar \
     --sim \
     --config server.properties \
     --brokers $BROKERS \
     --boot-data bootstrap-data.xml 
#java -Xdebug -Xrunjdwp:server=y,transport=dt_socket,address=8000,suspend=n \
#    -server -Xmx1024m -jar target/server-war-1.8.0-SNAPSHOT-spring-boot.jar --foo=bar

