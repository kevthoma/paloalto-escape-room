#!/bin/env bash

# Delete on minikube
kubectl delete -f escape-room-deployment.yaml

# Shut down minikube
minikube stop