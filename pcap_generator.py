#! /usr/bin/env python3

# That is a beta version so proceed carefully, please.

from scapy.all import *
import sys

if len(sys.argv) == 1:
    print('Usage: python3 pcap_generator.py <number of packets> <filename> ')

n = int(sys.argv[1])
filename = sys.argv[2]

time = 0.00114108 * n  + 0.157758
minutes = time/60
print('Generating packets, it will take %s seconds, moreless (%s, minutes)' % (time, minutes))

pkgs = [IP(dst='10.0.0.1')/ICMP() for i in range (n)]
wrpcap(filename, pkgs)

print('%s packets generated.' % (n))   
