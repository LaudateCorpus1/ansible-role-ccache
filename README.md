Ccache Role
===========

This role installs the [ccache][ccache] software on the given Ansible host and configures
it for a given user.


Supported Host OS Types
-----------------------

This role only supports Unix hosts, given that `ccache` only supports the same. On
debian-based systems and macOS, installation can be done with a package manager. However,
installation from sources is also possible and is recommended for all other platforms. To
do this, you should define `ccache_build_from_sources: true`.

See `defaults/main.yml` for further documentation of supported variables.


[ccache]: https://ccache.dev
