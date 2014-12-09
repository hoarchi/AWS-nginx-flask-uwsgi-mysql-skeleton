## AWS EC2 setting//linux-nginx-flask-uwsgi-mysql skeleton

### [ flask application setting ]

#### Install packages
	$ sudo yum install python26-devel nginx gcc gcc-c++ python-setuptools
	$ sudo easy_install pip
	$ sudo pip install uwsgi virtualenv
	$ sudo pip install flask flask-sqlalchemy flask-migrate python-gflags flask-oauth flask-wtf(install library on EC2)

#### Make directory and setting

	$ mkdir chuizonebeta
	$ cd chuizonebeta
	$ virtualenv venv
	$ . venv/bin/activate
	$ pip install -flask flask-sqlalchemy flask-migrate python-gflags flask-oauth flask-wtf(install library on venv)

#### Nginx setting(sudo vi /etc/nginx/nginx.conf)
	user root;
	server{
	listen 80
	server_name localhost;
	root /home/ec2-user;
	location / {
	try_files $uri @path;
	}
	location @path {
	include uwsgi_params;
	uwsgi_pass unix:/home/ec2-user/chuizonebeta/uwsgi.sock;
	}

#### uwsgi setting: make .ini (vi uwsgi.ini)
	[uwsgi]
	chdir = /home/ec2-user/chuizonebeta
	module = app:app
	venv = /home/ec2-user/chuizonebeta/venv
	socket = /home/ec2-user/chuizonebeta/uwsgi.sock
	master = True
	process = 2
	chmod-socket = 644
	daemonize = /home/ec2-user/chuizonebeta/logs/log.log
	pidfile = /home/ec2-user/chuizonebeta/mypid.pid

#### nginx start and stop 

	$ sudo service nginx start
    $ sudo service nginx stop

#### make log.log 
	$ mkdir logs
	$ uwsgi --ini uwsgi.ini (application start)
	$ vi logs/log.log (view log file)
	$ vi tail logs/log.log (last 10 sentences of log file)

#### make shell script file
	$ vi mypid.pid (you can see 4 numbers if you start your application)

	$ vi restart.sh
		kill -9 $(cat mypid.pid)
		uwsgi --ini uwsgi.ini

#### start shell script file 
	$ sh restart.sh

#### check your file in your directory
	$ ls
		logs mypid.pid restart.sh uwsgi.ini uwsgi.sock venv
#### $ vi main.py
	from app import app
	app.run(app)

#### $ (/app) vi __init__.py
	from flask import Flask
	app = Flask(__name__)
	if __name__ == "__main__":
	  app.run(host='0.0.0.0')
	from app import views

#### $ (/app) vi views.py
	from app import app
	@app.route('/')
	def main():
	     return 'HELLO Wolrd'

#### (venv) pip install libraryname
/venv/site-package 안에 설치됨

#### mysql 설치
	$ sudo yum install mysql
	$ sudo yum install mysql-server
	$ sudo yum install mysql-devel
	$ sudo chgrp -R mysql /var/lib/mysql
	$ sudo chmod -R 770 /var/lib/mysql
	$ sudo service mysqld start

	$ /usr/bin/mysqladmin -u root password yourpasswordhere
	
	mysql> CREATE USER 'myuser'@'localhost' IDENTIFIED BY 
	    -> 'yourpasswordhere';
	mysql> GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'localhost'
	    -> WITH GRANT OPTION;
	mysql> CREATE USER 'myuser'@'%' IDENTIFIED BY 'yourpasswordhere';
	mysql> GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%'
	    -> WITH GRANT OPTION;

	$ mysql -u root -p
	mysql> show databases;
	musql> create database dbname;

	$ sudo yum install MySQL-python
	$ /app> (venv) pip install MySQL-python
 

#### Etc
	* All copyright reserved CODAA lab
	* something Q&A below herer