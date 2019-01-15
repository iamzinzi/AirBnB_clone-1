#!/usr/bin/python3
from fabric.api import local, put, run, env
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder
    of AirBnB clone.
    All archives must be stored in the folder versions
    (folder will be created if it doesn’t exist).
    Return: Archive path if the archive has been successfully generated.
    Otherwise, it should return None
    """
    try:
        if not os.path.exists("./versions"):
            print("hi")
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_" + date + ".tgz"
        command = "tar -cvzf " + "./versions/" + file_name + " ./web_static"
        local(command)
        return "versions/" + file_name
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers.
    Returns True if all operations have been done correctly; else, False.
    """
    env.hosts = ['34.73.14.116', '34.73.100.50']
    try:
        put('versions/web_static_20190115005446.tgz',
            '/tmp/web_static_20190115005446.tgz')
        run('mkdir -p /data/web_static/releases/web_static_20190115005446')
        run('tar -xzf /tmp/web_static_20190115005446.tgz -C '
            '/data/web_static/releases/web_static_20190115005446')
        run('rm -rf /tmp/web_static_20190115005446.tgz')
        run('mv /data/web_static/releases/web_static_20190115005446/web_static'
            '/* /data/web_static/releases/web_static_20190115005446/')
        run('rm -rf /data/web_static/releases/web_static_20190115005446/'
            'web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/web_static_20190115005446/ '
            '/data/web_static/current')
        return True
    except:
        return None
