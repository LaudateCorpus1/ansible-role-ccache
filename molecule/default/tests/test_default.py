import os

import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_ccache_config(host):
    ccache_config_file = host.file("/home/molecule/.ccache/ccache.conf")

    assert ccache_config_file.is_file
    assert ccache_config_file.user == "molecule"
    assert "cache_dir = /tmp/caches/ccache" in ccache_config_file.content_string
    assert "compression = true" in ccache_config_file.content_string


def test_ccache_installed(host):
    ccache_bin_file = host.file("/usr/local/bin/ccache")

    assert ccache_bin_file.is_file
    assert ccache_bin_file.mode == 0o0755


@pytest.mark.parametrize("compiler", ["cc", "c++", "clang", "clang++"])
def test_ccache_symlinks(host, compiler):
    ccache_symlink_path = "/tmp/lib/ccache"
    ccache_symlink_dir = host.file(ccache_symlink_path)
    compiler_symlink = host.file(os.path.join(ccache_symlink_path, compiler))

    assert ccache_symlink_dir.is_directory
    assert compiler_symlink.is_symlink
