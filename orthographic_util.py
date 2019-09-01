# coding: utf-8
import csv
import re


def get_orthographic_list(file):
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
        raise EnvironmentError


def check_orthographic(text, orthographic_lis):
    cp_lis = orthographic_lis.copy()
    for dic in cp_lis:
        for key in dic.keys():
            for m in re.finditer(key, text, re.MULTILINE):
                dic[key] = dic[key] + 1
    return cp_lis


def print_result(lis):
    for dic in lis:
        if(sum(dic.values()) > 0):
            print(dic)


def gettext(file):
    try:
        with open(file, encoding="utf-8") as f:
            return f.read()
    except EnvironmentError:
        raise EnvironmentError