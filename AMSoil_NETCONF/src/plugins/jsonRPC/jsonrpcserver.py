import amsoil.core.pluginmanager as pm

from amsoil.config import (netconfrpc_server_ip, netconfrpc_server_port)
from SocketServer import ThreadingMixIn
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


handler_object = pm.getService('netconfrpc')

class JSON_RPC_SERVER (ThreadingMixIn, SimpleJSONRPCServer):
    pass

def set_parameter(parameter_type, parameter_value):
    return handler_object.set_parameter(parameter_type, parameter_value)

def list_interfaces():
    return handler_object.list_interfaces()

def list_capabilities():
    return handler_object.list_capabilties()

def list_properties():
    return handler_object.list_properties()


def runServer():
    print "Waiting For NETCONF Requests...!!"
    server = JSON_RPC_SERVER((netconfrpc_server_ip, int(netconfrpc_server_port)))
    server.register_function(list_interfaces)
    server.register_function(set_parameter)
    server.register_function(list_capabilities)
    server.register_function(list_properties)
    server.serve_forever()

