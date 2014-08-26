from ncclient import manager
from amsoil.config import netconf_server_password,\
    netconf_server_ip,\
    netconf_server_port, \
    netconf_server_namespace

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
                                 username='adel',
                                 password=netconf_server_password,
                                 hostkey_verify=False) as m:

                if filter:
                    filter_text = '<%s xmlns="%s"/>' % (filter['type'], netconf_server_namespace)
                    return m.get_config(source='running', filter=str(filter_text)).data_xml
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
                             username='adel',
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
                * value: determines the value for which the parameter type should be set to.
        Return:
            True if the configuration was successful, and False if the configuration failed
        """
        def change_interface_name():

            config_data = """<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                            <interfaces xmlns="%s">
                                <interface>%s</interface>
                            </interfaces>
                         </config>""" % (netconf_server_namespace, parameter_value)

            with manager.connect(host=netconf_server_ip,
                                 port=int(netconf_server_port),
                                 username='adel',
                                 password=netconf_server_password) as m:

                assert(":validate" in m.server_capabilities)
                m.edit_config(target='running', config=config_data)
                print m.get_config(source='running').data_xml

        def disable_interface():
            print None


        def enable_interface():
            pass

        functions = {'change': change_interface_name,
                     'disable': disable_interface,
                     'enable': enable_interface}

        if parameter_type in ['interface', 'interfaces']:
            return functions['change']()
        else:
            return functions['disable']()

