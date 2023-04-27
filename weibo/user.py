import requests
import data
import os

class User:
  def __init__(self, id):
    self.id = id
    self.page = 1

    print('请稍候...')
    self.init_profile()
    self.init_blogs()
    
    os.system('cls')
    self.show_info()


  def init_profile(self):
    self.profile_api = f'https://weibo.com/ajax/profile/info?custom={self.id}'
    print(requests.get(url=self.profile_api, headers=data.header).json())
    return
    self.data = requests.get(url=self.profile_api, headers=data.header).json()['data']
  

  def init_blogs(self):
    self.blog_api = f'https://weibo.com/ajax/statuses/mymblog?uid={self.get_uid()}&page={self.page}&feature=0'
    self.blogs = requests.get(url=self.blog_api, headers=data.header).json()['data']


  def more_blogs(self):
    self.blog_api = f'https://weibo.com/ajax/statuses/mymblog?uid={self.get_uid()}&page={self.page}&feature=0&since_id={self.blogs["since_id"]}'
    self.blogs = requests.get(url=self.blog_api, headers=data.header).json()['data']


  def get_name(self):
    if not self.data:
      return ''
    
    return self.data['user']['screen_name']


  def get_id(self):
    return self.id


  def get_uid(self):
    if not self.data:
      return ''

    return self.data['user']['id']


  def get_followers(self):
    if not self.data:
      return ''

    return self.data['user']['followers_count_str']


  def more_blog(self):
    self.page += 1
    self.more_blogs()
    self.show_blogs()


  def show_info(self):
    print('-' * 145)
    print(f'昵称: {self.get_name()}')
    print(f'账号: {self.get_id()}')
    print(f'UID: {self.get_uid()}')
    print(f'粉丝: {self.get_followers()}')


  def show_page_info(self):
    print(f'第 {self.page} 页 | 共 {self.blogs["total"]} 条数据')


  def show_blogs(self):
    for item in self.blogs['list']:
      try:
        print('-' * 145)
        print(item['region_name'])
        print(f'id: {item["id"]}')
        print(f'date: {item["created_at"]}')
        print('text: ' + item["text_raw"].replace("\n", ""))
      except:
        print('跳过广告...')
        continue

    print('-' * 145)
    self.show_page_info()
