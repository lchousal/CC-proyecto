# Hito 5, contenedores con Docker

Se ha creado una cuenta y se ha enlazado con el repositorio del proyecto de github (https://hub.docker.com/r/lchousal/cc-proyecto/)

## Contenedores

Para la creación del contenedor Docker utilzo el siguiente archivo Dockerfile

```
FROM debian:stable
MAINTAINER Lucia Chousal Rodriguez

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

RUN pip install flask

COPY contenedores/service.py /app

ENTRYPOINT ["python"]
CMD ["service.py"]
```

### Desliegue en azure

Se ejecutan los siguientes comandos:

```
az webapp deployment user set --user-name lchousal --password $password

az group create --name proyectoDocker --location "West Europe"

az webapp create --resource-group proyectoDocker --plan planProyecto --name proyectoServicio --deployment-container-image-name lchousal/cc-proyecto

az webapp config appsettings set -g proyectoDocker -n proyectoServicio --settings PORT=5000
```

Finalmente compribamos que el servicio funciona correctamente
![ok](https://user-images.githubusercontent.com/10090976/34886046-2cd68b8c-f7c2-11e7-9327-00df713ddab8.jpeg)
