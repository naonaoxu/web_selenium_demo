import pytest
from time import strftime
import pytest_html
from py.xml import html
from selenium import webdriver

send_browser=' '
send_url=' '


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default = "chrome",help="serial of the mode")
    parser.addoption("--url", action="store", default="https://www.126.com", help="serial of the mode")

@pytest.fixture(scope="session",autouse=True)
def getBrowser(request):
    global send_browser
    send_browser = request.config.getoption('browser')
    return send_browser

@pytest.fixture(scope="session",autouse=True)
def getUrl(request):
    global send_url
    send_url = request.config.getoption('url')
    return send_url

def pytest_html_report_title(report):
    report.title = "Demo of Web Automation Test"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata:dict):
    metadata.pop("Packages")
    metadata.pop("Plugins")
    metadata['Browser']="TBD"
    metadata['URL'] = "TBD"
'''
def pytest_configure(config):
    config._metadata.clear()
    config._metadata['Platfrom'] = ""
    config._metadata['WebBrowser'] = "Chrome"
    config._metadata["selenium"] = "4.7.0"
    
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata["其他环境"] = "联网环境"    
'''

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.clear()  # 清空summary中的内容
    prefix.extend([html.p("Author: MS.Xu")])

def pytest_html_results_table_header(cells):
    cells.insert(3,html.th("Description",col="desc"))
    cells.insert(4, html.th("Time", class_="sortable time", col="time"))
    cells.pop()

def pytest_html_results_table_row(report,cells):
    cells.insert(3,html.td(report.description))
    cells.insert(4, html.td(strftime('%Y-%m-%d %H:%M:%S'), class_='col-time'))
    cells.pop()

@pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    setattr(report,'duration_formatter',"%H:%M:%S.%f")
    report.description = str(item.function.__doc__)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    out = yield  # 钩子函数
    res = out.get_result()  # 获取用例执行结果
    print(res)
    if res.when == "call":  # 只获取call用例失败时的信息
        print("item：{}".format(item))
        print("CaseDescription：{}".format(item.function.__doc__))
        print("Exception：{}".format(call.excinfo))
        print("DetailLog：{}".format(res.longrepr))
        print("TestResult：{}".format(res.outcome))
        print("Duration：{}".format(res.duration))
        print(res.__dict__)
    res.description = str(item.function.__doc__)


