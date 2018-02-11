"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_aptly_user(host):
    """
    Tests Aptly user
    """

    user = host.user('aptly')

    assert user.exists
    assert user.group == 'aptly'
    assert user.home == '/var/lib/aptly'
    assert user.shell == '/bin/bash'


def test_aptly_user_home(host):
    """
    Tests Aptly user home properties
    """

    home_dir = host.file('/var/lib/aptly')

    assert home_dir.exists
    assert home_dir.is_directory
    assert home_dir.mode == 0o700
    assert home_dir.user == 'aptly'
    assert home_dir.group == 'aptly'


def test_aptly_configuration_file(host):
    """
    Tests Aptly configuration
    """

    config_file = host.file('/var/lib/aptly/.aptly.conf')

    assert config_file.exists
    assert config_file.is_file
    assert config_file.mode == 0o700
    assert config_file.user == 'aptly'
    assert config_file.group == 'aptly'


def test_repository_file(host):
    """
    Test community repository file permissions
    """

    repo_file_name = ''

    if host.system_info.distribution in ['debian', 'ubuntu']:
        repo_file_name = '/etc/apt/sources.list.d/repo_aptly_info.list'

    repo_file = host.file(repo_file_name)

    assert repo_file.exists
    assert repo_file.is_file
    assert repo_file.user == 'root'
    assert repo_file.group == 'root'
    assert repo_file.mode == 0o644


def test_debian_family_repository_file_content(host):
    """
    Test repository file content on Debian family
    """

    if host.system_info.distribution not in ['debian', 'ubuntu']:
        pytest.skip('Not apply to %s' % host.system_info.distribution)

    repo_file = host.file('/etc/apt/sources.list.d/repo_aptly_info.list')

    assert repo_file.contains('deb http://repo.aptly.info/ squeeze main')


def test_packages(host):
    """
    Test Aptly packages are installed
    """

    package = host.package('aptly')

    assert package.is_installed
    assert '1.2.0' in package.version


def test_aptly_mirror_management(host):
    """
    Test if mirrors managed in test playbook are ok
    """

    assert 'mariadb_10.0' in host.check_output(
        'sudo -H -u aptly aptly mirror list -raw')


def test_aptly_repo_management(host):
    """
    Test if repos managed in test playbook are ok
    """

    assert 'testing' in host.check_output(
        'sudo -H -u aptly aptly repo list -raw')
