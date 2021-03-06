"""
WEBDEP

A simple python web deployment used to quickly setup easy to modify
jinja2 and cherrypy based python servers.
"""

import os

# DIRECTORY GLOBALS
BASEDIR = os.path.dirname(os.path.realpath(__file__))

# PUBLIC GLOBALS
PUBDIR = os.path.join(BASEDIR, "public")
IMGDIR = os.path.join(PUBDIR, "images")
SCPDIR = os.path.join(PUBDIR, "scripts")
CONDIR = os.path.join(PUBDIR, "config")

# WEBPAGES GLOBALS
WEBDIR = os.path.join(BASEDIR, "webpages")

# LOGS GLOBALS
LOGDIR = os.path.join(BASEDIR, "logs")
BACKUP_COUNT = 60
