import sys
from optparse import OptionParser
""" Calculate de Address, Netmask, Network and Broadcast from a speficied IP """
usageStr = "Usage: %prog [options] IP-Block"
parser = OptionParser(usage= usageStr)
parser.add_option("-c", "--cidr", dest="cidr", metavar="CIDR", default=24, type="int", help="IP CIDR class.")
(opts, args) = parser.parse_args()
if len(args) < 1:
    parser.error("IP is required")
if len(args[0].split("/")) == 2:
    cidr = int(args[0].split("/")[1])
else:
    cidr = opts.cidr
ip = args[0].split("/")[0]
addr = ip.split(".")
mask = [0,0,0,0]
for i in range(cidr):
    mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
net = []
for i in range(4):
    net.append(int(addr[i]) & mask[i])
broad = list(net)
brange = 32 - cidr
for i in range(brange):
    broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))
print "Address: ", ip
print "Netmask: ", ".".join(map(str,mask))
print "Network ", ".".join(map(str,net))
print "Broadcast ", ".".join(map(str,broad))
