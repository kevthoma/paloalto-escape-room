import requests
# Run 'pip install "pymongo"' to use this
import pymongo
#import json

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

# MongoDB connection details
mongo_host = "mongodb-service"
mongo_port = 27017
mongo_db_name = "mongodb"
mongo_collection_name = "escape-room"

# Sample data to insert into MongoDB
data_to_insert = [
    {"output": posture_response.text}
]

# MongoDB connection
client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
db = client[mongo_db_name]
collection = db[mongo_collection_name]

# Insert data into MongoDB collection
result = collection.insert_many(data_to_insert)

# Print the inserted document IDs
print("Inserted IDs:", result.inserted_ids)
