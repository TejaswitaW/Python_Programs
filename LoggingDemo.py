#logging in python module
import logging  as lg
lg.basicConfig(filename="log.txt",level=lg.WARNING)
print("Python logging demo")
lg.debug('debug message')
lg.info('info message')
lg.warning('warning message')
lg.error('error message')
lg.critical('debug message')
