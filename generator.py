from typing import *
import yaml 
import os

def get_list_of_files(dir_name: str):
    fileList = os.listdir(dir_name)
    result = []
    for entry in fileList: 
        full_path = os.path.join(dir_name, entry) 
        if os.path.isdir(full_path):
            result = result + get_list_of_files(full_path)
        else:
            result.append(full_path)
    return result

def file_read_to_end(path): 
    f = open(path,"r",encoding='utf-8')
    content = f.read()
    f.close() 
    return content

def parse_yaml_headers(mdtext : str):
    result = {} 
    try: 
        start_index = mdtext.index("---")
        if start_index != 0:
            raise ValueError(f"파싱할 수 없습니다.") 
        
        end_index = mdtext.index("---",start_index + 1)
        mdtext = mdtext[start_index: end_index]

        result = yaml.load(mdtext, Loader=yaml.FullLoader)
    except ValueError:
        raise ValueError
    except Exception as e:
        raise e
    
    return result

def valid_yaml_headers(yaml_dict : dict):
    keys = ("file", "name", "src", "tags", "done")
    return set(keys).issubset(yaml_dict)

def make_list(path):
    file_list = get_list_of_files(path)
    result = []
    for file in file_list:
        try: 
            dir = os.path.dirname(file)
            body = file_read_to_end(file)
            headers = parse_yaml_headers(body)

            if not valid_yaml_headers(headers): 
                raise ValueError("필요한 키가 포함되어있지 않음")
            
            result.append({
                "file": os.path.join(dir, headers["file"]),
                "name": headers["name"],
                "src": headers["src"],
                "tags": headers["tags"],
                "done": headers["done"],
            })
            print(dir)

        except Exception as e:
            raise e
    
    return result

def make_markdown_table(hlist):
    """
    흠..
    """
    
path = ".\\baekjoon"
lst = make_list(path)
print(lst)

    # vegetables = yaml.load(f, Loader=yaml.FullLoader)
    # print(vegetables)

# file_list2 = get_list_of_files(".\\baekjoon")
# print(file_list2) 