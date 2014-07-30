from amsoil.core import pluginmanager as pm
from netconf_rm import NETCONFResourceManager

def setup():
    resource_manger = NETCONFResourceManager()
    pm.registerService('netconfrm', resource_manger)
