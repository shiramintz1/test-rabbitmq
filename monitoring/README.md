
# Python Container Logging Monitoring with Filebeat and Elasticsearch

## Overview

This project demonstrates how to collect and monitor logs from a Python application running inside a Docker container using Filebeat and send them to Elasticsearch on Elastic Cloud for analysis and visualization.

---

## Project Components

- **Python app**: A simple Python script that writes logs every 5 seconds to a file inside the container.
- **Filebeat**: A lightweight log shipper that runs as a Docker container, reads the container logs, enriches them with Docker metadata, and forwards them to Elasticsearch.
- **Elasticsearch (Elastic Cloud)**: Cloud-hosted Elasticsearch service that stores and indexes the logs.
- **Kibana (Elastic Cloud)**: Web UI for searching, analyzing, and visualizing logs stored in Elasticsearch.



---

## Project Structure

- `app.py` - Python script generating logs.
- `Dockerfile` - Dockerfile for building the Python app image.
- `filebeat.yml` - Filebeat configuration file.
- `docker-compose.yml` - Docker Compose configuration to run both the Python app and Filebeat.

---

## Setup and Run

 **Build and start containers:**

   ```bash
   docker-compose up --build
   ```
3. **Verify:**

   - The Python app container writes logs to `/logs/app.log`.
   - Filebeat container collects logs from Docker containers and sends them to Elasticsearch.

4. **Access Kibana:**

   Log in to your Elastic Cloud Kibana dashboard and check the logs under the appropriate index (`filebeat-*`).

