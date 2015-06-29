#!/usr/bin/python

# address-book-tool.py
# June 2015 - ben.dale@gmail.com
# Converts ScreenOS address-book entries to Junos SRX global entries

import sys
import shlex

def mask2cidr(mask):
    if mask=="255.255.255.255":
        return '/32'
    elif mask=='255.255.255.254':
        return '/31'
    elif mask=='255.255.255.252':
        return '/30'
    elif mask=='255.255.255.248':
        return '/29'
    elif mask=='255.255.255.240':
        return '/28'
    elif mask=='255.255.255.224':
        return '/27'
    elif mask=='255.255.255.192':
        return '/26'
    elif mask=='255.255.255.128':
        return '/25'
    elif mask=='255.255.255.0':
        return '/24'
    elif mask=='255.255.254.0':
        return '/23'
    elif mask=='255.255.252.0':
        return '/22'
    elif mask=='255.255.248.0':
        return '/21'
    elif mask=='255.255.240.0':
        return '/20'
    elif mask=='255.255.224.0':
        return '/19'
    elif mask=='255.255.192.0':
        return '/18'
    elif mask=='255.255.128.0':
        return '/17'
    elif mask=='255.255.0.0':
        return '/16'
    elif mask=='255.254.0.0':
        return '/15'
    elif mask=='255.252.0.0':
        return '/14'
    elif mask=='255.248.0.0':
        return '/13'
    elif mask=='255.240.0.0':
        return '/12'
    elif mask=='255.224.0.0':
        return '/11'
    elif mask=='255.192.0.0':
        return '/10'
    elif mask=='255.128.0.0':
        return '/9'
    elif mask=='255.0.0.0':
        return '/8'
    else:
        return '**ERROR**'


def main(argv):
    sys.stdout.write("address-book-tool\n\n")
    if len(sys.argv) != 2:
        sys.stdout.write("Error: Missing parameter\n")
        sys.stdout.write("Usage: address-book-tool.py <ssg-config.cfg>\n")
        sys.exit()
    configfile = open(str(sys.argv[1]),'r')
    for configline in configfile:
        linetokens = shlex.split(configline)
        if (linetokens[0]=='set' and linetokens[1]=='address'):
            addressObjectName=linetokens[3].strip('""').replace('.','_').replace(' ','_')
            addressObjectMask=mask2cidr(linetokens[5])
            addressObjectIP=linetokens[4]
            print "set security address-book global address " + addressObjectName + " " + addressObjectIP + addressObjectMask
    configfile.close()
# set address "Trust" "Host 10.100.1.129/32" 10.100.1.129 255.255.255.255


if __name__ == "__main__":
   main(sys.argv[1:])
