# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask web application
EXPOSE 5000

# Set the command to run the Flask application
CMD ["python", "server.py"]
