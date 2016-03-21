require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'aptly Ansible role configuration' do

    # Declare variables
    aptly_user = 'aptly'
    aptly_mirror_name = 'mariadb_10.0'
    aptly_repo_name = 'testing'

    # Aptly mirror test
    describe command("sudo -H -u #{aptly_user} aptly mirror list -raw") do
        its(:stdout) { should match /mariadb_10.0/ }
    end

    # Aptly repo test
    describe command("sudo -H -u #{aptly_user} aptly repo list -raw") do
        its(:stdout) { should match /testing/ }
    end
end

