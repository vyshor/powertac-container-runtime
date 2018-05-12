#!/bin/sh
#java -jar target/server-war-1.5.1-SNAPSHOT-spring-boot.jar -server -Xmx1024m
java -server -Xmx1024m -jar server.jar \
     --sim \
     --config server.properties \
     --brokers $BROKERS \
     --boot-data bootstrap-data.xml 
#java -Xdebug -Xrunjdwp:server=y,transport=dt_socket,address=8000,suspend=n \
#    -server -Xmx1024m -jar target/server-war-1.5.1-SNAPSHOT-spring-boot.jar --foo=bar

