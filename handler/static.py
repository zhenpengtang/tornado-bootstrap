# coding=utf-8
'''
Created on 2013-5-19

@author: Microacup
'''
import  handler.base

class PageNotFoundHandler(handler.base.BaseHandler):
    def get(self):
        self.render("snippet/404.html");
