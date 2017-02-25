# aptly

[![Build Status](https://travis-ci.org/infOpen/ansible-role-aptly.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-aptly)

Install aptly package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial
and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

Follow the possible variables with their default values

```yaml
# Custom gpg key
aptly_custom_gpg_key_file : False
aptly_custom_gpg_key_id   : False

# System gpg keys archive import
aptly_system_archive_gpg_keys_import: True
aptly_system_archive_gpg_keys_keyring: 'system-trusted.gpg'

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
```

## How manage ...

### mirrors

You can manage aptly mirrors with this role with the following settings.

> Note: Only create, update and drop actions are managed !

If you want launching mirrors updates during the playbook execution, set
"aptly_mirror_do_updates" to True.

You can define mirrors using "aptly_mirrors" list.
Mirror definition example:

```yaml
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
```

### repos

You can manage aptly repos with this role with the following settings.

> Note: Only create and drop actions are managed !

You can define mirrors using "aptly_repos" list.
Repo definition example:

```yaml
- name: 'testing'
  create_flags:
    - '-comment="Testing repository"'
    - '-component="main"'
    - '-distribution="trusty"'
  state: 'present'
```

## Dependencies

None

## Example Playbook

```yaml
- hosts: servers
  roles:
     - role: infOpen.aptly
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
