# To Run application

## Start and SSH into Vagrant VM

```
vagrant up
vagrant ssh servidorWeb
```

## Run the webApp

```
install apache2 for seeing in a website and then:
move your files to: /var/www/
cd /var/www/webapp
export FLASK_APP=run.py
python3 -m flask run --host=0.0.0.0
```

```
for activate the site you must do this:
cd /etc/apache2/sites-available
create a page.conf and paste this:

<VirtualHost *:80>
ServerName 192.168.60.3
DocumentRoot /var/www/webapp

WSGIDaemonProcess app user=www-data group=www-data threads=5 python-home=/var/www/flask-app/flask-venv
#WSGIDaemonProcess app user=www-data group=www-data threads=5
WSGIScriptAlias / /var/www/webapp/flask-app.wsgi

ErrorLog ${APACHE_LOG_DIR}/flask-error.log
CustomLog ${APACHE_LOG_DIR}/flask-access.log combined

<Directory /var/www/webapp/web>
WSGIProcessGroup app
WSGIApplicationGroup %{GLOBAL}
Order deny,allow
Require all granted
</Directory>

Alias /static /var/www/webapp/web/static

<Directory /var/www/webapp/web/static>
Order allow,deny
Allow from all
</Directory>

</VirtualHost>
```

```
sudo a2ensite page.conf
sudo systemctl reload apache2
```
