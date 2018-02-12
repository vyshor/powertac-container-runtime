from mysql:5.7.21

LABEL maintainer=pascalwhoop
LABEL name=powertac-weather

ENV MYSQL_ROOT_PASSWORD my-secret-pw

#adding all the needed dependencies, as alpine is a bloody lightweight
RUN apt update && apt install -y --no-install-recommends python wget unzip git
# need to install certificates because the image came with none (for security)
RUN apt install -y --no-install-recommends ca-certificates
WORKDIR /weather
RUN git clone http://github.com/powertac/powertac-weather-server
RUN apt-get install -y libmysqlclient-dev python-dev python-pip && pip install MySQL-python

#powertac-server credentials expected by MySQL
ENV MYSQL_USER localUsername
ENV MYSQL_PASSWORD localPassword
ENV MYSQL_DATABASE powertac_weather

RUN apt install -y default-jdk maven tomcat7 tomcat7-admin
RUN cp /weather/powertac-weather-server/src/main/resources/weatherserver.properties.template /weather/powertac-weather-server/src/main/resources/weatherserver.properties && \
    cd powertac-weather-server && \
    mvn verify

#making tomcat happy
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
ENV CATALINA_BASE /var/lib/tomcat7
RUN mkdir -p /usr/share/tomcat7/logs && \
    mkdir -p /usr/share/tomcat7/temp
COPY tomcat-users.xml /var/lib/tomcat7/conf

EXPOSE 8080

COPY init.sh /
CMD /init.sh
