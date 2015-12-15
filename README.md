# docker

To start multi-node wordpress application:
docker-compose --x-networking --project-name=wp --x-network-driver=overlay up -d

To start multi-node counter application:
docker-compose --x-networking --project-name=counter --x-network-driver=overlay up -d
