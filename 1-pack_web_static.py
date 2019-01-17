#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """enerates a .tgz archive from the contents of the web_static folder
    of AirBnB clone.
    All archives must be stored in the folder versions
    (folder will be created if it doesn’t exist).
    Return: Archive path if the archive has been successfully generated.
    Otherwise, it should return None
    """
    try:
        if not os.path.exists("./versions"):
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_" + date + ".tgz"
        command = "tar -cvzf " + "./versions/" + file_name + " ./web_static"
        local(command)
        return "versions/" + file_name
    except:
        return None
