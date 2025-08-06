# Use official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /src

# Copy the application files
COPY . /src

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
