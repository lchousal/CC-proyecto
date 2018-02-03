FROM python:alpine
MAINTAINER Lucia Chousal Rodriguez

WORKDIR /servicio
COPY . /servicio

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["serv.py"]
