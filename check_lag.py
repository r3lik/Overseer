#!/usr/bin/env python
""" Python version of check_lag nrpe check. """

import os
import sys
import json
import argparse
from subprocess import Popen,PIPE,STDOUT
from collections import namedtuple

def parse_args():
    """ Parse CLI arguments -  """
    parser = argparse.ArgumentParser()

    parser.add_argument(    "--community",
                            dest='community',
                            default='public',
                            help="SNMP community set as public by default")

    parser.add_argument(    "--unicast-ip",
                            dest='uni_ip',
                            help="Unicast IP address, can be specified by $HOSTADDRESS$ Nagios macro")

    parser.add_argument(    "--agg-port",
                            dest='aggregate_port',                    
                            help="Specifies aggregate ethernet port." )

    parser.add_argument(    "--port-speed",
                            default='port_speed',
                            help="Specifies port speed in mb/sec." )                          

    args = parser.parse_args()
    return args

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


if __name__ == "__main__":
    args = parse_args()
    print args
