FROM centos:latest

RUN  yum install python3 -y

RUN pip3 install flask

RUN pip3 install pymongo

RUN pip3 install sklearn

RUN pip3 install pandas

WORKDIR /hara

COPY . .

CMD chmod +x app.py

CMD python3 app.py