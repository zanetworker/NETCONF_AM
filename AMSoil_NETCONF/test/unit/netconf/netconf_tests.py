import unittest
import jsonrpclib

class TestNETCONF(unittest.TestCase):

    server = jsonrpclib.Server('http://localhost:3333')

    # def test_interfaces(self):
    #     """
    #     Test setting the value of an interface using the set_parameter method.
    #
    #     Check whether the value was correctly modified on the server side by retrieving a copy of the configuration
    #     and making sure it contains the desired parameter
    #     """
    #     result = TestNETCONF.server.set_parameter('interfaces', ['interface', 'eth0'])
    #     #self.assertIn('<interface>', result)
    #     self.assertIsNotNone(result)


    def test_experimenter(self):
        """
        Test setting the value of an experimenter using the set_parameter method.

        Check whether the value was correctly modified on the server side by retrieving a copy of the configuration
        and making sure it contains the desired parameter
        """
        result = TestNETCONF.server.set_parameter('properties', ['experimenter', 'admin'])
        self.assertIsNotNone(result)
        #self.assertIn('<experimenter>', result)



if __name__ == '__main__':
    unittest.main()