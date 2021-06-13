"""

Regular Expressions
^ - starts with
? - optional
+ - one or more
$ - end
"""
import re

RE_NUM = r'[0-9]+'
RE_ALPHA = r'[0-9]+'
RE_ALPHANUM = r'[0-9]+'
RE_OPERANDS = r'[0-9]+'
RE_NUM_TEXT = r'(zero|one|two|three|four|five|six|seven|eight|nine)'
RE_VAR_SYMBOLS = r'b|c|x|y|z'


def get_alpha(str_line):
    list_nums = re.findall(RE_ALPHA, str_line)
    return list_nums


def get_alphanum(str_line):
    list_nums = re.findall(RE_ALPHANUM, str_line)
    return list_nums


def get_operands(str_line):
    list_nums = re.findall(RE_OPERANDS, str_line)
    return list_nums


def get_numbers(str_line):
    list_nums = re.findall(RE_NUM, str_line)
    return list_nums


def get_num_text(str_line):
    list_nums = re.findall(RE_NUM_TEXT, str_line)
    return list_nums


def get_var_symbols(str_line):
    list_nums = re.findall(RE_VAR_SYMBOLS, str_line)
    return list_nums


def main():
    s = "adbv345hj43hvb42one"
    array = get_numbers(s)
    print(*array)
    s = "adbv345hj43hvb42one"
    array = get_alpha(s)
    print(*array)
    s = "adbv345hj43hvb42one"
    array = get_alphanum(s)
    print(*array)
    s = "adbv345hj43hvb42one"
    array = get_operands(s)
    print(*array)
    s = "adbv345hj43hvb42one"
    array = get_num_text(s)
    print(*array)
    s = "adbv345hj43hvb42one"
    array = get_var_symbols(s)
    print(*array)


if __name__ == '__main__':
    main()
