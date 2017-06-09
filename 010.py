import logging  
from suds.client import Client  
  
if __name__ == '__main__':  
    logging.basicConfig(level=logging.INFO)  
    logging.getLogger('suds.client').setLevel(logging.DEBUG)  
    hello_client = Client('http://localhost:7789/?wsdl', cache=None)  
    result = hello_client.service.say_hello("Dave", 5)  
    print result