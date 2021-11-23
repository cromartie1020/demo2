from python:3.8-slim-buster
workdir /app
copy demo2.json /etc/demo2.json
copy requirements.txt requirements.txt
run pip3 install -r requirements.txt
copy . .
cmd ["python3","manage.py","runserver","0.0.0.0:8000"]

