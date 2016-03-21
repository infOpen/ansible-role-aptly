# aptly

[![Build Status](https://travis-ci.org/infOpen/ansible-role-aptly.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-aptly)

Install aptly package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role contains two tests methods :
- locally using Vagrant
- automatically with Travis

### Testing dependencies
- install [Vagrant](https://www.vagrantup.com)
- install [Vagrant serverspec plugin](https://github.com/jvoorhis/vagrant-serverspec)
    $ vagrant plugin install vagrant-serverspec
- install ruby dependencies
    $ bundle install

### Running tests

#### Run playbook and test

- if Vagrant box not running
    $ vagrant up

- if Vagrant box running
    $ vagrant provision

## Role Variables

### Default role variables

Follow the possible variables with their default values

    # Custom gpg key
    aptly_custom_gpg_key_file : False
    aptly_custom_gpg_key_id   : False

    # User settings
    aptly_user    : aptly
    aptly_group   : aptly
    aptly_user_home : "/var/lib/aptly"

    # Software settings
    aptly_version       : "0.9.5"
    aptly_activate_api  : False
    aptly_gpg_key       : E083A3782A194991
    aptly_gpg_keyserver : "hkp://pgp.mit.edu" # "hkp://keys.gnupg.net" : timeout
    aptly_repository    : "deb http://repo.aptly.info/ squeeze main"

    # Aptly configuration
    aptly_rootdir : "{{ aptly_user_home }}"
    aptly_download_concurrency : 4
    aptly_download_speed_limit : 0
    aptly_architectures : []
    aptly_dependency_follow_suggests : False
    aptly_dependency_follow_recommends : False
    aptly_dependency_follow_all_variants : False
    aptly_dependency_follow_source : False
    aptly_gpg_disable_sign : False
    aptly_gpg_disable_verify : False
    aptly_download_source_packages : False
    aptly_ppa_distributor_id : "ubuntu"
    aptly_ppa_codename : ""
    aptly_s3_publish_endpoints : {}
    aptly_swift_publish_endpoints : {}

    # Mirror management
    #------------------
    aptly_mirror_remove_all_mirrors: False
    aptly_mirror_do_updates: False
    aptly_mirrors: []

## How manage ...

### mirrors

You can manage aptly mirrors with this role with the following settings.

> Note: Only create, update and drop actions are managed !

If you want remove all existing mirrors, set "aptly_mirror_remove_all_mirrors"
to True.

If you want launching mirrors updates during the playbook execution, set
"aptly_mirror_do_updates" to True.

You can define mirrors using "aptly_mirrors" list.
Mirror definition example:

    - name: 'my_mirror'
      archive_url: 'http://foo.bar/foobar'
      distribution: 'trusty'
      do_update: True
      component1:
        - 'main'
      create_flags:
        - 'filter="nginx"'
        - 'keyring="foo.bar.gpg"'
      update_flags:
        - 'keyring="foo.bar.gpg"'
      gpg:
        key: 'fdsfqdsfqsfd'
        server: 'server-keys.org'
        keyring: 'foo.bar.gpg'
      state: 'present'

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: infOpen.aptly }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro

