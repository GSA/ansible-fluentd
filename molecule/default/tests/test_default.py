import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_fluentd_is_installed(host):
    package = host.package("td-agent")
    assert package.is_installed
    assert package.version.startswith("3")


def test_fluentd_config_file_present(host):
    config_file = host.file('/etc/td-agent/td-agent.conf')
    assert config_file.is_file
