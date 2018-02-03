# CC-proyecto

[Web del proyecto](https://lchousal.github.io/CC-proyecto/index)

## Descripción del problema

  El TFG "Does every jazz musician leave a fingerprint?" necesitaba acceso un repositorio de partituras con el que entrenar los distintos algoritmos de MR

## Solución propuesta

  Se propone realizar un servicio para la creación y gestión de este repositorio

## Introducción descriptiva del proyecto

  El proyecto necesita:

  - Almacenamiento de los datos en una base de datos. Se utilizará mysql para la creación de la BBDD
  - Servicio que gestionara el repositorio de partituras. Se implementará con el lenguaje de programación Python

## Arquitectura

  Se utilizará una arquitectura basada en microservicios.

## Provision

  Para la realización del provisionamiento de los servicios necesarios se utiliza Ansible. Se ha escogido un provisionamiento con ansible ya que es una herramienta simple de utilizar y solo requiere tener instaldo python.
  Se provisionarán los siguientes paquetes: git, python3, python3-pip, apache2 y mysql-server.
  El provisionamiento se ha probado en máquinas de Amazon Web Services ya que es ácil de usar.

  Para una descripción más detallada de los pasos a seguir: [provision](https://github.com/lchousal/CC-proyecto/blob/gh-pages/provision.md)

## Automatización

  Se ha reaizado la automatización de la creación y provisionamiento de las máquinas virutales con el cliente de azure.Se ha escogido azure para probar otra tecnología de servivicios en la nube.
  Se ha utilizado una imagen de Ubuntu 16.04 para la creación de la máquina, esta elección se basa en la familiaridad con este SO por mi parte.

  Para una descripción más detallada de los pasos a seguir: [automatizacion](https://github.com/lchousal/CC-proyecto/blob/gh-pages/automatizacion.md)

  Despliegue:52.174.7.180


## Orquestación

  Se ha realizado la orquestación con Vagrant por su compatibilidad con el cliente de azure.
  Para una descripción más detallada de los pasos a seguir: [orquestacion](https://github.com/lchousal/CC-proyecto/blob/gh-pages/orquestacion.md)

  Despliegue Vagrant:13.95.83.41

## Contenedores

  Se ha utilizado Docker para el despliegue de aplicaciones en Contenedores. El servicio se proporciona a través de una imagen de debian, que se ha aprovisionado a través del fichero Dockerfile.
  Para una descripción más detallada de los pasos a seguir: [enlace](https://github.com/lchousal/CC-proyecto/blob/gh-pages/contenedores.md)

  Contenedor:https://proyectoservicio.azurewebsites.net/

  Dockerhub:https://hub.docker.com/r/lchousal/cc-proyecto/

## Composición

  Se ha utilizado Docker compose para la composición de servicios en contenedores docker. El servicio se proporciona a través de una imagen de alpine con python, que se ha aprovisionado a través del fichero Dockerfile.Se ha utilizado esta imagen por ser mucho más pequeña la mayoría de imagenes.
Para el contenedor volumen se ha utilizado la imagen busybox, esta imagen también se ha elegido por su pequeño tamaño y proporcionaa la funcionalidad esperada de que otros sitemas GNU homólogos.
  Para una descripción más detallada de los pasos a seguir: [enlace](https://github.com/lchousal/CC-proyecto/blob/gh-pages/composicion.md)

  Hito6:http://lchousalhito6cc.eastus.cloudapp.azure.com:5000/

## Licencia

  Este proyecto será liberado bajo la licencia [GNU GPL V3]
