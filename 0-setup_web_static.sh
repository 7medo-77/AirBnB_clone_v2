#!/usr/bin/env bash
# Bash script which sets up a web server for deployment of web_static project
html_content="
<html>
	<head>
		<style></style>
	</head>
	<body>
		<p>Sample paragraph</p>
	</body>
</html>
"
nginx_location="#\tlocation alias directive\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n
"
sudo apt update -y
sudo apt-get -y install nginx
mkdir -p /data/web-static/releases/test/
echo "$html_content" > /data/web-static/releases/test/index.html

mkdir -p /data/web-static/shared/

sudo ln -s -f /data/web-static/releases/test /data/web-static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/^\s*location \//i $nginx_location" /etc/nginx/sites-enabled/default

sudo service nginx restart
