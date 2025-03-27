import os
import json

project_path=os.path.dirname(os.path.dirname(__file__))

log_path=os.path.join(project_path,"log")

log_name="test.log"

element_file = os.path.join(os.path.join(project_path,"page"),'page_elements.yaml')

def set_windows_title(allure_html_path, new_title):
    with open(allure_html_path, 'r+', encoding="utf-8") as f:
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_the_lines:
            f.write(line.replace("Allure Report", new_title))
        f.close()


def set_report_name(allure_html_path, new_name):
    title_filepath = os.path.join(allure_html_path, "widgets", "summary.json")
    with open(title_filepath, 'rb') as f:
        params = json.load(f)
        params['reportName'] = new_name
        new_params = params
    with open(title_filepath, 'w', encoding="utf-8") as f:
        json.dump(new_params, f, ensure_ascii=False, indent=4)

def get_():
    with open('..//environment.properties','r') as f:
        lines=f.readlines()
        result_dict={}
        for line in lines:
            key= line.strip().split(':')[0]
            value= line.strip().split(':')[1:]
            result_dict[key] = value
        return result_dict

if __name__ == '__main__':
    print(project_path)
    get_()




