# docker

**compose directory:**

To start single-node wordpress application:

docker-compose up -d

To start multi-node wordpress application:

docker-compose --x-networking --project-name=wp --x-network-driver=overlay up -d

To start multi-node counter application:

docker-compose --x-networking --project-name=counter --x-network-driver=overlay up -d

**apache directory:**

Dockerfile for apache application

**haproxy directory:**

haproxy configuration for load balancing between 3 nginx containers

**container_lifecycle directory:**

Files associated with this blog(https://sreeninet.wordpress.com/2017/08/15/docker-features-for-handling-containers-death-and-resurrection/)

**loadbalance directory:**

Compose files for illustrating different load balancers like internal, ingress, proxy and L7 load balancer
