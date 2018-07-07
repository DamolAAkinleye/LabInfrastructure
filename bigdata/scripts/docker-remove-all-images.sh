#!/bin/bash

echo 'Deleting all containers...'
docker rm $(docker ps -a -q)

echo 'Deleting all images...'
docker rmi $(docker images -q)