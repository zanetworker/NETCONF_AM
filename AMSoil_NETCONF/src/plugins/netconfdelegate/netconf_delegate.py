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
        return self.list_parameter('interfaces')

    def list_properties(self):
        """
        Args:
            None

        Return:
            A list of capabilities supported by the underlying device using NETCONF's status message
        """
        return self.list_parameter('properties')

    def list_capabilities(self):
        """
        Translates the list_capabilities rpc call to a NETCONF message

        Args:
            None

        Return:
            A list of capabilities supported by the underlying device using NETCONF's status message
        """
        return self._rm.status()

    def set_parameter(self, parameter_type, parameter_value):
        """
        Change the value of an interface, it could be enable, disable ports or change port names

        Args:
             A named list of the values to change

        Return:
            A list of capabilities supported by the underlying device using NETCONF's status message
        """
        return self._rm.edit_config(parameter_type, parameter_value)


    def set_parameterst(self, parameters):
        return self._rm.edit_config_parameters(parameters)

    def list_parameter(self, parameter_to_list):
        """
        calls get-config with the right parameters

        Args:
            the type of parameter to show

        Return:
          the parameter to show
        """
        options = {'type': parameter_to_list}
        return self._rm.get_config(options)