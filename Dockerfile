# Use an official Python runtime as a parent image
FROM python:3.12

COPY . /app

WORKDIR /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which your Flask app will run
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
