#!/bin/bash
# for docs see https://github.com/powertac/powertac-weather-server

#starting mysql daemon
/entrypoint.sh mysqld & > /data/mysqld.log
sleep 10 #waiting for db to start up



cd /weather/powertac-weather-server/scripts/

#downloading the weather data
wget http://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/uurgeg_344_2001-2010.zip
wget http://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/uurgeg_344_2011-2020.zip
unzip uurgeg_344_2001-2010.zip
unzip uurgeg_344_2011-2020.zip

cd ../
/usr/share/tomcat7/bin/startup.sh
echo "waiting for tomcat"
sleep 5
mvn compile tomcat7:deploy


cd scripts/
mysql -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE < powertac_weather.sql
echo "importing data into database with python"
python2.7 import_knmi_data.py > /data/py_import.log 2> /data/py_import_error.log

#fixing file first (wrong city)
echo "exporting data into xml file with python"
sed -i -e 's/minneapolis/rotterdam/g' create_sim_weather.py
python2.7 create_sim_weather.py 20100101 > /data/py_export.log 2> /data/py_export_error.log
echo "moving exported weather to target destination"
mv weather.xml /data
echo "all done, goodbye"
sleep 10000
