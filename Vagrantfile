Vagrant.configure("2") do |config|
  config.vm.box = "kalilinux/rolling"
  config.vm.hostname = "kali-v"
  config.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant"
  config.vm.provision "shell", path: "vagrant-bootstrap.sh"
end