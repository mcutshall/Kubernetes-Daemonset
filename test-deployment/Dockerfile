FROM ubuntu:18.04

RUN apt-get update

ADD loop.sh /tmp/loop.sh
RUN chmod 777 /tmp/loop.sh

CMD ["/tmp/loop.sh"]
