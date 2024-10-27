# Step 1: Build the React app
FROM node:18-alpine AS build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json into the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Vite will use (5173 is the default Vite port)
EXPOSE 5173

# Command to start Vite development server
CMD ["npm", "run", "dev", "--", "--host"]
