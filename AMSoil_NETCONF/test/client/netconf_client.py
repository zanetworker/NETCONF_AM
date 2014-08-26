import jsonrpclib

def main():
    """
    Run the Application
    """
    server = jsonrpclib.Server('http://localhost:2222')
    result = server.set_parameter('interface', 'eth1')

    print result

if __name__ == "__main__":
    main()
