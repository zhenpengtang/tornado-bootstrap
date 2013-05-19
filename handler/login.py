# coding=utf-8
'''
Created on 2013-5-18

@author: Microacup
'''
import handler.base

class LoginHandler(handler.base.BaseHandler):
    def get(self):
        self.render("login.html")
        
    def post(self):
        self.redirect("/")
        # TODO ...验证用户
        
class SignHandler(handler.base.BaseHandler):
    def get(self):
        self.render("login.html")
        
    def post(self):
        self.redirect("/")