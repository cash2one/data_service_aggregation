#conding=utf-8
#!/usr/bin/env python

import sys
import os

def get_module_name():

    def main_module_name():
        mod = sys.modules['__main__']
        file = getattr(mod, '__file__', None)
        return file and os.path.splitext(os.path.basename(file))[0]

    def modname(fvars):

        file, name = fvars.get('__file__'), fvars.get('__name__')
        if file is None or name is None:
            return None

        if name == '__main__':
            name = main_module_name()
        return name

    module_name = modname(globals())
    return module_name


def getParam(request,param_name):
    paramvalue = request.POST.get(param_name, None)
    if paramvalue == None:
        paramvalue = request.GET.get(param_name, None)
    return paramvalue