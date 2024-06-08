#!/usr/bin/python3
"""
Python script which packs all files in
/data/web_static into a compressed file
"""
from fabric.api import (run, cd,
                        env, put,
                        local
                        )
import importlib
from os import path
from datetime import datetime


env.hosts = ['54.82.134.192', '54.146.93.43']

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


def do_deploy(archive_path='none'):
    """
    Function to pack files in web_static into a compressed file
    """

    try:
        if not (path.exists(archive_path)):
            return False

        with cd("/tmp"):
            put("{}".format(archive_path), "/tmp/")

            output_object = run("echo $(ls -t /tmp | awk 'NR==1')")
            archive_name = output_object.stdout
            raw_name = run("echo \"{}\" | cut -d '.' -f 1"
                           .format(archive_name)).stdout

            run("sudo mkdir -p /data/web_static/releases/{}".format(raw_name))
            run("sudo tar -xvf /tmp/{} -C /data/web_static/releases/{}"
                .format(archive_name, raw_name))
            run("sudo rm -f {}".format(archive_name))
            run("sudo rm -f /data/web_static/current")
            run("sudo ln -s -f /data/web_static/releases/{}/web_static/\
                 /data/web_static/current".format(raw_name))
            return (True)
    except Exception:
        return False


def deploy(archive_path='none'):
    """
    Function to pack files in web_static into a compressed file
    """

    archive = do_pack()
    if (archive):
        return do_deploy(archive)
    else:
        return False
