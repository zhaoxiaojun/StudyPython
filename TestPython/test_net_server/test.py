#coding-UTF8
import sys, traceback
 
traceback_template = '''Traceback (most recent call last):
 File "%(filename)s", line %(lineno)s, in %(name)s
%(type)s: %(message)s\n''' # Skipping the "actual line" item


try:
    x=1/0
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
            'filename': exc_traceback.tb_frame.f_code.co_filename,
            'lineno' : exc_traceback.tb_lineno,
            'name'  : exc_traceback.tb_frame.f_code.co_name,
            'type'  : exc_type.__name__,
            'message' : exc_value.message, # or see traceback._some_str()
    }
    print traceback_template % traceback_details
    
    
    