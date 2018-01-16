#!/usr/bin/env python

import fire
import scapy.all as scapy
from scapy.layers import http

def printer(pkt):
    if http.HTTPRequest in pkt:
        return pkt.sprintf("{IP:%IP.src% -> %IP.dst%\n}{HTTPRequest:%HTTPRequest.Path%\n}")
    elif http.HTTPResponse in pkt:
        #pkt.show()
        return pkt.sprintf("{IP:%IP.src% -> %IP.dst%\n}{HTTPResponse:%HTTPResponse.Status-Line%\n}{RAW:%RAW.load%\n}")
    else:
        return None

def sniff(filter):
    scapy.sniff(filter=filter,prn=printer)

if __name__ == '__main__':
    fire.Fire(sniff)
