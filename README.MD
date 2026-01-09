# Docker Learning

**A comprehensive, hands-on introduction to containers, networking, and multi-service systems.**

This repository is intended as a foundational learning resource for anyone seeking to understand Docker through straightforward, practical examples. Rather than learning Docker purely in theory, I have built multiple containerised applications, each illustrating a key Docker concept.
- Single containers
- Containerising applications
- Redis, MySQL, NginX as services
- Docker Compose orchestration
- Scaling containers with load balancing
- Persistent storage & environment variables
- Pushing & pulling images from public and private repositories (DockerHub & AWS ECR) 

### 1. hello_flask (Flask with MySQL)

#### This project teaches

 Connecting to MySQL database:
 - Install MySQL:   
 ```bash   
sudo apt update
sudo apt install mysql
```
- Connect to it on your application file
```python
import MySQLdb

db = MySQLdb.connect(
    host="mydb",           # Hostname of the MySQL container
    user="root",           # Username to connect to MySQL
    passwd="my-secret-pw", # Password for the MySQL user
    db="mysql"             # Name of the database to connect to
)
```
Multi-stage Dockerfile optimises container deployment by splitting the build into two stages.
The first stage handles building the application, while the second stage creates the final image. This approach reduces the image size, as it does not include all the dependencies needed for building the application.
```dockerfile
 #Stage 1: Build
    FROM python:3.8-slim as Build
    WORKDIR /app
    RUN apt-get update && apt-get install -y \
        gcc \
        python3-dev \
        libmariadb-dev \
        pkg-config
    COPY . .
    RUN pip install flask mysqlclient

    #Stage 2: Producion
    FROM python:3.11 slim
    WORKDIR /app
    COPY --from=Build /app /app
    EXPOSE 5002
    CMD ["python", "app.py"]
```
