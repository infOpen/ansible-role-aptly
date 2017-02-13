# Check vagrant prerequites is OK
check-vagrant-prerequisites:
ifeq (, $(shell which vagrant))
	$(error "No vagrant in $(PATH), consider install vagrant package")
endif


# Clean all
clean: clean-test clean-pyc


# Clean test environments
clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr reports/


# Clean python files
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


# Execute Vagrant tests
test-vagrant: check-vagrant-prerequisites
test-vagrant:
	vagrant up
	vagrant provision
	vagrant ssh-config > .vagrant/ssh-config
	testinfra --hosts=aptly-jessie --ssh-config=.vagrant/ssh-config --noconftest --sudo
	testinfra --hosts=aptly-trusty --ssh-config=.vagrant/ssh-config --noconftest --sudo
	testinfra --hosts=aptly-xenial --ssh-config=.vagrant/ssh-config --noconftest --sudo
