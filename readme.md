Simple http-load-balancer

Prepare
Suggested test strategy:
Machine 1 (native PC) - Web browser
Machine 2 (VM #1) - Load balancer
Machine 3 (VM #2) - Web server #1

Configuration
Load Balancer
./set_LB.sh

Web Server
./set_server.sh [virtual-ip-address]
