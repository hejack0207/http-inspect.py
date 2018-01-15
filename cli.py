#!/usr/bin/env python
try:
    import scapy.all as scapy
except ImportError:
    import scapy

try:
    # This import works from the project directory
    import scapy_http.http
except ImportError:
    # If you installed this package via pip, you just need to execute this
    from scapy.layers import http

packets = scapy.sniff(filter='host 10.0.51.14',count=4)
for p in packets:
    print '=' * 78
    p.show()
