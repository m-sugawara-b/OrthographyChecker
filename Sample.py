# coding: utf-8
import csv
import re

def get_orthographic_list(file):
    """
    揺らぎファイルを読み込み、辞書型に変換して返す。

    Args:
        file: 揺らぎファイルのパス

    Returns:
        辞書をリストにしたもの。

    Raises:
        KeyError: EnviromentError
    """
    try:
        with open(file, encoding="utf-8") as f:
            lis = list()
            reader = csv.reader(f)
            for row in reader:
                dic = {}
                for element in row:
                    dic[element] = 0
                lis.append(dic)
            return lis
    except EnvironmentError:
        print(file + "が読み込めませんでした。")


def check_orthographic(text, lis):
    reslis = lis.copy()
    for dic in reslis:
        for key in dic.keys():
            for m in re.finditer(key, text, re.MULTILINE):
                dic[key] = dic[key] + 1
    return reslis

def print_result(lis):
    for dic in lis:
        if(sum(dic.values()) > 0):
            print(dic)


lis = get_orthographic_list("/Users/m.sugawara/Documents/git/GrammerChecker/orthographic.csv")
lis2 = check_orthographic("避難してください。そうしてください。いや、やっぱりやめて下さい。", lis)
print_result(lis2)