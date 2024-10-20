import socket
from asyncio import timeout
from itertools import count

import icmplib

def discover(host_ip: str) -> list[str]:
    network_range = ".".join(host_ip.split(".")[:-1])
    online = []
    for i in range(256):
        turn = network_range + "." + str(i)

        if icmplib.ping(turn):
            online.append(turn, count=1, timeout=0.5)
    return online


def localhost() -> str:
    address = socket.gethostbyname(socket.gethostname())
    return address
