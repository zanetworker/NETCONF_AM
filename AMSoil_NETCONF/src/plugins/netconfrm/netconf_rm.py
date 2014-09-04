from ncclient import manager
from amsoil.config import netconf_server_password,\
    netconf_server_ip,\
    netconf_server_port, \
    netconf_server_namespace, \
    root_namespace, \
    netconf_server_username

from netconf_rm_utils import *

import xml.etree.ElementTree as ET

class NETCONFResourceManager(object):

    def __init__(self):
        pass

    def get_config(self, filter=None):
        """
        Retrieve device configuration

        Args:
            filter: If only part of the configuration is required and not the whole configuration

        Return:
            A list of capabilities supported by the underlying device
        """
        try:
            with manager.connect(host=netconf_server_ip,
                                 port=int(netconf_server_port),
                                 username= netconf_server_username,
                                 password=netconf_server_password,
                                 hostkey_verify=False) as m:

                if filter:
                    parsed_xml = parseXML(m.get_config(source='running').data_xml, filter['type'])
                    return parsed_xml if parsed_xml is not None else "There is not such element in the tree"
                else:
                    return m.get_config(source='running').data_xml
        except Exception as e:
            print e

    def status(self):
        """
        To understand what capabilities are supported

        Args:
            None

        Return:
            A list of capabilities supported by the underlying device
        """
        capabilities = []
        with manager.connect(host=netconf_server_ip,
                             port=int(netconf_server_port),
                             username= netconf_server_username,
                             password=netconf_server_password,
                             hostkey_verify=False) as m:

            for c in m.server_capabilities:
                capabilities.append(c)
            return capabilities

    def edit_config(self, parameter_type, parameter_value):
        """
        NETCONF edit config, used for relaying configuration changes to the underlying devies
        Args:
            configuration_options: A dictionary that contains important parameters such as:
                * type: defines whether the modification should be done to an interface, port, switch, etc.
                * value: determines the value for which the parameter type should be set to. The value of a parameter contains the
                  property name to be changed, and the value of the property. For example, it could look like this ['interface', 'eth0'].
                  In this case we want to change the interface name to eth0
        Return:
            True if the configuration was successful, and False if the configuration failed
        """

        assert isinstance(parameter_value, list), "Parameter Value needs to be a list"

        def change_interface_name():

            parameter_dictionary = {'a': 'config',
                                    parameter_type: [netconf_server_namespace, {parameter_value[0]:parameter_value[1]}]}
            xml, tags = dictToXML(parameter_dictionary, [root_namespace, netconf_server_namespace])
            config_data = wrap_tags(xml, tags)

            with manager.connect(host=netconf_server_ip,
                                 port=int(netconf_server_port),
                                 username=netconf_server_username,
                                 password=netconf_server_password) as m:

                assert(":validate" in m.server_capabilities)
                m.edit_config(target='running', config=config_data)
                return m.get_config(source='running').data_xml

        def set_experimenter():

            parameter_dictionary = {'a': 'config',
                                    parameter_type: [netconf_server_namespace, {parameter_type[0]: parameter_value[1]}]}
            xml, tags = dictToXML(parameter_dictionary, [root_namespace, netconf_server_namespace])
            config_data = wrap_tags(xml, tags)

            with manager.connect(host=netconf_server_ip,
                port=int(netconf_server_port),
                username= netconf_server_username,
                password=netconf_server_password) as m:

                assert(":validate" in m.server_capabilities)
                m.edit_config(target='running', config=config_data)
                return m.get_config(source='running').data_xml


        functions = {'change': change_interface_name,
                     'experimenter': set_experimenter}

        if parameter_type in ['interface', 'interfaces']:
            return functions['change']()

        if parameter_type in ['experimenter', 'experiment']:
            return functions['experimenter']()





