Ansible Role: SDKMAN init
=========================

[![Tests](https://github.com/gantsign/ansible_role_sdkman_init/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible_role_sdkman_init/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.sdkman__init-blue.svg)](https://galaxy.ansible.com/gantsign/sdkman_init)
[![License](https://img.shields.io/badge/license-Apache_2-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_sdkman_init/master/LICENSE)

Role to initialize [SDKMAN](https://sdkman.io/) the software development kit
manager. This role allows you to install particular SDKs as part of your Ansible
provisioning and set which versions should be use by default.

**Important:** this role requires SDKMAN to be already installed. You can use
our [gantsign.sdkman](https://galaxy.ansible.com/gantsign/sdkman) role to
install SDKMAN.

Requirements
------------

* Ansible >= 2.8

* Linux Distribution

    * Debian Family

        * Debian

            * Stretch (9)
            * Buster (10)
            * Bullseye (11)

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

    * RedHat Family

        * CentOS

            * 7

        * Fedora

            * 31

    * SUSE Family

        * openSUSE

            * 15.1

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role:

```yaml
# SDKMAN is initialized per user so you must specify at least one user
users:
  - username: # User to initialize SDKMAN for
    sdkman_install:
      - candidate: # Candidate SDK name e.g. java
        version: # Candidate version to install
        path: # Optional. To add an existing SDK install to SDKMAN.
              # The `version` for the existing SDK can't be the same any of
              # those provided by SDKMAN. The version string is just an
              # identifier so you can give it any value you like (as long as it
              # doesn't clash with any other versions for this candidate).
    sdkman_default:
      _candidate_sdk_name_here_: # Optional. Default version
```

Example Playbooks
-----------------

This is an example configuration for this role by itself (without the necessary
role for installing SDKMAN).

```yaml
- hosts: servers
  roles:
    - role: gantsign.sdkman_init
      users:
        - username: example_username
          sdkman_install:
            - candidate: java
              version: '8.0.181-zulu'
            - candidate: java
              version: '10'
              path: '/opt/java/jdk-10.0.2'
            - candidate: maven
              version: '3.5.4'
          sdkman_default:
            java: '10'
            maven: '3.5.4'
```

This is a complete example that uses the `gantsign.sdkman` role to install
SDKMAN. Notice how the `gantsign.sdkman_init` role can be used more than once
with Ansible tags to conditionally install particular SDKs.

```yaml
- hosts: servers
  roles:
    - role: gantsign.sdkman
      sdkman_users:
        - example_username

    - role: gantsign.sdkman_init
      tags:
        - java
      users:
        - username: example_username
          sdkman_install:
            - candidate: java
              version: '8.0.181-zulu'
            - candidate: java
              version: '10'
              path: '/opt/java/jdk-10.0.2'
          sdkman_default:
            java: '10'

    - role: gantsign.sdkman_init
      tags:
        - java
        - maven
      users:
        - username: example_username
          sdkman_install:
            - candidate: maven
              version: '3.5.4'
          sdkman_default:
            maven: '3.5.4'
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

Apache 2

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
