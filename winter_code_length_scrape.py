# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import requests
from IPython import embed

class User:
    def __init__(self, id):
        self.id = id
        self.work_list = {}
        self.sum_size = None

    def add_file(self, filename, size):
        self.work_list[filename] = size

    def size(self):
        self.sum_size = self.sum_size or sum(self.work_list[i] for i in self.work_list)
        return self.sum_size

    def print_info(self):
        print(self.id)
        print("size: " + str(self.size()))
        print("files: " + " | ".join("{0}({1})".format(i, self.work_list[i]) for i in self.work_list))
        print('-' * 100 + "\n")

s = requests.Session()

id_list = ["13fi025", "14fi013", "14fi044", "14fi052", "14fi061", "14fi085", "14fi088", "14fi091", "14fi401", "15fi001", "15fi002", "15fi003", "15fi004", "15fi005", "15fi006", "15fi007", "15fi008", "15fi009", "15fi010", "15fi011", "15fi012", "15fi013", "15fi014", "15fi015", "15fi016", "15fi017", "15fi018", "15fi019", "15fi021", "15fi022", "15fi023", "15fi024", "15fi025", "15fi026", "15fi027", "15fi028", "15fi029", "15fi030", "15fi031", "15fi032", "15fi033", "15fi034", "15fi035", "15fi036", "15fi037", "15fi039", "15fi040", "15fi041", "15fi042", "15fi043", "15fi044", "15fi045", "15fi046", "15fi047", "15fi048", "15fi049", "15fi050", "15fi051", "15fi052", "15fi053", "15fi054", "15fi056", "15fi057", "15fi058", "15fi059", "15fi060", "15fi061", "15fi062", "15fi063", "15fi064", "15fi065", "15fi067", "15fi069", "15fi070", "15fi071", "15fi072", "15fi075", "15fi077", "15fi078", "15fi080", "15fi081", "15fi082", "15fi083", "15fi084", "15fi085", "15fi086", "15fi087", "15fi088", "15fi089", "15fi090", "15fi091", "15fi092", "15fi093", "15fi094", "15fi095", "15fi096", "15fi097", "15fi098", "15fi099", "15fi100", "15fi101", "15fi102", "15fi103", "15fi104", "15fi105", "15fi106", "15fi107", "15fi108", "15fi109", "15fi110", "15fi111", "15fi112", "15fi113", "15fi115", "15fi116", "15fi117", "15fi118", "15fi119", "15fi120", "15fi121", "15fi122", "15fi123", "15fi124", "15fi125", "15fi126", "15fi127", "15fi128", "15fi129", "15fi130", "15fi131", "15fi132", "15fi133", "15fi134"]
url_format = 'http://www.mlab.im.dendai.ac.jp/programming/2015/user/{0}/blockBreakOriginal/applet/'
users = []
for id in id_list:
    url = url_format.format(id)
    r = s.get(url)
    soup = BeautifulSoup(r.text)
    len_sum = 0
    if len(soup.find_all('p')) <= 2:
        continue

    user = User(id)
    for ea in soup.find_all('p')[-2].find_all('a'):
        filename = ea['href']
        res = requests.get(url + filename)
        res.text
        len_sum += len(res.text)
        user.add_file(filename, len(res.text))
        # embed()
    users += [user]
    # print(soup)
    # exit()

users.sort(key=lambda x: -x.size())
for user in users:
    user.print_info()
