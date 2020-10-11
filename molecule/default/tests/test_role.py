import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('installed_version', [
    '+ tmp',
    '* 0.51.0',
    '* 0.50.0',
    '* 0.49.0',
])
def test_installed(host, installed_version):
    cmd = 'source ~/.sdkman/bin/sdkman-init.sh && sdk list jbang'
    out = host.check_output("sudo --login --user=test_usr1 bash -c %s", cmd)
    assert installed_version in out


def test_default(host):
    cmd = 'source ~/.sdkman/bin/sdkman-init.sh && sdk current jbang'
    out = host.check_output("sudo --login --user=test_usr1 bash -c %s", cmd)
    assert '0.50.0' in out
