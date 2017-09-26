# Overseer
A collection of monitoring scripts for Nagios

1. Lag Speed check
--* confirms that your ports are running at correct speed
2. Kernel version check
3. Anycast IP check

```
define command{
	command_name	check_kernel
	command_line	$USER1$/check_nrpe -H $HOSTADDRESS$ -c check_kernel
	}
```
