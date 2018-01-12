echo `pwd && dirname $0`
#docker run -ti powertac-kubernetes-console:latest
echo `dirname "$(readlink -f "$0")"`
