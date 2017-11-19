# CC-proyecto
  Repositorio para el proyecto de la asignatura Cloud Computing

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

  Para la realización del provisionamiento de los servicios necesarios se utiliza Ansible.
  Se provisionarán los siguientes paquetes: git, python3, python3-pip, apache2 y mysql-server

## Licencia

  Este proyecto será liberado bajo la licencia [GNU GLP V3]
