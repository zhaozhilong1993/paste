''''' 
Created on 2016-12-27 
 
@author: zhaozhilong
'''  
  
from wsgiref.simple_server import make_server
import os
from paste.deploy import loadapp
import sys
import wsgi

class Controller(object):
    def __init__(self):
        print "Controller"

    def test(self, req):
        print "req",req
        return {
            "name":"test",
            "properties":"test"
        }

class MyRouterApp(wsgi.Router):
    def __init__(self, mapper):
        controller = Controller()
        mapper.connect(
            '/test',
            controller=wsgi.Resource(controller),
            action='test',
            conditions={'method':['GET']}
        )
        super(MyRouterApp, self).__init__(mapper)

