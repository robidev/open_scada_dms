#!/bin/bash


sudo docker compose up -d redis influxdb mongodb portainer # first start the databases, and container management console and let them initialise themselves
sleep 60 # wait about 60 seconds for mongodb to have been set up
sudo docker compose up -d mongoClientTemp # create the mongodb scada user when the database is done initialising
sleep 5 # ensure the mongodb user has been generated
sudo docker compose up -d # start everything else; scada_client, grafana, static_dataprovider, solver, ifs, mongodb admin panel, redis admin panel

