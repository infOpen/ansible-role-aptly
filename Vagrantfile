# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provision "ansible" do |ansible|

    # If we have a custom gpg key defined, test it, else skip gpg tasks
    if ENV['APTLY_CUSTOM_GPG_KEY_FILE'] and ENV['APTLY_CUSTOM_GPG_KEY_ID']
      ansible.extra_vars = {
        aptly_custom_gpg_key_file: "#{ENV['APTLY_CUSTOM_GPG_KEY_FILE']}",
        aptly_custom_gpg_key_id:   "#{ENV['APTLY_CUSTOM_GPG_KEY_ID']}"
      }
    else
      ansible.skip_tags = "custom_gpg"
    end

    # Playbook used to test role
    ansible.playbook  = "tests/test_vagrant.yml"

  end

end

