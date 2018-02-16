#!/bin/bash
# for docs see https://github.com/powertac/powertac-weather-server

#starting mysql daemon
/entrypoint.sh mysqld & > /data/mysqld.log
sleep 10 #waiting for db to start up

cd ../
/usr/share/tomcat7/bin/startup.sh
echo "waiting for tomcat"
sleep 5

mvn compile tomcat7:deploy
