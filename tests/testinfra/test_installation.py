"""
Role tests
"""
import pytest

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_aptly_user(User):
    """
    Tests Aptly user
    """

    user = User('aptly')

    assert user.exists
    assert user.group == 'aptly'
    assert user.home == '/var/lib/aptly'
    assert user.shell == '/bin/bash'


def test_aptly_user_home(File):
    """
    Tests Aptly user home properties
    """

    home_dir = File('/var/lib/aptly')

    assert home_dir.exists
    assert home_dir.is_directory
    assert home_dir.mode == 0o700
    assert home_dir.user == 'aptly'
    assert home_dir.group == 'aptly'


def test_aptly_configuration_file(File):
    """
    Tests Aptly configuration
    """

    config_file = File('/var/lib/aptly/.aptly.conf')

    assert config_file.exists
    assert config_file.is_file
    assert config_file.mode == 0o700
    assert config_file.user == 'aptly'
    assert config_file.group == 'aptly'


def test_repository_file(SystemInfo, File):
    """
    Test community repository file permissions
    """

    repo_file_name = ''

    if SystemInfo.distribution in ['debian', 'ubuntu']:
        repo_file_name = '/etc/apt/sources.list.d/repo_aptly_info.list'

    repo_file = File(repo_file_name)

    assert repo_file.exists
    assert repo_file.is_file
    assert repo_file.user == 'root'
    assert repo_file.group == 'root'
    assert repo_file.mode == 0o644


def test_debian_family_repository_file_content(SystemInfo, File):
    """
    Test repository file content on Debian family
    """

    if SystemInfo.distribution not in ['debian', 'ubuntu']:
        pytest.skip('Not apply to %s' % SystemInfo.distribution)

    repo_file = File('/etc/apt/sources.list.d/repo_aptly_info.list')

    assert repo_file.contains('deb http://repo.aptly.info/ squeeze main')


def test_packages(Package):
    """
    Test Aptly packages are installed
    """

    package = Package('aptly')

    assert package.is_installed
    assert '0.9.7' in package.version


def test_aptly_mirror_management(Command):
    """
    Test if mirrors managed in test playbook are ok
    """

    command = Command('sudo -H -u aptly aptly mirror list -raw')

    assert 'mariadb_10.0' in command.stdout


def test_aptly_repo_management(Command):
    """
    Test if repos managed in test playbook are ok
    """

    command = Command('sudo -H -u aptly aptly repo list -raw')

    assert 'testing' in command.stdout
