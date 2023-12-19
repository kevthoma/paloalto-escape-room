#!/bin/env bash

# Delete on minikube
kubectl delete -f api-pod-job.yaml

# Shut down minikube
minikube stop