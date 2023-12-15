# Ansible module for ipmitool

This is a really simple module and it is done mainly for experimenting. It's main purpose is to provide an Ansible way to control IPMI via the `ipmitool` binary.

## Prerequisites

- `ipmitool` - the binary must be present in `$PATH`.

### Module args

- `raw_command` - Ipmitool command. Example: `lan print 1`, `sel clear` and etc.

### Running the module, examples

- Print the general information about the IPMI:

    ```bash
    ANSIBLE_LIBRARY=./library ansible -i localhost, all -m ipmitool -a 'raw_command="lan print 1"'
    ```

- Clear the SEL logs:

    ```bash
    ANSIBLE_LIBRARY=./library ansible -i localhost, all -m ipmitool -a 'raw_command="sel clear"'
    ```

### Return values

- `raw_command`: Command that is actually passed to the ipmitool program.
- `command_output`: Output of the IPMI command if any. If none, return generic message.
- `command_rc`: Return code of the command.
