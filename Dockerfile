FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3.8 python3-pip

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip3 install -r requirements.txt

CMD python3 /app/deployment.py
