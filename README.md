aptly
=====

[![Build Status](https://travis-ci.org/infOpen/ansible-role-aptly.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-aptly)

Install aptly package.

Requirements
------------

This role requires Ansible 1.5 or higher, and platform requirements are listed
in the metadata file.

User should have a custom GPG key, not automatic creation

Testing
-------

This role has two test methods :

- localy with Vagrant :
    vagrant up

- automaticaly by Travis

To not have a fake gpg key used only for tests, i've add tags for tasks about
gpg.
These tasks are skipped for Travis tests, but can be tested by Vagrant with
proper environment variables :
- APTLY_CUSTOM_GPG_KEY_FILE
- APTLY_CUSTOM_GPG_KEY_ID

Vagrant should be used to check the role before push changes to Github.

Role Variables
--------------

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

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: achaussier.aptly }

License
-------

MIT

Author Information
------------------

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro } }}"

