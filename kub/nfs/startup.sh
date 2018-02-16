#!/usr/bin/env bash

#start external provisoner of storage
kubectl create -f nfs/provisioner/nfs-server-gce-pv.yaml
#nfs server that connects to RWOne abstract storage
kubectl create -f nfs/nfs-server-rc/yaml
#expose it as service
kubectl create -f nfs/nfs-server-service.yaml
#defined volume on top of nfs
kubectl create -f nfs/nfs-pv.yaml
#expose volume as claim for many pods
kubectl create -f nfs/nfs-pvc.yaml
