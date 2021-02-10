# 3
# >python tcp_pack.py (math 0+1) (math (cat seq)+1)
# подтвердить получение пакета
# >python tcp_ack.py (math 0+1+57) (math (cat seq)+1+184)
# подтверждаем что отправили 57 байт, а получили 184

from scrapy.all import *
import sys
from consts import _sport, host, port, d
from helpers import *

_seq = int(sys.argv[1])
_ack = int(sys.argv[2])

# print _seq
print(_seq)
SENDDATA = IP(dst=host)/TCP(sport=_sport, dport=port, flags="PA", ack=_ack, seq=_seq)
R = send(SENDDATA)
