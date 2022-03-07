# The following commands will create a virtual interface (e.g. a virtual NIC) called virtual0 that is connected to the same physical network as eth0.
sudo ip link add link eth0 address 00:11:11:11:11:11 virtual0 type macvlan
sudo ifconfig virtual0 up
sudo ifconfig eth0 promisc
