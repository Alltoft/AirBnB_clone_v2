#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    a Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack
    """
    try:
        dir = "versions"
        time_now = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(time_now)
        command = "tar -cvzf {}/{} web_static".format(dir, file_name)
        local("mkdir -p {}".format(dir))
        local(command)
        return "{}/{}".format(dir, file_name)
    except:
        return None
