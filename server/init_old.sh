#redirecting all logs to stdout
echo "Starting PowerTAC Server Container"
BROKERS="AgentUDE17,slytherin_v1"
mvn -Pcli -Dexec.args="--sim --brokers $BROKERS --config ./server.properties --boot-data bootstrap-data.xml"
