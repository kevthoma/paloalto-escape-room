#!/bin/env bash

kubectl delete -f mongodb-service.yaml
kubectl delete -f mongodb-deployment.yaml