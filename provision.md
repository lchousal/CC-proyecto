## Hito 2, provisionamiento con ansible

Primero se instala python
```
sudo apt-get install python
```
A continuación instalamos Ansible
```
sudo apt-get update
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```
En el archivp /etc/ansible/hosts añadimos la máquima virtual
```
[proyecto]
54.202.194.144
```
Creamos el playbook para el provisionamiento
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
Ejecutamos el playbook
```
ansible-playbook /etc/ansible/provision.yml
```
![5](https://user-images.githubusercontent.com/10090976/32722227-7fb82afa-c869-11e7-96e4-10838726998d.jpeg)
