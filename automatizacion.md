# Hito 3, automatización de la creación de máquinas virutales

## Instalacines

Para poder realizar el provisionamiento tenemos que instalar ansible de la siguiente forma:
```
sudo apt-get update
sudo apt-get install python
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```
También hay que instalar jq:
```
sudo apt-get install jq
```
Para la creación de la máquina virtual instalaremos el cliente de azuere Azure CLI 2.0
```
sudo apt-get install azure-cli
```

## Creación y provisionamiento de la máquina virtual

Lo primero que debemos hacer es ejecutar el siguiente comando para conectarnos a nuestra cuenta de azure
```
az login
```
Después creamos el script para automatizar la creación y el provisionamiento.

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
Para el provisionamiento utilizaremos la siguiente receta de ansible:
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
Finalmente ejecutamos el scrit de automatización
```
sh acopio.sh
```
Si todo sale correctamente deberíamos obtener el siguiente resultado
![acopio](https://user-images.githubusercontent.com/10090976/33264366-861d7d0a-d36d-11e7-9891-2acc34332246.png)
