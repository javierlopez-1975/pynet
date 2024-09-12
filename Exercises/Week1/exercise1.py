#!/usr/bin/env python

import os
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()
nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}

net_connect = ConnectHandler(**nxos1)
print(net_connect.find_prompt())
