#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
import os
from fabric.api import run, put, execute, env

# Set the hosts and user for Fabric
env.hosts = ['52.91.126.247', '35.153.19.245']
env.user = 'ubuntu'


def do_deploy(archive_path):
    # Check if the archive_path exists
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, "/tmp/")

        # splitting the path into a list
        path_list = archive_path.split("/")

        # picking the file name from the path
        file_name = path_list[-1]

        # Split the file name into a list of file name and extension
        file_list = file_name.split('.')

        # Get the file name without the extension
        file_no_ext = file_list[1]

        # Set the remote directory path
        rem_dir_path = "/data/web_static/releases/{}/".format(file_no_ext)

        # Set the symbolic link path
        sym_link = "/data/web_static/current"

        run('mkdir - p {}'.format(rem_dir_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, rem_dir_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}'.format(rem_dir_path, rem_dir_path))
        run('rm -rf {}/web_static'.format(rem_dir_path))
        run('rm -rf {}'.format(sym_link))
        run('ln -s {} {}'.format(rem_dir_path, sym_link))
        return True
    except Exception:
        return False
