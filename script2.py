import requests

# Your Job logic here

# Assuming you have some output from your Job
job_output = {"result": "some data from the job"}

# Example of storing the output in a database using API (replace URL and payload accordingly)
db_url = "http://database-service:port/store"
response = requests.post(db_url, json=job_output)

# Check the response
if response.status_code == 200:
    print("Output stored in the database.")
else:
    print("Failed to store output in the database.")
