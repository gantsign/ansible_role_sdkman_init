import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('installed_version', [
    '+ tmp',
    '* 1.10.1',
    '* 1.10.0',
    '* 1.9.9',
])
def test_installed(host, installed_version):
    cmd = 'source ~/.sdkman/bin/sdkman-init.sh && sdk list ant'
    out = host.check_output("sudo --login --user=test_usr1 bash -c %s", cmd)
    assert installed_version in out


def test_default(host):
    cmd = 'source ~/.sdkman/bin/sdkman-init.sh && sdk current ant'
    out = host.check_output("sudo --login --user=test_usr1 bash -c %s", cmd)
    assert '1.10.0' in out
