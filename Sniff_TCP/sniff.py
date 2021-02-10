# D:\>pip install Twisted-20.3.0-cp39-cp39-win_amd64.whl
# >pip install scrapy
from scrapy.all import *

host = "host 85.143.216.55"
string = "IP.src% %TCP.sport% seq=%TCP.seq% ack=%TCP.ack% %TCP.flags%Raw.load%"
sniff(filter=host, prn=lambda x: x.sprintf(string))