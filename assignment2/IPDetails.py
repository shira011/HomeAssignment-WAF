import ipcalc
from netaddr import IPNetwork
import socket
import struct


def ipDetails(IPAdress, subnetMask):
    """
    :param IPAdress: ip address
    :param subnetMask: subnet mask
    :return: nothing, the function print only  the number of hosts, number of endpoints, network address
    First endpoint IP, Last endpoint IP and Broadcast IP address.
    """
    # 1
    full_ip = IPAdress + '0' + '/' + subnetMask
    ip_split = IPAdress.split('.')
    ip_split.pop()
    ip_split.append('0')
    IPAdress += '0'
    num_of_hosts = pow(2, (32 - int(subnetMask))) - 2
    print("The numbers of available hosts in the subnet is: ", str(num_of_hosts))
    # 2
    ip_list = IPNetwork(full_ip)
    print("The number of endpoints: " + str(ip_list.size - 2))
    # 3
    addr = ipcalc.IP(IPAdress, mask=subnetMask)
    network_with_cidr = str(addr.guess_network())
    bare_network = network_with_cidr.split('/')[0]
    print("The network address: " + bare_network)
    # 4 + 5
    first, last = ip_list[1], ip_list[-2]
    print("The first endpoint: " + str(first))
    print("The last endpoint: " + str(last))
    # 6
    host_bits = 32 - int(subnetMask)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    subnetMask_split = netmask.split('.')
    broadcast = [(int(ioctet) | ~int(moctet)) & 0xff for ioctet, moctet in zip(ip_split, subnetMask_split)]
    print('Broadcast IP address:', '.'.join(map(str, broadcast)))


def main():
    ipDetails('192.168.0.', '24')
    # ipDetails('192.168.5.', '24')
    # ipDetails('192.168.0.', '28')
    # ipDetails('192.168.0.', '31')


main()
'''
 ipDetails('192.168.0.', '24'):
 The numbers of available hosts in the subnet is:  254
 The number of endpoints: 254
 The network address: 192.168.0.0
 The first endpoint: 192.168.0.1
 The last endpoint: 192.168.0.254
 Broadcast IP address: 192.168.0.255
'''
