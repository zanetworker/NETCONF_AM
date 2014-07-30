import amsoil.core.pluginmanager as pm

from amsoil.config import (netconfrpc_server_ip, netconfrpc_server_port)
from SocketServer import ThreadingMixIn
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


handler_object = pm.getService('netconfrpc')

class JSON_RPC_SERVER (ThreadingMixIn, SimpleJSONRPCServer):
    pass

def list_interfaces():
    return handler_object.list_interfaces()

def set_interface(type, interface_value):
    return handler_object.set_interface(type, interface_value)

def runServer():

    print "Waiting For NETCONF Requests...!!"
    server = JSON_RPC_SERVER((netconfrpc_server_ip, int(netconfrpc_server_port)))
    server.register_function(list_interfaces)
    server.register_function(set_interface)
    server.serve_forever()

