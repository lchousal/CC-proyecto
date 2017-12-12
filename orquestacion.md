# Hito 4, orquestación con vagrant

## Instalaciones

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
