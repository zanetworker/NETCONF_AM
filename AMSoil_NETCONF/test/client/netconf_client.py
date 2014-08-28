import jsonrpclib

def main():
    """
    Run the Application
    """
    server = jsonrpclib.Server('http://localhost:2222')
    #result = server.set_parameter('experimenter', 'adel')
    #result = server.list_interfaces()
    result = server.list_properties()
    print result

if __name__ == "__main__":
    main()
