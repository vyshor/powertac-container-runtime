echo "Building server"
cd server/
./build.sh
cd ..
echo "Building slytherin"
cd agents/AgentUDE17/
./build.sh
cd ../../
