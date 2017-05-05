import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


# import pytest
# @pytest.fixture  # (scope="module")
# def AnsibleDefaults(Ansible):
#     return Ansible("include_vars", "./defaults/main.yml")["ansible_facts"]
#
#
# @pytest.fixture  # (scope="module")
# def AnsibleVars(Ansible):
#     return Ansible("include_vars", "./vars/main.yml")["ansible_facts"]
#
#
# def test_ansible(AnsibleVars):
#     print AnsibleVars
#     assert False

def test_apt_packages_are_installed(Package):
    packages = [
        ("snapserver", "0.11.1"),
        ("snapclient", "0.11.1"),
        ]

    for package_name, package_version in packages:
        package = Package(package_name)
        assert package.is_installed
        assert package.version == package_version
