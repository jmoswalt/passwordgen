# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    # BOX
    config.vm.box = "precise64"


    # PROVISIONING
    config.vm.provision "shell", path: "vagrant_provision.sh"


    # PORTS
    # config.vm.network :forwarded_port, guest: inside the VM, host: in your normal environment (outside of the VM)

    config.vm.network :forwarded_port, guest: 80, host: 8005  # nginx


    # HOSTNAME and PATHS
    config.vm.hostname = "passwordgen"
    config.vm.synced_folder ".", "/opt/apps/passwordgen"


    # PROVIDERS
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", 256]
        vb.customize ["modifyvm", :id, "--cpuexecutioncap", "25"]
    end
end
