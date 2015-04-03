VAGRANTFILE_API_VERSION = "2"

Vagrant.configure VAGRANTFILE_API_VERSION do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.box_url = "https://dl.dropboxusercontent.com/u/88202830/ancor-precise64.box"

    config.vm.network :forwarded_port, guest: 80, host: 8000, auto_correct: true
    config.vm.provision :shell, path:"bootstrap.sh"
end
