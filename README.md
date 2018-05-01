# powerTAC Dockerized 4 Google Cloud Kubernetes / Docker Compose


This package can run the powerTAC server and a selected number of agents in a Kubernetes Cluster. For now, it's still
not working, but I am also thinking about switching to a simple docker-compose. I might later again transfer to
kubernetes but for now it's compose. 



**What is Kubernetes? What is a cluster?** [link](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
> In Kubernetes Engine, a container cluster consists of at least one cluster master and multiple worker machines called nodes. These master and node machines run the Kubernetes cluster orchestration system.
> A container cluster is the foundation of Kubernetes Engine: the Kubernetes objects that represent your containerized applications all run on top of a cluster.

## Structure

There are a few components that let the whole thing play out
- permanent storage, instantiated through provider (can be AWS, GCE, local)
- DNS resolver to let pods find each other
- services: to expose the GRPC endpoint that hooks into the powertac environment


## Installation
First, follow [these quickstart steps](https://cloud.google.com/kubernetes-engine/docs/quickstart) to receive an API key and enable billing.

If you don't mind using the Google Cloud Shell, feel free to use that. Otherwise use the Local Shell, either by following the steps described in the quickstart (installs it on your machine) linked above or by getting another docker container that runs the cloud-sdk as shown below. Details on [hub.docker.com](https://hub.docker.com/r/google/cloud-sdk/)

```
cd console
#this builds the kubernetes console that we can use to interact with their API and deploy our containers.
./build.sh
docker run -v ../:/powertac-docker -ti powertac-kubernetes-console:latest
```

This should put you into a console. A simple `gcloud auth login` triggers the auth process and you are now authorized in this container to use the gcloud sdk.

Now we are again following along the lines of the [quickstart](https://cloud.google.com/kubernetes-engine/docs/quickstart).

```
gcloud config set project [project-id]
gcloud config set compute/zone europe-west1-b #this one has GPU support which might come in handy at some point
gcloud container clusters create powertac-cluster #this takes a while
gcloud container clusters get-credentials powertac-cluster
```
And we are ready to start deploying containers into the Google Cloud from our machine.
<!--```
#pulls a docker image to use the google cloud sdk
docker pull google/cloud-sdk:alpine
```-->

## Local Installation

TODO Build init container that builds all images locally

Right now you need to build the images on the minikube cluster first and tag them appropriately because they aren't in any repositories.

## CRIU freezing of containers

Intall on Debian (Ubuntu)
[more info here](https://criu.org/Installation)
```
sudo apt install --no-install-recommends -y asciidoc xmlto libprotobuf-dev libprotobuf-c0-dev protobuf-c-compiler protobuf-compiler python-protobuf pkg-config build-essential iproute2 libcap-dev libnl-3-dev libnet-dev
cd /tmp
wget http://download.openvz.org/criu/criu-3.8.1.tar.bz2
tar -xvf criu-3.8.1.tar.bz2
sudo apt autoremove -y criu
cd criu-3.8.1 
make
make install 
```
