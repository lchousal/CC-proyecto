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
