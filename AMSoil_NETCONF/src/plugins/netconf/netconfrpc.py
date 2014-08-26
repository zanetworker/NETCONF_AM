import amsoil.core.pluginmanager as pm
from amsoil.core import serviceinterface

from amsoil.config import (netconfrpc_server_ip, netconfrpc_server_port)
from SocketServer import ThreadingMixIn
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

class NETCONF_Handler(object):
    def __init__(self):
        self._delegate = None

    @serviceinterface
    def setDelegate(self, adelegate):
        """
        Set this object's delegate.
        """
        self._delegate = adelegate

    @serviceinterface
    def getDelegate(self):
        """
        Get this object's delegate.
        """
        return self._delegate

    @serviceinterface
    def list_interfaces(self):
        """
         TODO: In case  filter is not working, fetch the whole config and view interfaces only
        """
        return self._delegate.list_interfaces()

    @serviceinterface
    def list_capabilities(self):
        return self._delegate.list_capabilities()


    def set_parameter(self, parameter_type, parameter_value):
        return self._delegate.set_parameter(parameter_type, parameter_value)
