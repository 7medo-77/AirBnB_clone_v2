#!/usr/bin/python3
"""Python script which packs all files in
/data/web_static into a compressed file"""
from fabric.api import run
from fabric.api import local
from fabric.api import lcd
from datetime import datetime


def do_pack():
    """
    Function to pack files in web_static into a compressed file
    """
    time_now = datetime.now()
    name_str = "web_static_{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".\
        format(time_now.year, time_now.month,
               time_now.day, time_now.hour,
               time_now.minute, time_now.second)

    try:
        local("mkdir -p ./versions/")
        res = local("tar -cvzf versions/{} web_static".format(name_str))
    except Exception:
        return None
    return (name_str)
