from amsoil.core import pluginmanager as pm
from netconfrpc import NETCONF_Handler

def setup():

    handler = NETCONF_Handler()
    print pm.registerService('netconfrpc', handler)
