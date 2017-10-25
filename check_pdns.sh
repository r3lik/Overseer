#!/bin/bash

ERROR=`/usr/bin/pdnssec check-all-zones |grep -B1 'missing field at the end of record content'|head -n1`

if [ -z "$ERROR" ]; then
    echo "OK - No empty fields"
    exit 0
else
    echo "CRITICAL - Empty field in ${ERROR} !"
    exit 2
fi
