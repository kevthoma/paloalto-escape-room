#!/bin/env bash

kubectl delete -f mysql-service.yaml
kubectl delete -f mysql-deployment.yaml
kubectl delete -f mysql-pvc.yaml
kubectl delete -f mysql-pv.yaml
