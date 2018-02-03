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

## Orquestación

  Se ha realizado la orquestación con Vagrant por su compatibilidad con el cliente de azure.

### Pasos a seguir

  Para realizar la orquestación de este proyecto hay que tener instalado ansible y el cliente de azure.

  También debemos instalar vagrant, he utilizado la versión 2.0.1. Es necesario también el plugin de azure en la versión 2.0.0.

  ##Creación de la orquestación

  Antes de nada debemos loguearnos en el cliente de azure.
  Para poder crear las máquinas virtuales necesitamos la siguiente información sobre nuestra cuenta:
    - tenant id
    - client id
    - client secret
    - subscription id

  Para ello utilizaremos los siguientes comandos:
  ```
  az add create-for-rbac
  az account list --query "[?isDefault].id" -o tsv
  ```
  Después debemos de crear el archivo VagrantFile
  ```
  Vagrant.configure("2") do |config|

    config.vm.define "remoteLucia1" do |serviceObject|
      serviceObject.vm.box = 'azure'

      serviceObject.ssh.private_key_path = '~/.ssh/id_rsa'

      serviceObject.vm.provider :azure do |azure, override|
        #Set a territory
        azure.location="westeurope"

        azure.resource_group_name="grupoLucia"
        azure.vm_name="remoteLucia1"

        azure.vm_image_urn="credativ:Debian:8:latest"

        azure.tenant_id = ENV['AZURE_TENANT_ID']
        azure.client_id = ENV['AZURE_CLIENT_ID']
        azure.client_secret = ENV['AZURE_CLIENT_SECRET']
        azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

      end
      serviceObject.vm.provision "ansible" do |ansible|
        ansible.playbook = "provision.yml"
      end
    end

    config.vm.define "remoteLucia2" do |serviceImage|
      serviceImage.vm.box = 'azure'

      serviceImage.ssh.private_key_path = '~/.ssh/id_rsa'

      serviceImage.vm.provider :azure do |azure, override|
        #Set a territory
        azure.location="westeurope"

        azure.resource_group_name="grupoLucia"
        azure.vm_name="remoteLucia2"

        azure.vm_image_urn="credativ:Debian:8:latest"

        azure.tenant_id = ENV['AZURE_TENANT_ID']
        azure.client_id = ENV['AZURE_CLIENT_ID']
        azure.client_secret = ENV['AZURE_CLIENT_SECRET']
        azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

      end
      serviceImage.vm.provision "ansible" do |ansible|
        ansible.playbook = "provision.yml"
      end
    end
  end
  ```
  Esta vez se ha utilizado una imagen de Debian 8 para probar su funcionamiento.

  Finalmente ejecutaremos el archivo vagrantFile con el siguiente comando
  ```
   vagrant up --no-parallel
  ```


## Contenedores

  Se ha utilizado Docker para el despliegue de aplicaciones en Contenedores. El servicio se proporciona a través de una imagen de debian, que se ha aprovisionado a través del fichero Dockerfile.

### Pasos a seguir

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

## Composición

### Pasos a seguir

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
## Licencia

  Este proyecto será liberado bajo la licencia [GNU GPL V3]
