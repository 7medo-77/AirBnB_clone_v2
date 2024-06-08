#!/usr/bin/python3
"""
Python script which packs all files in
/data/web_static into a compressed file
"""
from fabric.api import (run, cd,
                        env, local
                        )


env.hosts = ['54.82.134.192', '54.146.93.43']


def do_clean(number=0):
    """
    Function to delete older versions of
    the archive in the versions directory
    and in the releases directory remotely
    """
    numberOfVersions = int(local("ls -t ./versions | wc -l").stdout)
    listRemoveFiles = local("ls -t ./versions | tail -{}"
                            .format(numberOfVersions - 1
                                    if number <= 1
                                    else numberOfVersions - number)).stdout
    local("rm -f {}".format(listRemoveFiles))

    with cd("/data/web_static/releases/"):
        numberOfReleases = int(run("ls -t /data/web_static/releases/\
                            | wc -l").stdout)
        listRemoveReleases = local("ls -t | tail -{}"
                                   .format(numberOfReleases - 1
                                           if number <= 1 else
                                           numberOfReleases - number)).stdout
        local("rm -rf {}".format(listRemoveReleases))
