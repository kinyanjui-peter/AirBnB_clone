#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# Install nginx if it does not exist
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create a folder /data if it does not exist
if [ ! -d "/data" ]; then
    sudo mkdir /data
fi

# Create the folder /data/web_static/ if it doesn’t already exist
if [ ! -d "/data/web_static/" ]; then
    sudo mkdir -p /data/web_static/
fi
# Create the folder /data/web_static/releases/ if it doesn’t already exist
if [ ! -d "/data/web_static/releases/" ]; then
    sudo mkdir -p /data/web_static/releases/
fi
# Create the folder /data/web_static/shared/ if it doesn’t already exist
if [ ! -d "/data/web_static/shared/" ]; then
    sudo mkdir -p /data/web_static/shared/
fi
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
if [ ! -d "/data/web_static/releases/test/" ]; then
    sudo mkdir -p /data/web_static/releases/test/
fi
# sets up your web servers for the deployment of web_static

# A fake HTML file /data/web_static/releases/test/index.html 
# (with simple content, to test your Nginx configuration)
echo "<html>
  <head>
  </head>
  <body>
    <p>Test Web Static Deployment</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# A symbolic link /data/web_static/current linked to the
# /data/web_static/releases/test/ folder. If the symbolic link
# already exists, it should be deleted and recreated every time
# the script is run.
if [ -L "/data/web_static/current" ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
# (you can assume this user and group exist). This should be recursive;
# everything inside should be created/owned by this user/group.
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of 
# /data/web_static/current/ to hbnb_static
# (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart
# Nginx after updating the configuration:
sudo sed -i '/listen 80 default_server;/a location /hbnb_static {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default

sudo service nginx restart