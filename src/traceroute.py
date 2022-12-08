import sys

from scapy.sendrecv import (sr1)
from scapy.layers.inet import (IP, ICMP)

TIMEOUT_FOR_PACK = 5
MAX_HOPS = 16

HELP_TOOLTIP = """
   Correct usage: traceroute.py -m <int> target

   E.g:
   1. traceroute.py google.com
   2. traceroute.py -m 5 google.com
"""


def send_packet(target: str, ttl: int):
    packet = IP(dst=target, ttl=ttl) / ICMP()
    return sr1(packet, verbose=0, timeout=TIMEOUT_FOR_PACK)


def get_reply_from_target(target: str, hops_number: str = None):
    hops_number = int(hops_number) if hops_number else MAX_HOPS
    for i in range(hops_number):
        print(i + 1, end=' ')
        reply = send_packet(target, i)
        if reply is None:
            print("timeout")
            continue
        print(reply.src)
        if reply.type == 0:
            break


def run_traceroute(target: str, flag: str = None, value: str = None):
    get_reply_from_target(target, value)


def validate_args(args: list[str]):
    if len(args) == 2:
        (_, target) = args
        return target, None, None
    elif len(args) == 4:
        (_, flag, value, target) = args
        if flag == "-m" or flag == "--max-hops":
            return target, flag, value
    print(HELP_TOOLTIP)
    exit(0)


if __name__ == '__main__':
    run_traceroute(*validate_args(sys.argv))
