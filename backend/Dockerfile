# Step 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container at /app
COPY requirements.txt .

# Step 4: Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container at /app
COPY . .

# Step 6: Expose the port that FastAPI will run on (8000)
EXPOSE 8000

# Step 7: Define the command to start the FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
