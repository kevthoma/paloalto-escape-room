# Use an official Python runtime as a base image
FROM python:latest

# Install 'requests' Python module
RUN pip install requests

# Install 'json' Python module
RUN pip install json

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define the command to run your script
CMD ["python", "script.py"]