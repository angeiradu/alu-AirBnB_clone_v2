#!/usr/bin/bash
# Script to setup web servers

# Install nginx
sudo apt-get install nginx

# Create test folder
mkdir '/data/web_static/releases/test/' -p

# Create a test HTML file
echo '<h1>Hello Nginx</h1>' > '/data/web_static/releases/test/index.html'

# Link the test directory to the current web_static
ln -sf '/data/web_static/current' '/data/web_static/releases/test'

# Change owner of the data folder to ubuntu of the ubuntu user group
# -R option to apply this change to every file recursively
chown -R ubuntu:ubuntu /data

# Writing the nginx configuration file for the static file server
echo "
http {
    include /etc/nginx/mime.types;
    
    server {
        listen 80;
	server_name getrelay.tech www.getrelay.tech;
	
	location /hbnb_static {
	    alias /data/web_static/current/;
        }
    }
}
" > /etc/nginx/nginx.conf
