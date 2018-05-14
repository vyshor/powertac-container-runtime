mkdir -p /log/$clientname && ln -s /log/$clientname log
java -jar ./agent.jar --config broker.properties
