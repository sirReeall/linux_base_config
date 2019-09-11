linux_base_config
=========

Uses yum package manager to install the following roles:

  - lsof
  - git
  - telnet
  - ntp
  - iftop
  - unzip
  - vim
  - net-tools.x86_64


Example Playbook
----------------

  - hosts: servers
    roles:
        - { role: linux_base_config }

License
-------

MIT
