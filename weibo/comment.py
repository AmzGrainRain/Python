import requests
import data
import os

header = data.header
header['referer'] = f'https://weibo.com/{data.user.get_id()}'

def get_comment(id):
    api = f'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id={id}&is_show_bulletin=2&is_mix=0&count=10&uid={data.user.get_id()}&fetch_level=0'
    data.comment = requests.get(url=api, headers=header).json()


def show_comments():
    for item in data.comment['data']:
        print('-' * 145)
        print(item['source'])
        print(f'编号：{item["id"]}')
        print(f'日期：{item["created_at"]}')
        print('评论内容：' + item["text_raw"].replace("\n", ""))
    
    print('-' * 145)


def get_more(id):
    api = f'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id={id}&is_show_bulletin=2&is_mix=0&max_id={data.comment["max_id"]}&count=20&uid={data.user.get_id()}&fetch_level=0'
    data.comment = requests.get(url=api, headers=header).json()


def print_menu():
    print('查看更多: more')
    print('退出评论: exit')
    print('-' * 145)

def main_loop(id):
    get_comment(id)
    os.system('cls')
    show_comments()

    while True:
        print_menu()
        op = input('[评论区]> ')

        if op == 'more':
            get_more(id)
            show_comments()
            continue
        if op == 'exit':
            print('已退出评论区')
            break
