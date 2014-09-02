"""
This file contains the bare minimum for bootstrapping AMsoil.
All (non core) implementations/plugins should use the config service/plugin.
"""

import logging
import os.path
import json

from amsoil.core.exception import *

import amsoil

##Paths
SRC_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
ROOT_PATH = os.path.normpath(os.path.join(SRC_PATH, '..'))
PLUGINS_PATH = os.path.join(SRC_PATH, 'plugins')

##Logging
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"
LOG_FILE = "%s/log/amsoil.log" % (ROOT_PATH,)

##CONFIGDB
CONFIGDB_PATH = "%s/deploy/config.db" % (ROOT_PATH,)
CONFIGDB_ENGINE = "sqlite:///%s" % (CONFIGDB_PATH,)
IS_MULTIPROCESS = True

##IPC related parameters
#IPC_RABBITMQ_SERVER="localhost"
# IPC_RABBITMQ_SERVER="192.168.0.218"
##IPC: uncomment to use user/password
#IPC_RABBITMQ_USERNAME="user"
#IPC_RABBITMQ_PASSWORD="pass"


def expand_amsoil_path(path):
    """If the given path is relative, the path will be made absolute, starting from AMsoil's root."""
    path = os.path.expanduser(path)
    if os.path.isabs(path):
        return path
    else:
        return os.path.normpath(os.path.join(ROOT_PATH, path))


CONFIG_PATH = expand_amsoil_path('deploy/config.json')

try:
    CONFIG = json.load(open(CONFIG_PATH))
except Exception:
    raise MissingFileOrData(CONFIG_PATH)

# NETCONF RPC Server configuration parameters
default_reg_ip, default_reg_port= 'localhost', '1234'
netconfrpc_server_ip = CONFIG['NETCONF_RPC_SERVER']['server'] or default_reg_ip
netconfrpc_server_port = CONFIG['NETCONF_RPC_SERVER']['port'] or default_reg_port

# NETCONF Server configuration parameters
netconf_server_password = CONFIG['NETCONF_SERVER']['password'] or None
netconf_server_namespace  = CONFIG['NETCONF_SERVER']['yang_namespace'] or None
root_namespace = CONFIG['NETCONF_SERVER']['root_namespace'] or None
netconf_server_port = CONFIG['NETCONF_SERVER']['port']
netconf_server_ip = CONFIG['NETCONF_SERVER']['server']



