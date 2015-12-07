#coding=utf8
import logging


console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
