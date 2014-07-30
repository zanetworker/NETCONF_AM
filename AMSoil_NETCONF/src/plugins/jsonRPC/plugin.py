from amsoil.core import pluginmanager as pm

import jsonrpcserver

def setup():

    handler = jsonrpcserver
    pm.registerService('jsonrpc', handler)
