#encoding=utf-8
import logging
import sys
from logging import handlers
from utils.project import *

level_relations = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "crit": logging.CRITICAL
}

def get_logger(logPath=log_path,logname=log_name, level='info'):
    if os.path.exists(logPath):
        pass
    else:
        os.mkdir(logPath)
    filename=os.path.join(logPath,logname)
    Log = logging.getLogger(filename)
    Log.setLevel(level_relations.get(level))
    fmt = logging.Formatter('%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    if not Log.handlers:
        consoler_handler = logging.StreamHandler(sys.stdout)
        consoler_handler.setFormatter(fmt)
        file_handler = handlers.RotatingFileHandler(filename=filename, maxBytes = 1 *1024*1024*1024,backupCount=1,
                                                    encoding='utf-8')
        file_handler.setFormatter(fmt)
#        Log.addHandler(consoler_handler)
        Log.addHandler(file_handler)
    return Log