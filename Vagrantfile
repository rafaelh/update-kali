Vagrant.configure("2") do |config|
  config.vm.box = "kalilinux/rolling"
  config.vm.hostname = "kali-v"
  config.vm.provision "shell", path: "vagrant-bootstrap.sh"
end