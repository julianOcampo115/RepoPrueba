# To Run application

## Start and SSH into Vagrant VM

```
vagrant up
vagrant ssh servidorWeb
```

## Run the webApp

```
install apache2 for seeing in a website and then go to:
cd /var/www/webapp
export FLASK_APP=run.py
python3 -m flask run --host=0.0.0.0
```
