# Use the Python 3.11.5 slim image based on Debian Bullseye
FROM python:3.11.5-slim-bullseye

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev && apt-get clean

# Upgrade pip
RUN pip install --upgrade pip

# Copy your requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application files
COPY . .

# Specify the command to run your Django application
ENTRYPOINT [ "gunicorn", "core.wsgi"]