# Ansible module for ipmitool

This is a really simple module and it is done mainly for experimenting. It's main purpose is to provide an Ansible way to control IPMI via the `ipmitool` binary.

## Prerequisites

- `ipmitool` - the binary must be present in `$PATH`.

### Module args

- `command` - Ipmitool command. Example: "lan", "sel", "raw", "session" and etc.
- `command_args` - Ipmitool command args. Example: "print 1" (used in conjuction with "lan print 1"), "clear" (used in conjuction with "sel clear").

### Running the module, examples

- Print the general information about the IPMI:

    ```bash
    ANSIBLE_LIBRARY=./library ansible -i 79.98.106.81, all -m ipmitool -a 'command=sel command_args="clear"'
    ```

- Clear the SEL logs:

    ```bash
    ANSIBLE_LIBRARY=./library ansible -i 79.98.106.81, all -m ipmitool -a 'command=sel command_args="clear"'
    ```
