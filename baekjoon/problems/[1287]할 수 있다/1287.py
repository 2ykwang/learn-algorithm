"""
    문제 이름: 할 수 있다
    문제 번호: 1287
    문제 링크: https://www.acmicpc.net/problem/1287
    난이도: Platinum V
    태그: 사칙연산, 많은 조건 분기, 구현, 수학, 파싱, 문자열

    첫째 줄에는 계산해야 되는 식이 주어진다. (띄어쓰기 없이, 길이는 1,000자를 넘지 않는다.)

    식을 구성하는 문자는 다음과 같다.

    +, -, /, *, (, ), 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    +, -, /, *는 모두 이항연산자로만 사용할 수 있다. 즉, (+6+3)과 같은 식은 올바르지 않은 식이다.
    또한, 계산 과정 중에 소수점이 등장하지 않는다.

    5+(1+2)*3   ->   14

"""

import sys


def input(): return sys.stdin.readline().rstrip()


class Token:
    def __init__(self, t: str, l: str = ""):
        self.token_type = t
        self.literal = l

    def __str__(self):
        return f"{self.token_type}{f'({self.literal})' if len(self.literal)>0 else ''}"


class TokenType:
    ADD = 'ADD'
    SUB = 'SUB'
    DIV = 'DIV'
    MUL = 'MUL'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    NUM = 'NUM'


token_dict = {
    '+': TokenType.ADD,
    '-': TokenType.SUB,
    '/': TokenType.DIV,
    '*': TokenType.MUL,
    '(': TokenType.LPAREN,
    ')': TokenType.RPAREN,
}


def tokenizer(body: str) -> list:
    result = []
    seek = 0

    while seek < len(body):

        if body[seek] in token_dict:
            result.append(Token(token_dict[body[seek]]))
            seek += 1

        elif body[seek].isdigit():
            literal = read_number(body, seek)
            result.append(Token(TokenType.NUM, literal[0]))
            seek += literal[1]
        else:
            seek += 1
    return result


def read_number(body: str, start_pos: int) -> tuple:
    cur_pos = start_pos

    while cur_pos < len(body) and body[cur_pos].isdigit():
        cur_pos += 1

    return (body[start_pos:cur_pos], cur_pos-start_pos)


class Calc:

    def __init__(self) -> None:
        self.__token = []
        self.__seq = 0
        self.__token_count = 0
        self.__err = False
        self.__ans = 0

    def cur_token(self) -> Token:
        return (self.__token[self.__seq] if self.__token_count > self.__seq else None)

    def next_token(self) -> int:
        self.__seq += 1
        return self.__seq

    def valid(self):
        return self.__err == False

    def answer(self):
        return self.__ans

    def expression(self) -> int:
        result = self.term()
        t = self.cur_token()
        while t is not None and (t.token_type == TokenType.ADD or t.token_type == TokenType.SUB):

            self.next_token()
            rhs = self.term()

            if t.token_type == TokenType.ADD:
                result += rhs
            else:
                result -= rhs
            t = self.cur_token()

        return result

    def term(self) -> int:
        result = self.factor()

        t = self.cur_token()

        while t is not None and (t.token_type == TokenType.MUL or t.token_type == TokenType.DIV):
            self.next_token()
            rhs = self.factor()
            # print(result, rhs)
            if t.token_type == TokenType.MUL:
                result *= rhs
            else:
                result //= rhs

            t = self.cur_token()

        return result

    def factor(self) -> int:
        result = 0
        t = self.cur_token()

        if t is not None:

            if t.token_type == TokenType.LPAREN:
                self.next_token()
                t = self.cur_token()

                # 바로 괄호 닫히면
                if t.token_type == TokenType.RPAREN:
                    self.__err = True

                result = self.expression()

                # 재귀 호출된 후 현재 가리키고 있는 토큰 타입이 RPAREN이 아닐경우 error
                if self.cur_token() is None or self.cur_token().token_type != TokenType.RPAREN:
                    # print(self.__token[self.__seq-1])
                    self.__err = True

                self.next_token()
                # check next token is RPAREN

                return result

            if t.token_type == TokenType.NUM:
                result = int(t.literal)
                self.next_token()

        return result

    def eval(self, s: str) -> None:
        self.__err = False
        self.__seq = 0
        self.__ans = 0
        self.__token = tokenizer(s)

        self.__token_count = len(self.__token)

        oper = [TokenType.ADD, TokenType.SUB, TokenType.MUL, TokenType.DIV]
        level = 0

        for i in range(self.__token_count):

            # 괄호 레벨이 일치하지 않은 경우
            if self.__token[i].token_type == TokenType.LPAREN:
                level += 1
            elif self.__token[i].token_type == TokenType.RPAREN:
                level -= 1

            if level < 0:
                self.__err = True
                break

            # 연산자 앞 뒤에 또 다른 연산자가 포함된경우
            if (self.__token[i].token_type in oper
                and (i-1 < 0 or i+1 > self.__token_count
                or self.__token[i-1].token_type in [*oper, TokenType.LPAREN]
                or self.__token[i+1].token_type in [*oper, TokenType.RPAREN])):

                self.__err = True
                break

            if (self.__token[i].token_type == TokenType.NUM
                and self.__token[i-1].token_type == TokenType.LPAREN
                and self.__token[i+1].token_type == TokenType.RPAREN):

                self.__err = True
                break

        if self.__err == False:
            self.__ans = self.expression()


calc = Calc()

s = input()

if s.count('(')-s.count(')') == 0:
    calc.eval(s)
    print(calc.answer() if calc.valid() else "ROCK")
else:
    print("ROCK")
