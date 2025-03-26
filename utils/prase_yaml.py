#encoding=utf-8
import inspect

import yaml
from utils import project
from utils.logger import get_logger
Log=get_logger()

class PraseYaml:

    @classmethod
    def load_yaml(self, file_path):
        try:
            with open(file_path,encoding='utf-8') as f:
                data = yaml.load(f.read(),Loader=yaml.FullLoader)
 #           Log.info(f"The data in {file_path} is {data}")
            return data
        except Exception as e:
            Log.info(e ,"Not find yaml")
            return {}

    @classmethod
    def get_dict_data(self,data,*args):
        try:
            for i in args:
                data = data.get(i)
            return data
        except Exception as e:
            Log.info(e,"Not find:  Krgs: ",args ,"in ",data)
            return {}

    @classmethod
    def get_page_ele(self,path=project.element_file):
        return self.load_yaml(path)

#*krgs need write code
    @classmethod
    def get_yaml_data(self,file_path,*args):
        data = self.load_yaml(file_path)
        try:
            for i in args:
                data = data.get(i)
                return data
        except Exception as e:
            Log.info(e,"Not find: " ,file_path ,"Krgs: ",args)
            return {}

    @classmethod
    def get_yaml_name(self,file_path):
        data = self.load_yaml(file_path)
        try:
            name = inspect.stack()[2].function
            steps = data[name]
            Log.info(f"Yaml {name}.data is {steps}")
            return steps
        except Exception as e:
            Log.info(e)
            return {}

if __name__ == '__main__':
    pass
 #   print(PraseYaml.get_yaml_data("../test_data/test_001Login.yaml", 'case1'))
#    for case in PraseYaml.get_dict_data(PraseYaml.get_yaml_data("../test_data/test_001Login.yaml", 'case')):
 #       print(case[0]['senario'])
 #   print(PraseYaml.get_dict_data({'aa':{'bb':{'cc':'cc','dd':'dd'},'b1':'b1'}},'aa','bb','cc'))
