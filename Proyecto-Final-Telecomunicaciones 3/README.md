# Balanceador de carga con haproxy y Datadog


## Descripción.
Este proyecto proporciona una guía detallada sobre la configuración de un balanceador de cargas utilizando HAProxy junto con tres máquinas Virtuales Ubuntu 22.04. Además, se integra Datadog como una interfaz de monitoreo para evaluar el rendimiento de una de las máquinas, en particular, el servidor HAProxy.

## Requisitos previos
Antes de comenzar con la configuración del balanceador de cargas, se deben tener en cuenta los siguientes requisitos:

1. Tener tres máquinas virtuales de Ubuntu instaladas y configuradas en la misma red.
2. Tener privilegios de superusuario en las tres máquinas, que para eso se usa el comando "sudo -i".
3. Tener instalado HAProxy en la máquina que actuará como balanceador de cargas.
4. Crear una cuenta en la página oficial de Datadog: https://www.datadoghq.com/ e instalar la aplicación.

## Creacion del archivo Vagrantfile
Se debe ejecutar el comando `Vagrant init` para crear el archivo y se configura asi en cualquier editor de texto:

# -- mode: ruby --
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	
	      if Vagrant.has_plugin? "vagrant-vbguest"
		            config.vbguest.no_install = true
		            config.vbguest.auto_update = false
		            config.vbguest.no_remote = true
  	    end
        config.vm.define :servidor do |servidor|
                servidor.vm.box = "bento/ubuntu-22.04"
		            servidor.vm.network :private_network, ip: "172.16.0.3"
                servidor.vm.network :private_network, ip: "192.168.50.3"
		            servidor.vm.network :public_network, bridge: "ethp", :dhcp => true
                servidor.vm.hostname = "servidor"
                servidor.vm.boot_timeout = 1000
        end
        config.vm.define :cliente do |cliente|
                cliente.vm.box = "bento/ubuntu-22.04"
                cliente.vm.network :private_network, ip: "192.168.50.2"
		            cliente.vm.network :forwarded_port, guest: 80, host:5567
		            cliente.vm.network :forwarded_port, guest: 443, host:5568
                cliente.vm.hostname = "cliente"
                cliente.vm.boot_timeout = 1000
        end
        config.vm.define :cliente2 do |cliente2|
                cliente2.vm.box = "bento/ubuntu-22.04"
                cliente2.vm.network :private_network, ip: "192.168.50.4"
                cliente2.vm.hostname = "cliente2"
                cliente2.vm.boot_timeout = 1000
        end
end


Una vez se haya configurado el archivo Vagrantfile, se procede a ejecutar el comando vagrant up para crear las tres máquinas virtuales. Se recomienda deshabilitar firewall con: sudo ufw disable.


# Configuración.
## Configuración de las máquinas virtuales.
1. Configuración de la primera máquina virtual

* Nombre de la maquina: servidor 
* IP: 192.168.50.3
* Sistema operativo: Ubuntu 22.04
* Servidor  instalado: haproxy y datadog-agent

**Para configurar HAProxy en el sistema, sigue los pasos a continuación**:

- Actualizar la lista de paquetes: Antes de instalar cualquier paquete, es una buena práctica actualizar la lista de paquetes disponibles. Abre una terminal y ejecuta: `sudo apt update`

- Instala los compiladores y dependencias necesarias utilizando el siguiente comando: `sudo apt install gcc libpcre3-dev tar make -y`.

- Instala haproxy en tu máquina utilizando el siguiente comando: `sudo apt-get install -y haproxy`.

- Finalmente, inicia el servicio de HAProxy: `sudo systemctl start haproxy`.

Con estos pasos, habrás instalado y configurado HAProxy en tu sistema Ubuntu. Asegúrate de haber ejecutado los comandos con permisos de superusuario o con el uso del comando sudo cuando sea necesario.


2. Configuración de la segunda máquina virtual
* Nombre de la maquina: backend1
* IP: 192.168.50.2
* Sistema operativo: Ubuntu 22.04
* Servidor web instalado: Apache  
Se debe instalar el servicio de apache2 con el siguiente comando: `sudo apt-get install apache2`, una vez instalado se debe crear un archivo index.html el cual se crea en la ruta `/var/www/html` y por ultimo se Ejecuta el siguiente comando para iniciar el servicio de Apache: `sudo systemctl start apache2`.
 

3. Configuración de la tercera máquina virtual
* Nombre de la maquina: backend2
* IP: 192.168.50.4
* Sistema operativo: Ubuntu 22.04
* Servidor web instalado: Apache  
Se debe instalar el servicio de apache2 con el siguiente comando: `sudo apt-get install apache2` una vez instalado se debe crear un archivo index.html el cual se crea en la ruta `/var/www/html` y por ultimo se Ejecuta el siguiente comando para iniciar el servicio de Apache: `sudo service apache2 start`.

# Configuración del balanceador de cargas

1. Ingresa al directorio correspondiente: `cd /etc/haproxy`. Configura el archivo `sudo vim haproxy.cfg`.
