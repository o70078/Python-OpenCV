#coding: utf-8
__author__= 'orangleliu'
__version__ = '0.1'
'''''
直接执行pyhton文件就可以把webservice启动了 
服务启动之后可以在浏览器： http://localhost:7789/?wsdl 
得到一个xml文件，具体怎么解读还需要查看资料 

需要研究下怎么手动写一个http客户端来请求webservice 
'''
import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array

class HelloWorldService(DefinitionBase):
    @soap(String,Integer,_returns=Array(String))
    def say_hello(self,name,times):
        results = []
        for i in range(0,times):
            results.append('Hello, %s'%name)
        return results
        
if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        soap_application = soaplib.core.Application([HelloWorldService], 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 7789, wsgi_application)
        print 'soap server starting......'
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"