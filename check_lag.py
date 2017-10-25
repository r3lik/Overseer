#!/usr/bin/env python
""" Python version of check_lag nrpe check. """

import os
import sys
import json
from subprocess import Popen,PIPE,STDOUT
from collections import namedtuple


def shell_exec(command):
    """ subprocess wrapper function, returns named 
    tuple namespace with stdout, stderr, and shell 
    exit code  """
    cmd = command.split(' ')
    shexec = Popen( cmd, stderr=STDOUT, stdout=PIPE )
    shout = shexec.communicate(), shexec.returncode
    stdout,stderr,returncode = shout[0][0],shout[0][1],shout[1]

    resp = namedtuple("resp", ["stdout","stderr","returncode"])
    return resp(stdout,stderr,returncode)

'''
#!/bin/bash
# r3lik 11/11/16
#check TRANSIT LAG member port speed, and thereby, the number of members. 

#SNMP community (don't use public)
COMMUNITY="xxxxxxxx"

#gets IP from $HOSTADDRESS$ Nagios macro
UNICAST_IP=$1

#specifies aggregate ethernet port
AE=$2

#port speed in Megabits
SPEED=$3

CMD=($(snmpwalk -v 2c -c $COMMUNITY $UNICAST_IP ifName | grep -i "$AE" | grep -v "$AE." | cut -d. -f2 | awk '{print $1}'))

 if [ -z $CMD ]; then
        CMD="empty"
        echo "index" $CMD
        echo "$AE DOES NOT EXIST"
        exit 1
 fi

 for i in "${CMD[@]}"
 do
   TRANSIT=`snmpwalk -v 2c -c $COMMUNITY $UNICAST_IP ifAlias.$i | awk '{print $6}'`
   LAGSPEED=`snmpwalk -v 2c -c $COMMUNITY $UNICAST_IP ifHighSpeed.$i | awk '{print $4}'`
   if [ $LAGSPEED -eq $SPEED ]; then
     echo "$TRANSIT PORT $AE LAG SPEED OK: $LAGSPEED"
    exit 0
   elif [ $LAGSPEED -eq 0 ]; then
     echo "$TRANSIT PORT $AE NOT CONNECTED: ifHighSpeed is $LAGSPEED"
    exit 1
   fi
 done

echo "$TRANSIT PORT $AE LAG SPEED INCORRECT: $LAGSPEED expecting $SPEED"
exit 2
'''
