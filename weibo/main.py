import data
from user import User
import os
import configparser


def debug_init():
    data.client_version = 'v2.40.40'
    data.server_version = 'v2023.04.23.5'
    data.cookie = input('cookie: ')
    data.xsrf_token = input('xsrf-version: ')


def init():
    data.client_version = input('client-version: ')
    data.server_version = input('server-version: ')
    data.cookie = input('cookie: ')
    data.xsrf_token = input('xsrf-version: ')


def print_menu():
    print('-' * 145)
    print('查看微博: show')
    print('查看更多: more')
    print('查看评论: comments <id>')
    print('设置UID: set_user_name')
    print('退出: exit')


def main_loop():
    # data.cookie = input('请输入 cookie: ')
    data.client_version = input('请输入 client-version: ')
    data.cookie = 'SINAGLOBAL=6556936655152.614.1682245766763; ULV=1682245766765:1:1:1:6556936655152.614.1682245766763:; PC_TOKEN=94c73c6404; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWXHpvX5Tf4FGAXgaY8YULC5JpX5KMhUgL.FoMfeKBcSh.peK22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNSK2XSoB4eK2p; ALF=1684925101; SSOLoginState=1682333101; SCF=AgenYkZ4_HCfvGzG238fAFMG1j9LlxuWeaIC-_E8wig5P3pZxYuQPd6FKiomHWH8eh33nHM4Hxf19yWWBkFUOLQ.; SUB=_2A25JQi39DeRhGeFL6lYX9CfNyj2IHXVqNhg1rDV8PUNbmtANLWPmkW9NQmeHliHF3d-bkPBumwE5x5YzaFgeX1wv; XSRF-TOKEN=I6ZTuhTVETJCxUXEKKyfXX3u; WBPSESS=sa-PnEMWKzHZNSeOZvXLGYbQT-2KM3_XefWDBDXdJ5tsdjYg-HHqyq9VcP368g03XhmermsnACKexu_8Fly-kGLkoqNzTMWrpMvNmHelNYdO7CBcbDSQnshm9g7lRBNFDsbieG6tbp46cAQIXKLdeA=='
    data.user = User(input('请输入微博用户名: '))
    from comment import main_loop as comments

    while True:
        print_menu()
        print('-' * 145)
        op = input(f'[{data.user.get_name()}的微博]> ')

        if len(op) == 0:
            continue
        if op == 'show':
            os.system('cls')
            data.user.show_blogs()
            continue
        if op == 'more':
            os.system('cls')
            data.user.more_blog()
            continue
        if op == 'set_user_name':
            os.system('cls')
            data.user = None
            data.user = User(input('请输入微博用户名: '))
            continue
        if op == 'exit':
            exit(0)
        
        op = op.split(' ')
        if op[0] == 'comments':
            comments(op[1])

main_loop()