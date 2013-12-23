# coding=utf-8
'''
Created on 2013-5-18

@author: Power
'''
import tornado.web
import tornado.ioloop
import os
import yaml

import handler.index
import handler.login
import handler.static

from tornado.options import parse_command_line
from jinja2 import Environment, FileSystemLoader

config = yaml.load(open('./config/config.yaml'))
server = config['server']

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            login_url="/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret=server['cookie_secret'],
            xsrf_cookies=True,
            autoescape=None,
            jinja2=Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")), trim_blocks=True),
        )
        
        handlers = [
            (r"/", handler.index.IndexHandler),
            (r"/login", handler.login.LoginHandler),
            (r"/signup", handler.login.SignHandler),
            (r".*", handler.static.PageNotFoundHandler)
        ]
        
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = config['db'];
        
def main():
    parse_command_line()
    http_server = Application()
    http_server.listen(server['port'])
    print("服务已启动...请访问：http://%s:%d" % (server['host'], server['port']))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print("服务正在启动...")
    main()
