# Smurf DDOS Tool
A python script for performing a smurf ddos attack. It uses scapy to generate the attack packets. \
Created for Final Year project at NYP.\
For educational purposes only.

## Usage
First install the packages and software needed to run the script by doing the following
(ensure you have [git](https://git-scm.com/downloads) and [python](https://www.python.org/downloads/) installed first):
```
Download and install Npcap
git clone https://github.com/secdev/scapy.git
cd scapy
python setup.py install
```
You can delete the scapy folder once you have installed scapy \
Instructions for script
```
python3 smurf_ddos.py
usage: smurf_ddos.py [-h] target broadcast interface

positional arguments:
  target      ipv4 address of target machine
  broadcast   broadcast address of target network
  interface   Interface to send the packets from

optional arguments:
  -h, --help  show this help message and exit

```

## Requirements
Latest development build of [scapy](https://github.com/secdev/scapy) \
The Latest version of [Npcap](https://nmap.org/npcap/) \
Python 3.4+