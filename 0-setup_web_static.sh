#!/usr/bin/env bash
# Sets up my web servers for web_static deployment.
sudo apt-get update
sudo apt-get -y install nginx

# Create directories if they don't already exist
mkdir -p /data/web_static/releases/test
mkdir /data/web_static/shared/

# Create test html file
fake_file=/data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolbertonSchool\n\t</body>\n<\html>" | sudo tee $fake_file

# Create sym link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to ubuntu user and groups
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static (ex: https://jinjis.space/hbnb_static)
config_file=/etc/nginx/sites-available/default
sed '29a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $config_file
service nginx restart
