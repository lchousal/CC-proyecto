# Hito 6, composición de servicios con Docker Compose

## Descripción del seervidio

Se ha creado un servicio que permite cargar un fichero nombrado de la forma indicada en la página pricipal.
![inicio](https://user-images.githubusercontent.com/10090976/35766467-b248d07c-08d9-11e8-9ed8-1ccf8474b745.jpeg)

El servicio almacenará el nombre del fichero en un archivo json que podrá tamvién ser consultado.
![lista](https://user-images.githubusercontent.com/10090976/35766474-c8773082-08d9-11e8-8959-c439c611a8c1.jpeg)

## Composición de servicios

Se han seguido los pasos de la iteración anterior [enlace](https://github.com/lchousal/CC-proyecto/blob/gh-pages/contenedores.md) para la creación de los Dockerfile necesarios para cada contenedor.

Además se ha creado el siguiente archivo docker-compose.yml para realizar la composición.

```
version: '2'

services:
  data:
    build: ./datos
    volumes:
      - ./datos:/servicio/datos
  web:
    build: ./web
    ports:
      - "5000:5000"
    links:
      - data
    volumes:
      - /tmp:/servicio/datos
    
volumes: 
data:
``` 

Para realizar la composición se utiliza el siguiente comando:
```
sudo docker-compose up
```

### Despliegue en azure

Para la realización del despliegue se ha utilizado azure.

Primero se crea el grupo de recusrsos de la siguiente manera:
```
az group create --name CC --location eastus
```
Luego se crea la máquina con el comando mostrado a continuación:

```
az group deployment create --resource-group CC --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/docker-simple-on-ubuntu/azuredeploy.json
```

Al ejecutar ese comando se nos pedirá introducir algunos datos como se muestra en la imagen.
![captura de pantalla de 2018-02-03 12-12-06](https://user-images.githubusercontent.com/10090976/35766590-8e639f14-08db-11e8-9379-ec448353a82a.jpeg)

A continuación accedemos a la máquina a través de ssh con los datos itroducidos, en este caso utilizamos el siguiente comando:
```
ssh lchousal@lchousalhito6cc.eastus.cloudapp.azure.com
```
Una vez dentro deberemos intalar git y clonar este repositorio.
Finalmente utilizamos el comando de composición
```
sudo docker-compose up -d
```
y accedemos al servicio através de la siguiente dirección: http://lchousalhito6cc.eastus.cloudapp.azure.com:5000/


