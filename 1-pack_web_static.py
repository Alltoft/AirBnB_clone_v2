#!/usr/bin/python3

from fabric.api import local
from datetime import datetime

def do_pack():
    dir = "version"
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(time_now)
    command = "tar -cvzf {}/{} web_static".format(dir, file_name)
    local("mkdir -p {}".format(dir))
    local(command)
    return "{}/{}".format(dir, file_name)
