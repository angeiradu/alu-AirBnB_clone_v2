#!/usr/bin/env bash
# Script to setup web servers

# Install nginx
sudo apt-get install nginx -y

# Create test and shared directories
sudo mkdir '/data/web_static/releases/test/' -p
sudo mkdir '/data/web_static/shared' -p

# Create a test HTML file
echo '<h1>Hello Nginx</h1>' | sudo tee '/data/web_static/releases/test/index.html'

# Link the test directory to the current web_static
sudo ln -sf '/data/web_static/current' '/data/web_static/releases/test'

# Change owner of the data directory to ubuntu of the ubuntu user group
# -R option to apply this change to every file recursively
sudo chown -R ubuntu:ubuntu /data

# Set the permissions to 740
sudo chmod 600 /data -R

# Writing the nginx configuration file for the static file server
echo "
events {

}

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
" | sudo tee '/etc/nginx/nginx.conf'
