#!/usr/bin/env python
import sys, os
import getopt

from amsoil import config
from amsoil.core import pluginmanager as pm

def print_usage():
    print "USAGE: ./main.py [--help] [--worker]"
    print
    print "When no option is specified, the server will be started."
    print
    print "  --help    Print this help message."
    print "  --worker  Starts the worker process instead of the RPC server."

def main():
    # set home environment variable to something (needed for apache deployment)
    os.environ['HOME'] = config.expand_amsoil_path('~')

    # load plugins
    pm.init(config.PLUGINS_PATH)
    rcp_server = pm.getService('jsonrpc')
    rcp_server.runServer()

if __name__ == "__main__":
    main()
