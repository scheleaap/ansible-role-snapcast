import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_apt_packages_are_installed(Package):
    packages = [
        ("snapserver", "0.11.1"),
        ("snapclient", "0.11.1"),
        ]

    for package_name, package_version in packages:
        package = Package(package_name)
        assert package.is_installed
        assert package.version == package_version


def test_var_lib_snapclient_exists(File):
    f = File("/var/lib/snapclient")
    assert f.exists
    assert f.user == "snapclient"
    assert f.group == "audio"


def test_snapclient_configuration(File):
    f = File("/etc/default/snapclient")
    assert f.exists
    assert f.contains("^SNAPCLIENT_OPTS=\"--test yes\"$")
