# Proyecto CC

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
  El provisionamiento se ha probado en máquinas de Amazon Web Services.

### Pasos a seguir

  * Primero se debe instalar python con en siguiente comando:
    ```
    sudo apt-get install python
    ```
  * A continuación instalamos Ansible
    ```
    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get update
    sudo apt-get install ansible
    ```
  * En el archivo /etc/ansible/hosts añadimos la máquima virtual
    ```
    [proyecto]
    54.202.194.144
    ```
  * Creamos el playbook para el provisionamiento
    ```
    ---
    - hosts: proyecto
      sudo: yes
      tasks:
        - name: Intalar paquetes
          apt: pkg=git state=present
          apt: pkg=python3 state=present
          apt: pkg=python3-pip state=present
          apt: pkg=apache2 state=present
          apt: pkg=mysql-server state=present
    ```
  * Ejecutamos el playbook
    ```
    ansible-playbook /etc/ansible/provision.yml
    ```
  Si hemos realizado correctamente el provisionamiento deberíamos obtener resultados similares a los de la imagen
  ![5](https://user-images.githubusercontent.com/10090976/32722227-7fb82afa-c869-11e7-96e4-10838726998d.jpeg)

## Automatización

  Se ha reaizado la automatización de la creación y provisionamiento de las máquinas virutales con el cliente de azure.Se ha escogido azure para probar otra tecnología de servivicios en la nube.
  Se ha utilizado una imagen de Ubuntu 16.04 para la creación de la máquina, esta elección se basa en la familiaridad con este SO por mi parte.

### Pasos a seguir

  * Primero debemos instalar ansible siguiendo los dos primeros pasos del apartado anterior

  * También hay que instalar jq:
    ```
    sudo apt-get install jq
    ```
  * Para la creación de la máquina virtual instalaremos el cliente de azuere Azure CLI 2.0
    ```
    sudo apt-get install azure-cli
    ```

  * Creación y provisionamiento de la máquina virtual

    * Lo primero que debemos hacer es ejecutar el siguiente comando para conectarnos a nuestra cuenta de azure
      ```
      az login
      ```
    * Después creamos el script para automatizar la creación y el provisionamiento.

      ```
      #!/bin/bash

      #Crear el gruppo de recursos
      echo ====================== Grupo de recursos ======================
      az group create -l westeurope -n CCGrupoLucia

      #Crear máquina virtual
      echo ======================= Maquina virtual =======================
      ipDir=$(az vm create -g CCGrupoLucia -n VMCCLucia --image UbuntuLTS --generate-ssh-keys | jq -r '.publicIpAddress')

      echo -name: VMCCLucia
      echo -ip: $ipDir

      #Realizar provisionamiento con ansible
      echo ================== Provisionamiento Ansible ===================
      ansible-playbook -i "$ipDir," provision.yml -u lucia
      ```
    * Para el provisionamiento utilizaremos la siguiente receta de ansible:
      ```
      ---
      - hosts: all
        sudo: yes
        tasks:
          - name: Intalar paquetes
            apt: pkg=git state=present
            apt: pkg=python3 state=present
            apt: pkg=python3-pip state=present
            apt: pkg=apache2 state=present
            apt: pkg=mysql-server state=present
      ```
    * Finalmente ejecutamos el scrit de automatización
      ```
      sh acopio.sh
      ```
  Si todo sale correctamente deberíamos obtener el siguiente resultado:
  ![acopio](https://user-images.githubusercontent.com/10090976/33264366-861d7d0a-d36d-11e7-9891-2acc34332246.png)


## Licencia

  Este proyecto será liberado bajo la licencia [GNU GLP V3]
