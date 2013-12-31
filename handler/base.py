# coding=utf-8
'''
Created on 2013-5-18

@author: Microacup
'''
import tornado.web
import tornado.escape

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.jinja2 = self.settings.get("jinja2")
    
    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id: return None
        return tornado.escape.json_decode(user_id)

    def render(self, template_name, **template_vars):
        html = self.render_string(template_name, **template_vars)
        self.write(html)
    
    # 重写，以便与原生接口调用一致
    def render_string(self, template_name, **template_vars):
        template_vars["current_user"] = self.current_user
        template_vars["xsrf_form_html"] = self.xsrf_form_html
        template = self.jinja2.get_template(template_name)
        return template.render(**template_vars)

    def render_from_string(self, template_string, **template_vars):
        template = self.jinja2.from_string(template_string)
        self.write(template.render(**template_vars))
        
    def render_json(self, data):
        '''输出json，注意，这里不要使用self.write(dict(data)),不要相信源码里说的，
                        因为它输出不了汉字，而是输出了编码,所以，这里的参数接受一个dict或者str.
        '''
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(str(data))
        
    def write_error(self, status_code, **kwargs):
        print('what? error code:' + str(status_code))