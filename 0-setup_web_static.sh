#!/usr/bin/env bash
# sets up your web servers for the deployment
sudo apt - get update
sudo apt - get - y install nginx
sudo mkdir - p / data / web_static / shared / /data / web_static / releases / test/
echo "Holberton School" > /data / web_static / releases / test / index.html
sudo rm - rf / data / web_static / current
sudo ln - s / data / web_static / releases / test / /data / web_static / current
sudo chown - R ubuntu: ubuntu / data/
allias = "\\\tlocation /hbnb_static/ { alias /data/web_static/current/; }"
sed - i "38i $allias" / etc / nginx / sites - enabled / default
sudo service nginx restart
