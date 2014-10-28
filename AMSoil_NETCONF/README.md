


# What is AMsoil

AMsoil is a light-weight framework for creating Aggregate Managers (AM) for test beds.
AMsoil is a pluggable system. It gives structure to develop new AMs and provides helpers for common tasks in AM development.

AMsoil is part of the [OFELIA](http://www.fp7-ofelia.eu) [Control Framework (OCF)](https://github.com/fp7-ofelia).
It has been extended to suite a the requirements of [ALIEN](http://www.fp7-alien.eu).

If you don't know what an Aggregate Manager is please see [here](https://alpha.fp7-ofelia.eu/doc/index.php/General_terminology).

# What is AMsoil NETCONF AM?

The NETCONF AM is an aggregate manager that is built using the AMSoil framework. Using the NETCONF AM, it is possible
easily modify underlying network device configurations without the need to memorize NETCONF specific commands.
Therefore it simplifies network configuration management.

# How to do a quick test for NETCONF AM?

To test the NETCONF AM please first install [netopeer] (https://code.google.com/p/netopeer/) server software on your
device. Furthermore, initialize the following YANG models (availabe in the "yangs" folder) inside the netopeer server to be able to issue configuration
mangement commands:

- zanetworker-box.yang
- of-config1.1.1.yang

The details on how to install a yang model inside your netopeer server is available [here] (https://code.google.com/p/netopeer/)


Finally, once the netopeer server is running log into "test/client/netconfclient.py", edit the test file and run it
to start configuring your underlying device.

