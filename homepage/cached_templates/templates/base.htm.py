# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427074773.352904
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan\\Desktop\\jcarlso2\\jcarlso2\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html lang="en">\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>homepage</title>\n    \n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n\n    <!-- Latest compiled and minified CSS -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n    <!-- Optional theme -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\n    <!-- Latest compiled and minified JavaScript -->\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n  \n    <header>\n      <nav class="navbar navbar-default">\n        <div class="container-fluid">\n          <!-- Brand and toggle get grouped for better mobile display -->\n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n              <span class="sr-only">Toggle navigation</span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">JCARLSO2</a>\n          </div>\n\n          <!-- Collect the nav links, forms, and other content for toggling -->\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n            <ul class="nav navbar-nav">\n              <li class="active"><a href="/homepage/table">Paginated Table<span class="sr-only">(current)</span></a></li>\n              <li><a href="#">Link</a></li>\n              <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>\n                <ul class="dropdown-menu" role="menu">\n                  <li><a href="#">Action</a></li>\n                  <li><a href="#">Another action</a></li>\n                  <li><a href="#">Something else here</a></li>\n                  <li class="divider"></li>\n                  <li><a href="#">Separated link</a></li>\n                  <li class="divider"></li>\n                  <li><a href="#">One more separated link</a></li>\n                </ul>\n              </li>\n            </ul>\n            <form class="navbar-form navbar-left" role="search">\n              <div class="form-group">\n                <input type="text" class="form-control" placeholder="Search">\n              </div>\n              <button type="submit" class="btn btn-default">Submit</button>\n            </form>\n            <ul class="nav navbar-nav navbar-right">\n              <li><a href="#">Link</a></li>\n              <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>\n                <ul class="dropdown-menu" role="menu">\n                  <li><a href="#">Action</a></li>\n                  <li><a href="#">Another action</a></li>\n                  <li><a href="#">Something else here</a></li>\n                  <li class="divider"></li>\n                  <li><a href="#">Separated link</a></li>\n                </ul>\n              </li>\n            </ul>\n          </div><!-- /.navbar-collapse -->\n        </div><!-- /.container-fluid -->\n      </nav>\n    </header>\n  \n    <div class="container">\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n    </div>\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n        Site content goes here in sub-templates.\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Jordan\\Desktop\\jcarlso2\\jcarlso2\\homepage\\templates/base.htm", "line_map": {"33": 5, "34": 15, "35": 25, "36": 25, "37": 25, "42": 89, "43": 93, "44": 93, "45": 93, "16": 4, "18": 0, "51": 87, "57": 87, "27": 2, "28": 4, "29": 5, "63": 57}, "uri": "base.htm"}
__M_END_METADATA
"""
