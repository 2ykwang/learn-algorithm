"""
TO-DO:
    - 문제 정렬 기준
"""

from typing import *
import fnmatch
import yaml
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


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


def file_read_to_end(path: str):
    f = open(path, "r", encoding='utf-8')
    content = f.read()
    f.close()
    return content


def parse_yaml_headers(mdtext: str):
    result = {}
    try:
        start_index = mdtext.index("---")
        if start_index != 0:
            raise ValueError(f"파싱할 수 없습니다.")

        end_index = mdtext.index("---", start_index + 1)
        mdtext = mdtext[start_index: end_index]

        result = yaml.load(mdtext, Loader=yaml.FullLoader)
    except ValueError:
        raise ValueError
    except Exception as e:
        raise e

    return result

def valid_yaml_headers(yaml_dict: dict):
    keys = ("file", "name", "src", "tags", "done", "date")
    return set(keys).issubset(yaml_dict)

def make_filedata_list(path: str):
    """
        src->ee
        
        eee
    """
    file_list = fnmatch.filter(get_list_of_files(path), "*.md")
    result = []

    for file in file_list:
        try:
            dir = os.path.dirname(file)
            body = file_read_to_end(file)
            headers = parse_yaml_headers(body)

            if not valid_yaml_headers(headers):
                raise ValueError("필요한 키가 포함되어있지 않음")

            result.append({
                "file_name": headers["file"],
                "path": dir.replace('\\', '/'),
                "file": os.path.join(dir, headers["file"]).replace('\\', '/'),
                "name": headers["name"],
                "src": headers["src"],
                "tags": sorted(headers["tags"]),
                "done": headers["done"],
                "date": headers["date"],
            })
            print(dir)

        except Exception as e:
            raise e

    return result

def make_markdown_table(hlist: list[dict],
                        orderby_done=False):
    """
    흠..
    """
    result = []

    # sort
    hlist = sorted(hlist, key=lambda x: (x["tags"], x["date"]))
    hlist = sorted(hlist, key=lambda x: x["done"], reverse=True)

    columns = [
        {"name": "#", "size": 5},
        {"name": "문제 이름", "size": 20},
        {"name": "유형", "size": 15},
        {"name": "풀이", "size": 10},
        {"name": "완료", "size": 6},
    ]
    result.append('|'.join([key["name"] for key in columns]))
    result.append('|'.join([key["size"]*'-' for key in columns]))

    for index, header in enumerate(hlist):
        row = []

        done = '✔️' if header["done"] else '❌'

        row.append(str(index+1))
        row.append(f"[{header['name']}]({header['src']})")
        row.append(', '.join(header['tags']))
        row.append(f"[{header['file_name']}]({header['path']})")
        row.append(done)

        result.append('|'.join(row))

    result.append('')
    return '\n'.join(result)


debug = False

if __name__ == "__main__": 
    rows = make_filedata_list("./baekjoon")
    baekjoon_table = make_markdown_table(rows, orderby_done=True)

    rows = make_filedata_list("./leetcode")
    leetcode_table = make_markdown_table(rows, orderby_done=True)
    template = file_read_to_end('template.md')

    # 치환 해준다
    readme_text = template.replace("__baekjoon_table__", baekjoon_table)\
        .replace("__leetcode_table__",leetcode_table)
    # make readme.md
    if not debug:
        f = open(os.path.join(BASE_DIR, 'README.md'), "w", encoding='utf-8')
        f.write(readme_text)
        f.close()
    else:
        print(readme_text)
