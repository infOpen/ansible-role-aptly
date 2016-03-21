require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'aptly Ansible role' do

    # Declare variables
    packages = Array[]
    aptly_user = 'aptly'
    aptly_group = 'aptly'
    aptly_home = '/var/lib/aptly'
    aptly_shell = '/bin/false'

    if ['debian', 'ubuntu'].include?(os[:family])
        packages = Array[ 'aptly' ]
    end

    it 'install role packages' do
        packages.each do |pkg_name|
            expect(package(pkg_name)).to be_installed
        end
    end

    # Aptly user tests
    describe user(aptly_user) do
        it { should exist }
        it { should belong_to_group aptly_group }
        it { should have_home_directory aptly_home }
        it { should have_login_shell aptly_shell }
    end

    # Aptly home directory tests
    describe file(aptly_home) do
        it { should exist }
        it { should be_directory }
        it { should be_mode 700 }
        it { should be_owned_by aptly_user }
        it { should be_grouped_into aptly_group }
    end

    # Aptly configuration file tests
    describe file("#{aptly_home}/.aptly.conf") do
        it { should exist }
        it { should be_file }
        it { should be_mode 700 }
        it { should be_owned_by aptly_user }
        it { should be_grouped_into aptly_group }
    end
end

