'''
Задача 2: Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,. 
приоритет операций стандартный.
*Пример:
2+2 => 4;
1+2*3 => 7;
1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
Пример:
1+2*3 => 7;
(1+2)*3 => 9;
'''
import re

def GN(func, *args):
    def exec(text: str):
        return func(text, *args)
    return exec

def token(text: str, token_text: str):
    if text.startswith(token_text):
        return token_text, text[len(token_text):]
    return None, text

def rexpr(text: str, regex: str):
    text = text.lstrip()
    res = re.match(regex, text)
    if res:
        return res.group(0), text[res.end():]
    else:
        return None, text

def serial(text, *funcs):
    res, rest = [], text
    for func in funcs:
        resd, restd = func(rest)
        if resd is None:
            return None, text
        res.append(resd)
        rest = restd
    if len(res) == 0:
        return None, text
    return res, rest

def alternative(text, *funcs):
    for func in funcs:
        res, rest = func(text)
        if res is not None:
            return res, rest
    return None, text

def optional(text, func):
    res, rest = func(text)
    return [res], rest

def num(expr):
    res, rest = rexpr(expr, r"^[+-]?\d(\.\d+)?")
    if res is not None:
        return float(res), rest
    return res, rest

def value(expr):
    sign = GN(rexpr, r"[+-]")
    maybe_sign = GN(optional,  sign)
    val = GN(alternative, num, grouping)
    res, rest = serial(expr, maybe_sign, val)

    if res is None:
        return None, expr

    numb = res[1]
    if res[0][0] == "-":
        return -numb, rest
    return numb, rest

def grouping(expr):
    opened_bracket = GN(token, "(")  # token(text, "(")
    closed_bracket = GN(token, ")")  # token(text, ")")

    res, rest = serial(expr, opened_bracket, term, closed_bracket)

    if res is None:
        return None, expr
    return res[1], rest

def mul(expr):
    full_expr = GN(serial, value, GN(rexpr, r"[*/]"), mul)
    res, rest = alternative(expr, full_expr, value)

    if res is None:
        return None, expr

    if isinstance(res, float):
        return res, rest

    numb1 = res[0]
    op = res[1]
    numb2 = res[2]

    if op == "*":
        return numb1 * numb2, rest
    if op == "/":
        return numb1 / numb2, rest

    return None, expr

def sum(expr):
    full_expr = GN(serial, mul, GN(rexpr, r"[+-]"), sum)
    res, rest = alternative(expr, full_expr, mul)

    if res is None:
        return None, expr

    if isinstance(res, float):
        return res, rest

    numb1 = res[0]
    op = res[1]
    numb2 = res[2]

    if op == "+":
        return numb1 + numb2, rest
    if op == "-":
        return numb1 - numb2, rest

    return None, expr

def term(expr):
    return sum(expr)


print(term("2 + 2 * 2"))
