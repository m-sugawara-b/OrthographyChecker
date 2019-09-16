# coding: utf-8
import csv
import re


def read(file):
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
    except IOError:
        raise IOError


def wc(text, oglist):
    cplist = oglist.copy()
    for dic in cplist:
        for key in dic.keys():
            for m in re.finditer(key, text, re.MULTILINE):
                dic[key] = dic[key] + 1
    return cplist


def pprint(lis):
    for dic in lis:
        if(sum(dic.values()) > 0):
            print(dic)


def gettext(file):
    try:
        with open(file, encoding="utf-8") as f:
            return f.read()
    except IOError:
        raise IOError