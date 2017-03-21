#! /usr/bin/env python3

# This is a beta version so proceed carefully, please.

from scapy.all import *
import sys

if len(sys.argv) == 1:
    print('Usage: python3 flooder_pcap.py <numbers of send> <filename> (Run it as root)')

n = int(sys.argv[1])
filename = sys.argv[2]

print('Reading pcap file.')
pkgs = rdpcap(filename)

for i in range (n):
    print('Sending %s packets.' % (len(pkgs)))
    sendpfast(pkgs)
    print('Done, part %s of %s' % ((i+1) , n))
