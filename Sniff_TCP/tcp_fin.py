# 4
# >python tcp_fin.py (math 0+1+57) (math (cat seq)+1+184)
# >python tcp_ack.py (math 0+1+1+57) (math (cat seq)+1+1+184)

from scrapy.all import *
import sys
from consts import _sport, host, port

_seq = int(sys.argv[1])
_ack = int(sys.argv[2])

# print _seq
print(_seq)
ACK = IP(dst=host)/TCP(sport=_sport, dport=port, flags="FA", ack=_ack, seq=_seq)
send(ACK)
