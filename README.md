AWS EC2 setting//linux-nginx-flask-uwsgi-mysql skeleton

AWS flask application 세팅하기

1. 패키지 설치
sudo yum install python26-devel nginx gcc gcc-c++ python-setuptools
sudo easy_install pip
sudo pip install uwsgi virtualenv
sudo pip install flask flask-sqlalchemy flask-migrate python-gflags flask-oauth flask-wtf(리눅스에 lib 설치)

2. 작업폴더 생성, 세팅

mkdir chuizonebeta
cd chuizonebeta
virtualenv venv
. venv/bin/activate
pip install -flask flask-sqlalchemy flask-migrate python-gflags flask-oauth flask-wtf(flask에 lib 설치)

3. Nginx 세팅(sudo vi /etc/nginx/nginx.conf)
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

4. uwsgi 세팅, .ini 파일(vi uwsgi.ini로 화일생성 후 작성하고 저장)
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

5. sudo service nginx start
    (sudo service nginx stop)

6. 로그화일 생성 
mkdir logs
어플리케이션 다시 시작하기 uwsgi --ini uwsgi.ini
로그 보기 vi logs/log.log
마지막 10줄 보기tail logs/log.log

7. 쉘 스크립트 화일 생성
vi mypid.pid (숫자뜨는지 확인)

vi restart.sh
kill -9 $(cat mypid.pid)
uwsgi --ini uwsgi.ini

sh restart.sh (쉘 스크립트 화일 실행)

8. ls로 생성된 화일 확인
logs mypid.pid restart.sh uwsgi.ini uwsgi.sock venv

9. vi main.py
from app import app
app.run(app)

10. (/app) vi __init__.py
from flask import Flask
app = Flask(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0')
from app import views

11. (/app) vi views.py
from app import app
@app.route('/')
def main():
     return 'HELLO Wolrd'

12. (venv) pip install libraryname
/venv/site-package 안에 설치됨

13. mysql 설치
http://samstarling.co.uk/2010/10/installing-mysql-on-an-ec2-micro-instance/

mysql -u root -p
show databases;
create database dbname;

sudo yum install MySQL-python
app폴더 (venv) pip install MySQL-python
 

