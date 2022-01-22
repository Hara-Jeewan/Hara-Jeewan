FROM centos:latest

RUN  yum install python3 -y

RUN pip3 install flask

RUN pip3 install pymongo

WORKDIR /hara

COPY . .

CMD chmod +x app.py

CMD python3 app.py