#!/usr/bin/python3
import requests

tracker_url = "https://trackerslist.com/best_aria2.txt"
header = {'User-Agent': 'Mozilla/5.0 (x86_64; rv:85.0) Gecko Firefox'}


def parse_task():
    task = open('task.txt', 'r')
    url = open('url.txt', 'w')
    repo = open('repo.txt', 'w')
    file_path = open('file_path.txt', 'w')
    info = task.read().splitlines()
    url.write(info[0])
    file_path.write(info[1])
    repo.write(info[2])
    task.close()
    url.close()
    repo.close()
    file_path.close()
    print(info[0], info[1], info[2], "task parsed!")


def add_tracker(url):
    r = requests.get(url)
    trackers = r.text
    conf = open('aria2.conf', 'a+')
    conf.write(f'bt-tracker={trackers}')
    conf.close()
    print("tracker added!")


if __name__ == '__main__':
    parse_task()
    add_tracker(tracker_url)
