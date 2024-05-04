#!/usr/bin/env bash
# Install nginx web server, edit index.html file and configure redirection
FILE='/etc/nginx/sites-available/default'
NEW_URL='https://www.youtube.com/watch?v=QH2-TGUlwu4'
REDIR_404="\n\terror_page 404 /c_404.html;\n\tlocation = /c_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}"

apt-get -y update
apt-get -y install nginx
mkdir -p /var/www/html
echo 'Hello World!' > /var/www/html/index.html
mkdir -p /usr/share/nginx/html
sed -i "/server_name _;/a\ \trewrite ^/redirect_me ${NEW_URL} permanent;" $FILE
echo -e "Ceci n'est pas une page\n" > /usr/share/nginx/html/c_404.html
sed -i "/rewrite .* permanent;/a\ ${REDIR_404}" $FILE
service nginx restart
