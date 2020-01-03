import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_installed_packages(host):
    lsof = host.package("lsof")
    assert lsof.is_installed

    git = host.package("git")
    assert git.is_installed

    telnet = host.package("telnet")
    assert telnet.is_installed

    ntp = host.package("ntp")
    assert ntp.is_installed

    iftop = host.package("iftop")
    assert iftop.is_installed

    unzip = host.package("unzip")
    assert unzip.is_installed

    net_tools = host.package("net-tools")
    assert net_tools.is_installed

    assert host.package("curl").is_installed
