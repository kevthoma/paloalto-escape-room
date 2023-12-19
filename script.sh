#!/bin/env bash

BASE_URL="https://wgyl9brnpk.execute-api.us-east-1.amazonaws.com/prod"
# ACCESS_KEY_ID="testuser"
# SECRET_ACCESS_KEY="testpassword"
TOKEN=`curl -L -X POST "$BASE_URL/login" --data '{"username":"testuser", "password":"testpassword"}' | cut -d'"' -f4`

curl -L -X GET "$BASE_URL/compliance/posture?timeType=relative&timeAmount=15&timeUnit=minute" --header "token: $TOKEN" | tee data.json