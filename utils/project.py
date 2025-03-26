import os

#获取工程所在的目录的绝对路径
project_path=os.path.dirname(os.path.dirname(__file__))

log_path=os.path.join(project_path,"log")

log_name="test.log"

element_file = os.path.join(os.path.join(project_path,"page"),'page_elements.yaml')

#main_url="https://www.cathaypacific.com/cx/sc_CN.html"

if __name__ == '__main__':
    print(project_path)




