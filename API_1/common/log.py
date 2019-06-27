#-*- coding: utf-8 -*-
# @Time    : 2019/6/26 20:14
# @Author  : lemon_shan
# @Email   :1529755032@qq.com
# @File    : log.py

import logging
from API_1.common import path
class Log:

    def log(self,level,msg):

        log = logging.getLogger('python14')
        log.setLevel('INFO')

        formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-%(filename)s-%(name)s-[日志信息]:%(message)s')

        ch = logging.StreamHandler()
        ch.setLevel('INFO')
        ch.setFormatter(formatter)

        fh = logging.FileHandler(path.log_path,encoding='utf-8')
        fh.setLevel('INFO')
        fh.setFormatter(formatter)

        log.addHandler(fh)
        log.addHandler(ch)

        if level =='DEBUG':
            log.debug(msg)
        elif level =='INFO':
            log.info(msg)
        elif level =='ERROR':
            log.error(msg)
        elif level == 'WARNING':
            log.warning(msg)
        else:
            log.critical(msg)

        log.removeHandler(fh)
        log.removeHandler(ch)


    def debug(self,msg):
        self.log('DEBUG',msg)

    def info(self,msg):
        self.log('INFO',msg)

    def warning(self,msg):
        self.log('WARNING',msg)

    def error(self,msg):
        self.log('ERROR',msg)

    def critical(self,msg):
        self.log('CRITICAL',msg)

if __name__ == '__main__':
    test_log = Log()
    test_log.info('咔咔咔哎呀哎呀')

