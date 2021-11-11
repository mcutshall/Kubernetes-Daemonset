#!/bin/bash

sudo crontab -l > cron_cpy
sudo echo "* * * * * /usr/bin/python /home/vagrant/app/deployment.py" >> cron_cpy
sudo crontab cron_cpy
sudo rm -f cron_cpy
