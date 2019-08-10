import yaml
import os

def analyze_file(file_name,key):
    with open("."+os.sep+"data"+os.sep+file_name, "r" , encoding="utf-8")as f:
        data = yaml.load(f)
        dict_data = data[key]
        list_data = []
        for i in dict_data.values():
            list_data.append(i)

        return list_data
