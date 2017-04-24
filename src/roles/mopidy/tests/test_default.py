import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


# def test_mopidy_apt_repository_present(File):
#     f = File("/etc/apt/sources.list.d/mopidy.list")
#     assert f.exists
#     content = f.content
#     assert "http://apt.mopidy.com/" in content


def test_mopidy_is_installed(Package):
    package = Package("mopidy")
    assert package.is_installed


def test_mopidy_configuration(File):
    f = File("/etc/mopidy/mopidy.conf")
    assert f.exists
    assert f.user == 'mopidy'
    content = f.content
    assert "[spotify]" in content


# def test_nginx_running_and_enabled(Service):
#     nginx = Service("nginx")
#     assert nginx.is_running
#     assert nginx.is_enabled


def test_mopidy_spotify_is_installed(Package):
    package = Package("mopidy-spotify")
    assert package.is_installed
