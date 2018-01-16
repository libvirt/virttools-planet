#!/usr/bin/python

import os
import time

update = "./planet.py ./virt-tools/config.ini"

os.system("rsync -av virt-tools/images/ /opt/app-root/web/images/")

while True:
    ret = os.system(update)
    rv = ret >> 8
    if rv != 0:
        print "Update failed, retrying in 60 seconds"
        time.sleep(60)
    else:
        print "Update succeeded, refreshing in 30 minutes"
        time.sleep(30*60)
