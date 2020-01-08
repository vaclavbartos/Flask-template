This is a simple example and quick-start template for micro web sites and services in Flask.


To get it running (on CentOS 7), install Apache and mod_wsgi with Python3.x support:

```
yum install epel-release
yum install python36 python36-devel httpd httpd-devel gcc

pip3 install mod_wsgi
mod_wsgi-express install-module > /etc/httpd/conf.modules.d/02-wsgi.conf

pip3 install flask
```

Quick start for testing (creates a temporary Apache config in /tmp and runs the server on port 8000):

```
mod_wsgi-express start-server wsgi_script.py
```
