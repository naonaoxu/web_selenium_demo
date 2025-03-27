import pytest
from time import strftime
from py.xml import html
from selenium import webdriver

from utils import project

send_browser=' '
send_url=' '

def pytest_addoption(parser):#browser/url copuld input as params
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
    report.title = "Demo of Web Automation Test" #define report title

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata:dict):    #change metadata
    metadata.pop("Packages")
    metadata.pop("Plugins")
 #   metadata['Browser'] = project.getBrowser_()
    metadata['Browser']=project.getBrowser_()['Browser'][0]
    metadata['URL'] = "".join(project.getBrowser_()['URL'])

'''
def pytest_configure(config):
    config._metadata.clear()
    config._metadata['Platfrom'] = ""
    config._metadata['WebBrowser'] = "Chrome"
    config._metadata["selenium"] = "4.7.0"
    
'''

def pytest_html_results_summary(prefix):     #change summay
    prefix.clear()  # clear summary
    prefix.extend([html.p("Author: MS.Xu")])

def pytest_html_results_table_header(cells):      #change table
    cells.pop(1)
    cells.pop(-1)
    cells.insert(1, html.th("TestCases", col="test"))
    cells.insert(3,html.th("Description",col="desc"))
    cells.insert(4, html.th("Time", class_="sortable time", col="time"))

def pytest_html_results_table_row(report,cells):   #detail in table
    cells.pop(1)
    cells.pop(-1)
    cells.insert(3, html.td(report.description))
    cells.insert(4, html.td(strftime('%Y-%m-%d %H:%M:%S'), class_='col-time'))
    cells.insert(1, html.th(report.__dict__['nodeid'].split('::')[0][5:-8]+report.__dict__['nodeid'].split('::')[-1][5:]))

#@pytest.mark.hookwrapper
#@pytest.hookimpl(hookwrapper=True)
#def pytest_runtest_makereport(item):
#    outcome = yield
#    report = outcome.get_result()
#    setattr(report,'duration_formatter',"%H:%M:%S.%f")
#    report.description = str(item.function.__doc__)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    out = yield
    res = out.get_result()  # Get result of testcase
    print(res)
    if res.when == "call":
        print("item：{}".format(item))
        print("CaseDescription：{}".format(item.function.__doc__))
        print("Exception：{}".format(call.excinfo))
        print("DetailLog：{}".format(res.longrepr))
        print("TestResult：{}".format(res.outcome))
        print("Duration：{}".format(res.duration))
        print(res.__dict__)
        print(f"****{res.__dict__['nodeid'].split('::')[0]}:{res.__dict__['nodeid'].split('::')[-1]}")
    res.description = str(item.function.__doc__)


