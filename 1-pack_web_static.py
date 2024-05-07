#!/usr/bin/python3
"""Python script which packs all files in
/data/web_static into a compressed file"""
from fabric.api import run
from fabric.api import local
from fabric.api import lcd
from datetime import datetime
import time


def do_pack():
    # time_component = time.localtime(time.time())
    time_now = datetime.now()
    name_str = "web_static_{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".\
        format(time_now.year, time_now.month,
               time_now.day, time_now.hour,
               time_now.minute, time_now.second)
        # format(time_component.tm_year, time_component.tm_mon,
        #        time_component.tm_mday, time_component.tm_hour,
        #        time_component.tm_min, time_component.tm_sec)

    local("mkdir -p ./versions/")
    res = local("tar -cvzf versions/{} web_static".format(name_str))
    print(res.stdout)
