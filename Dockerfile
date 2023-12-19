# Use an official Python runtime as a base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define the command to run your script
CMD ["python", "script.py"]