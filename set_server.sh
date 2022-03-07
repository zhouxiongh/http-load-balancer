# First, configure Linux to only respond to ARP requests for the primary network interface IP(s).
sudo sysctl -w net.ipv4.conf.lo.arp_ignore=1
sudo sysctl -w net.ipv4.conf.lo.arp_announce=2
sudo sysctl -w net.ipv4.conf.all.arp_ignore=1
sudo sysctl -w net.ipv4.conf.all.arp_announce=2

# Second, configure Linux to use the Virtual IP address as a virtual "loopback" address.
sudo ifconfig lo:1 $1 netmask 255.255.255.255 -arp up
