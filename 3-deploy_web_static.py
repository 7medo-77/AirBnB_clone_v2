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


env.hosts = ['54.82.134.192', '54.146.93.43']
do_pack = importlib.import_module('./1-pack_web_static.py').do_pack
do_deploy = importlib.import_module('2-do_deploy_web_static.py').do_deploy


def deploy(archive_path='none'):
    """
    Function to pack files in web_static into a compressed file
    """

    archive = do_pack()
    if (archive):
        return do_deploy(archive)
    else:
        return False
