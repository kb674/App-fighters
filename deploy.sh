#!/bin/bash

# Build image called flask-image
docker build -t flask-image .

# Run container called flask-app, as -e put in the actual database uri
docker run -d -p 5000:5000 --name flask-app -e DATABASE_URI="mysql+pymysql://user:password@ip_of_sql_instance/database_name" flask-image
