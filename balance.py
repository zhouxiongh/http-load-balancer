#!/usr/bin/env python3

# Simple http-load-balance demo # # Set script as executable via: chmod +x balance.py # Run via: ./balance.py <PORT> import socket import sys import argparse import netifaces

from getmac import get_mac_address

def main(args):
    print("Starting Balancer server")

    # Create TCP socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Error: could not create socket")
        print("Description: " + str(msg))
        sys.exit()

    # Bind to listening port
    try:
        host=''  # Bind to all interfaces
        s.bind((host, int(agrs.port)))
    except socket.error as msg:
        print("Error: unable to bind on port %d" % port)
        print("Description: " + str(msg))
        sys.exit()

    # Listen
    try:
        backlog=10  # Number of incoming connections that can wait
                    # to be accept()'ed before being turned away
        s.listen(backlog)
    except socket.error as msg:
        print("Error: unable to listen()")
        print("Description: " + str(msg))
        sys.exit()

    print("Listening socket bound to port %d" % port)

    # Accept an incoming request
    try:
        (client_s, client_addr) = s.accept()
        # If successful, we now have TWO sockets
        #  (1) The original listening socket, still active
        #  (2) The new socket connected to the client
    except socket.error as msg:
        print("Error: unable to accept()")
        print("Description: " + str(msg))
        sys.exit()

    print("Accepted incoming connection from client")
    print("Client IP, Port = %s" % str(client_addr))

    # Receive data
    try:
        buffer_size=4096
        raw_bytes = client_s.recv(buffer_size)
    except socket.error as msg:
        print("Error: unable to recv()")
        print("Description: " + str(msg))
        sys.exit()

    string_unicode = raw_bytes.decode('ascii')
    print("Received %d bytes from client" % len(raw_bytes))
    print("Message contents: %s" % string_unicode)

    # Close both sockets
    try:
        client_s.close()
        s.close()
    except socket.error as msg:
        print("Error: unable to close() socket")
        print("Description: " + str(msg))
        sys.exit()

    print("Sockets closed, now exiting")

def net_list():
    return list(enumerate(netifaces.interfaces(), start=1))

def print_config(args):
    print("Using Python 3 to run program")
    print("Running load balancer server")
    print("======= CONFIGURATION =======")
    print("Load Balancer interfaces: {}".format(net_list()))
    print("VIP interface: {}".format(args.intf))
    print("VIP IP: {}".format(args.ip))
    print("VIP Port: {}".format(args.port))
    print("VIP MAC Address: {}".format(get_mac_address(ip=args.ip)))
    print("Target IP list: {}".format(args.targets))
    mac_list = [get_mac_address(ip=ip) for ip in args.targets.split(',')]
    print("Target MAC list: {}".format(mac_list))
    print("=============================")

if __name__ == "__main__":
    if 'virtual0' not in net_list():
        print('virtual NIC (virtual0) is not available')
        # sys.exit(1)
    parser = argparse.ArgumentParser(description='HTTP Load Balancer for fun.')
    parser.add_argument('--version', help="show program's version number and exit")
    parser.add_argument('--intf', type=str, default='virtual0', help='VIP interface (e.g. eth0)')
    parser.add_argument('--port', type=int, default=80, help='VIP port number (e.g. 80)')
    parser.add_argument('--ip', help='VIP IP address (e.g. 192.168.0.100)')
    parser.add_argument('--targets', help='Comma separated list of HTTP servers for proxy to target (hostname or IP)')
    args = parser.parse_args()

    print_config(args)
    # sys.exit(main(args))
