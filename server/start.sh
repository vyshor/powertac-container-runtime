#java -jar target/server-war-1.5.1-SNAPSHOT-spring-boot.jar -server -Xmx1024m
java -server -Xmx1024m -jar server-war.jar \
     --sim \
     --config server.properties \
     --brokers "AgentUDE17,slytherin_v1" \
     --boot-data bootstrap-data.xml 
#java -Xdebug -Xrunjdwp:server=y,transport=dt_socket,address=8000,suspend=n \
#    -server -Xmx1024m -jar target/server-war-1.5.1-SNAPSHOT-spring-boot.jar --foo=bar

