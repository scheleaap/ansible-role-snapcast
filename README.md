# Ansible role for Mopidy

Installs and configures [Snapcast](https://github.com/badaix/snapcast)

## Requirements

<!-- Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required. -->


## Role Variables

<!-- A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well. -->

Variable | Description
--- | ---
`snapcast_install_server` | Install the Snapcast server? (boolean, default: yes)
`snapcast_install_client` | Install the Snapcast client? (boolean, default: yes)
`snapcast_version` | The version of Snapcast to install. See [the release page](https://github.com/badaix/snapcast/releases/latest) for all versions.
`snapcast_architecture` | The CPU architecture to install. Common values: `amd64`, `armhf` (e.g. Raspberry Pi). See [the release page](https://github.com/badaix/snapcast/releases/latest) for all architectures.


## Dependencies

None


## Example Playbook

See included `playbook.yml`.
