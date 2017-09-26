#!/bin/bash
#script to check kernel versions on linux boxes -mc 7/16/14

kernel=( 3.13.10 4.1.8 )
kernel_check=`uname -r`

for kernelversion in "${kernel[@]}"; do
    if [ $kernel_check = $kernelversion ]; then
        echo "OK - Kernel version correct ($kernelversion)"
        exit 0
    fi
done 

echo "WARNING - Kernel version NOT correct ($kernel_check)"
exit 1

