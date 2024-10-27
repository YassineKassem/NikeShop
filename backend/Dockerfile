# Use an official Python runtime as a parent image
FROM python:3.11-slim as base

# Set the working directory inside the container
WORKDIR /app

# Install any dependencies specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Define the command to start the FastAPI application without --reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
