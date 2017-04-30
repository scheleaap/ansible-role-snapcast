import ConfigParser as configparser
from StringIO import StringIO

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


# def test_test(Ansible):
#     print(Ansible.get_variables())


def test_mopidy_apt_repository_present(File):
    f = File("/etc/apt/sources.list.d/mopidy.list")
    assert f.exists
    content = f.content
    assert "http://apt.mopidy.com/" in content


def test_mopidy_apt_packages_are_installed(Package):
    packages = [
        ("mopidy", "2.1.0-1"),
        ("mopidy-scrobbler", "1.1.1-3"),
        ("mopidy-soundcloud", "2.0.2-2"),
        ("mopidy-spotify", "3.0.0-0mopidy1"),
        ("mopidy-spotify-tunigo", "1.0.0-0mopidy1"),
        ]

    for package_name, package_version in packages:
        package = Package(package_name)
        assert package.is_installed
        assert package.version == package_version


def test_mopidy_pip_packages_are_installed(PipPackage):
    packages = [
        ("Mopidy-Iris", "2.13.15"),
        ]

    installed_packages = PipPackage.get_packages()
    for package_name, package_version in packages:
        assert package_name in installed_packages
        package = installed_packages[package_name]
        assert package["version"] == package_version


def test_mopidy_configuration(File):
    f = File("/etc/mopidy/mopidy.conf")
    assert f.exists

    # TODO: See if we can access the mopidy_user variable here
    assert f.user == 'root'


def test_mopidy_mpd_configuration(File):
    parser = parse_config(File("/etc/mopidy/mopidy.conf"))
    assert parser.get("mpd", "hostname") == "::"
    assert parser.get("mpd", "port") == "6600"


def test_mopidy_http_configuration(File):
    parser = parse_config(File("/etc/mopidy/mopidy.conf"))
    assert parser.get("http", "enabled") == "true"
    assert parser.get("http", "port") == "6680"


def test_mopidy_file_configuration(File):
    parser = parse_config(File("/etc/mopidy/mopidy.conf"))
    assert parser.get("file", "enabled") == "false"


def test_mopidy_local_configuration(File):
    parser = parse_config(File("/etc/mopidy/mopidy.conf"))
    assert parser.get("file", "enabled") == "false"


def test_mopidy_scrobbler_configuration(File):
    parser = parse_config(File("/etc/mopidy/mopidy.conf"))
    assert parser.get("scrobbler", "enabled") == "true"
    assert parser.get("scrobbler", "username") is not None
    assert parser.get("scrobbler", "password") is not None


def test_mopidy_spotify_configuration(File):
    parser = parse_config(File("/etc/mopidy/mopidy.conf"))
    assert parser.get("spotify", "enabled") == "true"
    assert parser.get("spotify", "username") is not None
    assert parser.get("spotify", "password") is not None


# def test_service_running_and_enabled(Service):
#     service = Service("mopidy")
#     assert service.is_running
#     assert service.is_enabled


def parse_config(f):
    parser = configparser.SafeConfigParser()
    parser.readfp(StringIO(f.content))
    return parser
