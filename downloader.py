import os
import requests

def parse(url, proxy=None):
    r = requests.get(url) 
    file_list = r.text.splitlines()
    prefix = url.replace("file_list.txt", '')
    if proxy:
        prefix = proxy + prefix + "/resource/"
    else:
        prefix = prefix + "/resource/"
    result = open("dl.txt", "a")
    for file in file_list:
        result.write(prefix + file + '\n')
    result.close()

def parse_jsd(url):
    r = requests.get(url)
    file_list = r.text.splitlines()
    jsd = "https://cdn.jsdelivr.net/gh/"
    mid = url.replace("file_list.txt", '').replace("/main", "@main").split(".com/")[-1]
    result = open("dl.txt", "a")
    for file in file_list:
        result.write(jsd + mid + "resource/" + file + '\n')
    result.close()


if __name__ == "__main__":
    proxy = "https://dl.chan.im/url/"
    url = "https://raw.githubusercontent.com/0xfile/Adobe-Photoshop-CC-2019/main/file_list.txt"
    parse(url, proxy)
    os.system("wsl aria2c -i dl.txt")
