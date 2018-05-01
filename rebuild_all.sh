echo "Building server"
cd server/
./build.sh
cd ..
echo "Building slytherin"
cd agents/slytherin/
./build.sh
cd ../../
