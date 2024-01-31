#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
if ! dpkg -s nginx > /dev/null 2>&1;
then
    sudo apt-get -y install nginx
fi
if [ ! -d /data/ ]
then
    sudo mkdir /data/
fi
if [ ! -d /data/web_static/ ]
then
    sudo mkdir /data/web_static/
fi
if [ ! -d /data/web_static/releases/ ]
then
    sudo mkdir /data/web_static/releases/
fi
if [ ! -d /data/web_static/shared/ ]
then
    sudo mkdir /data/web_static/shared/
fi
if [ ! -d /data/web_static/releases/test/ ]
then
    sudo mkdir /data/web_static/releases/test/
fi
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "
    location /hbnb_static/ {
        alias /data/web_static/current/
    }" | sudo tee -a /etc/nginx/sites-available/default
