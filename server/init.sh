#redirecting all logs to stdout
touch /powertac/server-distribution/log/broker1.trace
touch /powertac/server-distribution/log/broker2.trace
tail -f /powertac/server-distribution/log/*.trace | tee &

echo "Starting PowerTAC Server Container"
BROKERS="AgentUDE17,slytherin_v1"
mvn -Pcli -Dexec.args="--sim --brokers $BROKERS --config ./server.properties --boot-data bootstrap-data.xml"
