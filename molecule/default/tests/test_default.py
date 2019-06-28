import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_easyrsa_bin(host):
    easyrsa = host.file("/usr/share/easy-rsa/3/easyrsa")
    assert easyrsa.exists == True

def test_easyrsa_pki_ca(host):
    easyrsa = host.file("/home/easyrsa/easyrsa/pki/ca.crt")
    assert easyrsa.exists == True
