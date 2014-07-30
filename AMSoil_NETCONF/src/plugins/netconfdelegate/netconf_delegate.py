import amsoil.core.pluginmanager as pm
from amsoil.core import serviceinterface



class NETCONF_Delegate(object):
    def __init__(self):
        self._rm = pm.getService('netconfrm')


    def list_interfaces(self):
        """


        Args:
            None

        Return:
            A list of capabilities supported by the underlying device using NETCONF's status message
        """
        options = {'type': 'interface', }
        return self._rm.get_config()

    def list_capabilities(self):
        """
        Translates the list_capabilities rpc call to a NETCONF message

        Args:
            None

        Return:
            A list of capabilities supported by the underlying device using NETCONF's status message
        """
        return self._rm.status()

    def set_interface(self, **options):
        """
        Change the value of an interface, it could be enable, disable ports or change port names

        Args:
             A named list of the values to change

        Return:
            A list of capabilities supported by the underlying device using NETCONF's status message
        """
        options = {'type': 'interface', }
        return self._rm.edit_config_test(options)

