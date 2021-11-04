import requests
import argparse
import datetime
import html
import os
from pytablewriter import MarkdownTableWriter

__tier_text = {
    0: "Unknown",
    1: "Bronze V",
    2: "Bronze IV",
    3: "Bronze III",
    4: "Bronze II",
    5: "Bronze I",
    6: "Silver V",
    7: "Silver IV",
    8: "Silver III",
    9: "Silver II",
    10: "Silver I",
    11: "Gold V",
    12: "Gold IV",
    13: "Gold III",
    14: "Gold II",
    15: "Gold I",
    16: "Platinum V",
    17: "Platinum IV",
    18: "Platinum III",
    19: "Platinum II",
    20: "Platinum I",
    21: "Diamond V",
    22: "Diamond IV",
    23: "Diamond III",
    24: "Diamond II",
    25: "Diamond I",
    26: "Ruby V",
    27: "Ruby IV",
    28: "Ruby III",
    29: "Ruby II",
    30: "Ruby I",
    31: "Master",
}

def write_all_text(path: str, text: str) -> None:
    f = open(path, 'w')
    f.write(text)
    f.close()


def make_problem_yaml(problem: dict) -> str:
    lines = []
    lines.append("---")
    lines.append(f"file: \"{problem['id']}.md\"")
    lines.append(f"name: \"{problem['name']}\"")
    lines.append(f"src: \"{problem['url']}\"")
    tags = '\n'+'\n'.join(f'  - {x}' for x in problem['tags']) if len(problem['tags']) > 0 else ''
    lines.append(f"tags: {tags}")
    lines.append(f"done: false")
    lines.append(f"draft: false")
    lines.append(f"level: {problem['level']}")
    lines.append(f"difficulty: \"{problem['difficulty']}\"")
    lines.append(f"date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    lines.append("---\n")
    return '\n'.join(lines)


def get_problems(problems: list) -> dict:
    """문제 정보를 담고 있는 딕셔너리를 반환합니다.
    """
    if len(problems) < 1:
        raise ValueError("Invalid number of problems")

    url = f"https://solved.ac/api/v3/problem/lookup?problemIds={','.join(problems)}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Unexpected response status")

    json_data = response.json()
    problems = []

    for problem in json_data:
        problem_info = {}
        problem_info["id"] = problem["problemId"]
        problem_info["name"] = html.unescape(problem["titleKo"])
        problem_info["level"] = problem["level"]
        problem_info["difficulty"] = __tier_text[problem["level"]]
        problem_info["url"] = f"https://www.acmicpc.net/problem/{problem['problemId']}"
        # language ko만 추출
        if problem["tags"] is not None:
            tags = [x["displayNames"] for x in problem["tags"]]
            problem_info["tags"] = [x["name"]
                                    for tags in tags for x in tags if x["language"] == 'ko']
        problems.append(problem_info)

    return problems

# response = requests.get("https://solved.ac/api/v3/problem/show?problemId=1052")
# json_data = response.json()


class CommandLineParser:
    def __init__(self):
        parser = argparse.ArgumentParser(description="백준 문제 가져오기 사용법")

        parser.add_argument("-p", "--problems", nargs='+',
                            help="사용법 -p 1052 3023", required=True, default="")
        parser.add_argument(
            "-o", "--output", help="사용법: -o 문제 정보를 저장할 디렉터리", required=False, default="")
        parser.add_argument(
            "-r", "--random", help="사용법: -r [최소레벨] [최대레벨] 레벨 범위 안에서 문제를 랜덤으로 가져옵니다.", required=False, default="")
        parser.add_argument(
            "-c", "--count", help="사용법: -c [가져올 문제 갯수]", required=False, default="")

        try:
            self.__problems = []
            self.__output = ""
            self.__valid = False
            argument = parser.parse_args()

            if argument.problems:
                try:
                    self.__problems = argument.problems
                    self.__valid = True
                except:
                    print("문제번호는 숫자로 기입해주세요.")
            if argument.output:
                self.__output = argument.output
        except:
            parser.print_help()

    def validation(self):
        return self.__valid

    def problems(self):
        return self.__problems

    def save_dir(self):
        return self.__output


if __name__ == '__main__':
    app = CommandLineParser()

    if app.validation():
        problems = app.problems()
        save_dir = app.save_dir()

        problems_info = get_problems(problems)

        writer = MarkdownTableWriter(
            table_name="example_table",
            headers=["문제 번호", "이름", "문제 레벨", "solved.ac 티어", "태그"],
            value_matrix=[
                [x['id'], x['name'], x['level'], x['difficulty'], ', '.join(x['tags'])] for x in problems_info
            ],
            margin=2
        )

        print(writer.dumps())

        if len(save_dir) > 0:
            for problem in problems_info:
                write_all_text(os.path.join(
                    save_dir, f"{problem['id']}.md"), make_problem_yaml(problem))
