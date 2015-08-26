# AutomateSSH
Automate SSH tasks

## Login with ssh key

`update.py`

```
#!/usr/bin/env python
#-*- coding: utf-8 -*-

from automate import AutomateSSH

def main():
	update = AutomateSSH()

	# Optional notification
	update.notify('Warning', 'Waiting connection')

	# Hosts you want to connect
	hosts = ['host1', 'host2']

	# List of commands to execute
	cmds = {
		hosts[0]: ['echo list of commands for host1', 'ls', 'uptime'],
		hosts[1]: ['echo list of commands for host2', 'date', 'hostname']
	}

	# Start tasks
	update.start(hosts, cmds)


if __name__ == "__main__":
	main()
```


## Login with user and password

`update.py`

```
#!/usr/bin/env python
#-*- coding: utf-8 -*-

from automate import AutomateSSH

def main():

	# Just pass user and password here
	update = AutomateSSH('username', 'password')

	# Optional notification
	update.notify('Warning', 'Waiting connection')

	# Hosts you want to connect
	hosts = ['host1', 'host2']

	# List of commands to execute
	cmds = {
		hosts[0]: ['echo list of commands for host1', 'ls', 'uptime'],
		hosts[1]: ['echo list of commands for host2', 'date', 'hostname']
	}

	# Start tasks
	update.start(hosts, cmds)


if __name__ == "__main__":
	main()
```

## Install

`$ cd path_folder`
`$ python setup.py install`

# Todos
- [x] Multiple users and password for different hosts