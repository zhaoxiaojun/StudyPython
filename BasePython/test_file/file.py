#coding=utf8


fp = file('test5.py', 'wb')

methodDefined = r"""    def %(methodname)s(self):
        sdfsdfsdfsdfsdf
        sdfsdfsdfsdfsfdssdsf
        121312414 *
        return 1
"""

fp.writelines(methodDefined % {'methodname': 'nananana'})


fp.flush()
fp.close()
