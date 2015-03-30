# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427074776.526406
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan\\Desktop\\jcarlso2\\jcarlso2\\homepage\\templates/table.html'
_template_uri = 'table.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        initial_page = context.get('initial_page', UNDEFINED)
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
        def content():
            return render_content(context)
        initial_page = context.get('initial_page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
 

        __M_writer('\n\n    <div class="content">\n    \t<h3>Paginated Table</h3>\n\n    \t<div id="table_container" data-page="')
        __M_writer(str( initial_page ))
        __M_writer('">\n    \t\tTable should be here.\n    \t</div>\n\n\n    \t<button class="btn btn-default" id="prev_page_button">&larr; Previous Page</button>\n    \t<button class="btn btn-default" id="next_page_button">Next Page &rarr;</button>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Jordan\\Desktop\\jcarlso2\\jcarlso2\\homepage\\templates/table.html", "line_map": {"35": 1, "52": 3, "53": 4, "55": 4, "56": 9, "57": 9, "27": 0, "45": 3, "63": 57}, "uri": "table.html"}
__M_END_METADATA
"""
