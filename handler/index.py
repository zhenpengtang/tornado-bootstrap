# coding=utf-8
'''
Created on 2013-5-18

@author: Power
'''
import handler.base

class IndexHandler(handler.base.BaseHandler):
    def get(self):
        self.render("index.html")