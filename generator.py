"""
TO-DO:
    - 문제 정렬 기준
"""
from collections import defaultdict
from urllib import parse
from typing import *
import fnmatch
import yaml
import os
from pytablewriter import MarkdownTableWriter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


__tier_text = {
    "Unknown": 0,
    "Bronze V": 1,
    "Bronze IV": 2,
    "Bronze III": 3,
    "Bronze II": 4,
    "Bronze I": 5,
    "Silver V": 6,
    "Silver IV": 7,
    "Silver III": 8,
    "Silver II": 9,
    "Silver I": 10,
    "Gold V": 11,
    "Gold IV": 12,
    "Gold III": 13,
    "Gold II": 14,
    "Gold I": 15,
    "Platinum V": 16,
    "Platinum IV": 17,
    "Platinum III": 18,
    "Platinum II": 19,
    "Platinum I": 20,
    "Diamond V": 21,
    "Diamond IV": 22,
    "Diamond III": 23,
    "Diamond II": 24,
    "Diamond I": 25,
    "Ruby V": 26,
    "Ruby IV": 27,
    "Ruby III": 28,
    "Ruby II": 29,
    "Ruby I": 30,
    "Master": 31,
}


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
    result = defaultdict(None)
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

            # draft 처리
            if headers.get("draft"):
                continue

            item = {
                "file_name": headers.get("file"),
                "path": dir.replace('\\', '/'),
                "file": os.path.join(dir, headers.get("file")).replace('\\', '/'),
                "name": headers.get("name"),
                "src": headers.get("src"),
                "tags": sorted(headers.get("tags")),
                "done": headers.get("done"),
                "date": headers.get("date"),
                "level": headers.get("level"),
                "difficulty": headers.get("difficulty"),
            }
            result.append(item)
            print(file)

        except Exception as e:
            raise e

    return result


def make_markdown_table(hlist: list, orderby_date=False):
    """
    흠..
    """
    result = []

    # sort
    def orderKey(x): return (x["tags"], x["date"])
    if orderby_date:
        def orderKey(x): return (x["date"], x["tags"])

    hlist = sorted(hlist, key=orderKey)
    hlist = sorted(hlist, key=lambda x: x["done"], reverse=True)

    writer = MarkdownTableWriter(
        headers=["이름", "태그", "풀이", "완료", "#"],
        value_matrix=[
            [
                f"[{x['name']}]({x['src']})",
                ', '.join(x['tags']),
                f"[{x['file_name']}]({parse.quote(x['path'])})",
                f"{'✔️' if x['done'] else '❌'}",
                f"{x['difficulty']}"

            ]
            for x in hlist
        ],
        add_index_column=True,
        margin=1
    )
    return writer.dumps()


debug = False

if __name__ == "__main__":
    rows = make_filedata_list("./baekjoon")
    baekjoon_table = make_markdown_table(rows, orderby_date=True)
    for tier in __tier_text.keys(): 
        baekjoon_table = baekjoon_table.replace(tier, f"![{tier}](./assets/{__tier_text[tier]}.svg)")

    rows = make_filedata_list("./leetcode")
    leetcode_table = make_markdown_table(rows)

    rows = make_filedata_list("./programmers")
    programmers_table = make_markdown_table(rows)

    template = file_read_to_end('./util/template.md')

    # 치환 해준다
    readme_text = template\
        .replace("__baekjoon_table__", baekjoon_table)\
        .replace("__leetcode_table__", leetcode_table)\
        .replace("__programmers_table__", programmers_table)

    # make readme.md
    if not debug:
        f = open(os.path.join(BASE_DIR, 'README.md'), "w", encoding='utf-8')
        f.write(readme_text)
        f.close()
    else:
        print(readme_text)
