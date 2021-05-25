#!/bin/bash

# create docker network for fight-app and mysql database, called fight-network
docker network create fight-network

# build and run mysql container called mysql
docker run -d -e MYSQL_DATABASE=fight_db -e MYSQL_ROOT_PASSWORD=password --name mysql --network fight-network mysql:5.7

# create fight-image based on dockerfile
docker build -t fight-image .

# run fight-app container
docker run -d --network fight-network --name fight-app -e DATABASE_URI=mysql+pymysql://root:password@mysql/fight_db  fight-image

# create tables
docker exec -d fight-app python3 create.py

# Create nginx container
docker run -d --network fight-network --mount type=bind,source=$(pwd)/nginx/nginx.conf,target=/etc/nginx/nginx.conf -p 80:80 --name nginx nginx:alpine 
