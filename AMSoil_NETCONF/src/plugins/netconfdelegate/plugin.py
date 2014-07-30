from amsoil.core import pluginmanager as pm
from netconf_delegate import NETCONF_Delegate

def setup():
    delegate = NETCONF_Delegate()
    netconf_handler = pm.getService('netconfrpc')
    netconf_handler.setDelegate(delegate)
