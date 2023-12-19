#!/bin/env bash

# Start minikube
minikube start

# Use minikube 'docker' to pull and create images
eval $(minikube docker-env)

# Pull latest Python Docker image
docker pull python:latest

# Build Docker Image
docker build -t api-pod-image .

# Deploy on minikube
kubectl apply -f api-pod-deployment.yaml