# Overseer
### A collection of monitoring scripts for [Nagios](https://www.nagios.org/)

1. Lag speed check
   - confirms that your ports are running at correct speed
   - runs on the Nagios server using `SNMP` 
2. Kernel version check
   - confirms that you are running the kernel that you expect
   - runs on the host target using `NRPE`
3. Anycast IP check
   - confirms that your IPs are being announced from multiple locations

## Lag speed check
Add the following to your Nagios `commands.cfg` file:

```
define command{
        command_name    check_lag
        command_line    $USER1$/check_lag $HOSTADDRESS$ $ARG1$ $ARG2$
}
```
Example `services.cfg` config:
```
define service {
    use                      network-service
    host_name                rtr01.ams1
    service_description      LAG: TRANSIT: AS3356 Level3
    check_command            check_lag! ae61 20000
}
define service {
    use                      network-service
    host_name                rtr01.fra1
    service_description      LAG: TRANSIT: AS2914 NTT
    check_command            check_lag! ae62 10000
}
```
Voilà :]

![Nagios lag_check](https://user-images.githubusercontent.com/3232601/30882288-59d8f1d8-a2bd-11e7-9c5f-a89439f290fe.JPG)

## Kernel version check
Specify the correct kernel variable. 
Add the following to your Nagios `commands.cfg` file:

```
define command{
	command_name	check_kernel
	command_line	$USER1$/check_nrpe -H $HOSTADDRESS$ -c check_kernel
	}
```

Add the script to NRPE on the host server(s)
