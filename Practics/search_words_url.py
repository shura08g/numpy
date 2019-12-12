# -*- coding: utf-8 -*-

from urllib.request import urlopen, ProxyHandler, build_opener, install_opener
from urllib.error import URLError, HTTPError

words = {}
my_url = "http://www.bbc.co.uk/"
# my_url = "http://korrespondent.net/"
html_list = []

# try:
#     html = urlopen("http://korrespondent.net/")
# except URLError as err:
#     print("Not found!!!")
#     print(err)


def GetURL(url):
    s = 'error'
    try:
        f = urlopen(url)
        s = f.read()
    except HTTPError:
        s = 'connect error'
    except URLError:
        s = 'url error'
    return s


def GetURL_proxy(url):
    # create the object, assign it to a variable
    proxy = ProxyHandler({'http': '192.168.0.1:3128'})
    # construct a new opener using your proxy settings
    opener = build_opener(proxy)
    # install the openen on the module-level
    install_opener(opener)
    s = urlopen(my_url)
    # s = urlretrieve(url)
    # s = temp.read()
    return s


def to_list(from_):
    to_ = []
    for line in from_:
        try:
            to_.append(line.decode("ascii"))
        except:
            pass
    return to_


def have_number(word):
    flag = False
    for symbol in word:
        try:
            int(symbol)
            flag = True
        except ValueError:
            flag = False
        if flag:
            return flag
    return flag


def in_word(word, sym_list):
    flag = False
    for symbol in sym_list:
        if symbol in word:
            flag = True
        if flag:
            return flag
    return flag


def replace_in_word(word, sym):
    for s in sym:
        word = word.replace(s, "")
    return word


def fill_words(html, without_sym):
    words_dict = dict()
    for line in html:
        line = line.strip(" \n")
        l = line.split(" ")
        for word in l:
            if in_word(word, without_sym):
                continue
            if 1 < len(word) < 15 and not have_number(word):
                word = replace_in_word(word, sym_replace)
                try:
                    words_dict[word] += 1
                except KeyError:
                    words_dict[word] = 1
    return words_dict

symbs = ['{', '}', '=', '&', '<', '/', "'", ',', '+', '-', '>', '<', '!', '*', '(', ')', '|', '[', ']', '_']
sym_replace = [":", ";", ",", ".", '"', "'"]

# html = GetURL(my_url)
html = GetURL_proxy(my_url)

html_list = to_list(html)

words = fill_words(html_list, symbs)

pairs = sorted(words.items(), key=lambda x: x[1], reverse=True)

# for k, v in sorted(words.items()):
#     print(k + ": " + str(v))

for p in pairs[:10]:
    print(p[0] + ": " + str(p[1]))
    # pass
