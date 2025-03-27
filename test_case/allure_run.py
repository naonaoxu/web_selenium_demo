#encoding=utf-8
import pytest
import os
import shutil

from utils.project import set_windows_title, set_report_name

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', '..//report//xml',"../test_case"])
    shutil.copy("..//environment.properties",'..//report//xml')
    os.system('allure generate --clean %s -o %s' % ('..//report//xml', '..//report//html'))
    set_windows_title('..//report//html//index.html','Web Automation Test Demo')
    set_report_name('..//report//html','Web Automation Test Demo')
