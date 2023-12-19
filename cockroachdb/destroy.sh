#!/bin/env bash

kubectl delete -f cockroachdb-deployment.yaml
kubectl delete -f cockroachdb-local-storage.yaml