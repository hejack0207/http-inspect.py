#!/usr/bin/env python

import fire
import scapy.all as scapy
from scapy.layers import http

def printer(pkt):
    if http.HTTP in pkt:
        return pkt.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}")
    else:
        None

def sniff(filter):
    #scapy.sniff(filter=filter,prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
    scapy.sniff(filter=filter,prn=printer)

if __name__ == '__main__':
    fire.Fire(sniff)
