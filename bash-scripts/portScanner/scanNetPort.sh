#!/bin/bash
if [ "$1" == "" ]
then
echo "You must insert an ip address!"
echo "Syntax: scanNetIps 192.168.238 80"
exit
fi

if [ "$2" == "" ]
then
echo "You must insert a port to scan!"
echo "Syntax: scanNetIps 192.168.238 80"
exit
fi

./ipsweep.sh $1 > tempIpList.txt

for ip in $(cat ./tempIpList.txt); do
nmap -sS -T4 -p $2 $ip &\
done

rm ./tempIpList.txt
