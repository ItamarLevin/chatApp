FROM python:3.6-alpine

#creating rooms folder
WORKDIR /usr/src/app
RUN mkdir rooms
COPY requirements.txt ./
COPY index.html ./
RUN pip install --no-cache-dir -r requirements.txt
RUN export FLASK_APP=flaskApp.py

EXPOSE 5000

COPY . .

CMD cat /proc/self/cgroup | grep "docker" | sed s/\\//\\n/g | tail -1 > containerId.txt && flask run --host=0.0.0.0