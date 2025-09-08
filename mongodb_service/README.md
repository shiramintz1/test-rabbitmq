# MongoDB Docker Setup - README

## Project Overview

In this project, I set up a MongoDB server running inside a Docker container.  
Using Docker allows running MongoDB in an isolated and portable environment without installing it directly on the host machine.

---

## Project Files

- `Dockerfile` – Defines the use of the official MongoDB image.

---

## How to Build and Run MongoDB

### 1. Build the Docker Image

Open a terminal in the project folder and run:

docker build -t my-mongo .

### 2. Run the MongoDB Container
docker run -d --name mongo-server my-mongo

### 3. Connect to the Database
Use the following connection string:
mongodb://localhost:27017