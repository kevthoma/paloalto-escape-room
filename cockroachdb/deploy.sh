#!/bin/env bash

kubectl apply -f cockroachdb-local-storage.yaml
kubectl apply -f cockroachdb-deployment.yaml