#!/bin/bash

docker rm -f fight-app mysql nginx

docker rmi fight-image

docker network rm fight-network
