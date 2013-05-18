# coding=utf-8
'''
Created on 2013-5-18

@author: Power
'''
import tornado.web
import tornado.ioloop
import os

import handler.index
import handler.login

from tornado.options import define, options, parse_command_line

define("port", default = 80, help = "run on the given port", type = int)

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            login_url = "/login",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret = "wozaiwolubianjiandaoyifenqian",
            xsrf_cookies = True,
        )
        
        handlers = [
            (r"/", handler.index.IndexHandler),
            (r"/login", handler.login.LoginHandler),
            (r"/signup", handler.login.SignHandler),
        ]
        
        tornado.web.Application.__init__(self, handlers, **settings)
        
def main():
    parse_command_line()
    http_server = Application()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == "__main__":
    main();    