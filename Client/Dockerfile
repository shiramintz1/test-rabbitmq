# Using official Node.js image as the base
FROM node:18

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if exists)
COPY package*.json ./

# Disable strict SSL for npm (if needed) and install dependencies
RUN npm config set strict-ssl false && npm install

# Copy the rest of the application code
COPY . .

# Declare a volume for persistent storage or for sharing files with the host
VOLUME ["/app/output"]

# Expose port 3000 for the app
EXPOSE 3000

# Start the app using npm start
CMD ["npm", "start"]
