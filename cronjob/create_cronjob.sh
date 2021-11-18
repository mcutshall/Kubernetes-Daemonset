#!/bin/bash

sudo crontab -l > cron_cpy
sudo echo "0 * * * * /usr/bin/python /home/vagrant/app/check-deployment.py" >> cron_cpy
sudo crontab cron_cpy
sudo rm -f cron_cpy
