#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

scapy.sniff(filter='host 10.0.51.14',prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
