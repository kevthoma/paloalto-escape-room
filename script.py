# Imports
import requests
import json

# Declare Variables
base_url_login = "https://wgyl9brnpk.execute-api.us-east-1.amazonaws.com/prod/login"
base_url_with_token = "https://wgyl9brnpk.execute-api.us-east-1.amazonaws.com/prod/compliance/posture?timeType=relative&timeAmount=15&timeUnit=minute"
access_key_id = "testuser"
secret_access_key = "testpassword"

# Set username/password for CURL command
login_data = {
    "username": access_key_id,
    "password": secret_access_key
}

# Run the first CURL command to get the token
login_response = requests.post(base_url_login, json=login_data)
# Good username/password
if login_response.status_code == 200:
    # Save the token info
    token = login_response.json().get("token")

    # Run second CURL command with the 'token' value above
    posture_response = requests.get(base_url_with_token, headers={"token": token})

    # Write output to JSON file
    with open("data.json", "w") as file:
        file.write(posture_response.text)
        print("Data written to data.json")
# Bad username/password
else:
    print(login_response.status_code)