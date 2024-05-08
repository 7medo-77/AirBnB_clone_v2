#!/usr/bin/python3
"""Python script which packs all files in
/data/web_static into a compressed file"""
from fabric.api import run, cd, env, put
# from fabric.api import cd
# from fabric.api import env
# from fabric.api import put
# from datetime import datetime

env.hosts = ['54.82.134.192', '54.146.93.43']
# env.user = 'ubuntu'
# env.key_filename = '~/.ssh/school'

def do_deploy(archive_path='none'):
    """
    Function to pack files in web_static into a compressed file
    """
    try:
        with cd("/tmp"):
            put("{}".format(archive_path), "/tmp/")

            output_object = run("echo $(ls -t /tmp | awk 'NR==1')")
            archive_name = output_object.stdout
            raw_name = run("echo \"{}\" | cut -d '.' -f 1".format(archive_name)).stdout

            run("mkdir -p /data/web_static/releases")
            run("tar -xvf /tmp/{} -C /data/web_static/releases"\
                .format(archive_name))
            run("rm -f {}".format(archive_name))
            run("rm -f /data/web_static/current")
            run("ln -s -f /data/web_static/releases/{} /data/web_static/current".format(raw_name))
            return (True)
    except Exception:
        return False
