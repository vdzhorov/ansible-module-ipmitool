#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Valentin Dzhorov
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

try:
    import subprocess
except ImportError:
    module = None
    

DOCUMENTATION = r'''
module: ipmitool

short_description: An Ansible module used for controlling ipmitool.

version_added: "0.1"

description: Use this module to manage local or remote devices via ipmitool.

options:
  name:
    description: Hostname or ip address of the BMC.
    required: false
    type: str
  port:
    description:
      - Remote RMCP port.
    required: false
    type: int
    default: 623
  user:
    description:
      - Username to use to connect to the BMC.
    required: false
  password:
    description:
      - Password to connect to the BMC.
    required: false
    default: null
  interface:
    description:
      - Send a command over a specific interface.
    required: false
    choices:
      - lan
      - lanplus
      - serial-terminal
    default: lan
  raw_command:
    description:
      - Ipmitool command. Example: "lan print 1", "sel clear"
    type: str
    required: true
'''

EXAMPLES = r'''
# Print the current configuration for the given channel.
ipmitool: raw_command='lan print 1'
'''

RETURN = r'''
raw_command:
    description: Command to pass to the ipmitool program.
    type: str
    sample: 'lan'
command_output:
    description: Output of the IPMI command if any. If none, return generic message.
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
      raw_command=dict(type='str', required=True),
    )
    
    result = dict(
      changed=False,
    )
  
    module = AnsibleModule(
      argument_spec=module_args,
      supports_check_mode=True
    )
    
    # Fail if module subprocess is absent.
    if module is None:
        module.fail_json(msg='The python subprocess module is required.')
    
    if module.check_mode:
      module.exit_json(**result)
    
    # Ipmitool module logic
    result['raw_command'] = module.params['raw_command']
    result['command_output'] = ''
    
    command = subprocess.Popen('ipmitool {}'.format(module.params["raw_command"]),
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  shell=True,
                                  universal_newlines=True)
    command_stdout, command_stderr = command.communicate()
    
    if command_stdout:
      if len(command_stdout) == 0:
        result['command_output'] = 'Command returned success.'
      else:
        result['command_output'] = command_stdout
    else:
      module.fail_json(msg=command_stderr, **result)
  
    module.exit_json(**result)
    
def main():
    run_module()


if __name__ == '__main__':
    main()
