# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427083820.786944
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan\\Desktop\\jcarlso2\\jcarlso2\\homepage\\templates/uploader.html'
_template_uri = 'uploader.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
 

        __M_writer('\n\n\t<h2>Upload a file.</h2>\n\n\t<div align="center">\n\t\t<form method="POST" enctype="multipart/form-data">\n\t\t\t<table>\n\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\n\t\t\t</table>\n\t\t\t<input type="submit"/>\n\t\t</form>\n\t</div>\n\n\t<br/>\n\n\t<div id="progress-bar" class="progress">\n\t  <div id="progress_bar" class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;">\n\t  </div>\n\t</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "52": 3, "53": 4, "55": 4, "56": 11, "57": 11, "27": 0, "45": 3, "63": 57}, "filename": "C:\\Users\\Jordan\\Desktop\\jcarlso2\\jcarlso2\\homepage\\templates/uploader.html", "uri": "uploader.html"}
__M_END_METADATA
"""
