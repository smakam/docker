FROM ubuntu:14.04
MAINTAINER Sreenivas Makam <smxxxx@yahoo.com>

# Install apache2
RUN apt-get install -y apache2

EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl"]
CMD ["-D", "FOREGROUND"]
