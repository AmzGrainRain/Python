from os import path, makedirs, listdir, remove
from requests import get


def empty_dir(dir_path):
    """
    递归清空目录
    :param dir_path: 目录路径
    :return:
    """
    for i in listdir(dir_path):
        c_path = path.join(dir_path, i)
        if path.isdir(c_path):
            empty_dir(c_path)
        else:
            remove(c_path)


def init_dirs():
    # 不存在缓存目录则创建
    if not path.exists('./tmp'):
        makedirs('./tmp')

    # 清理缓存目录
    empty_dir('./tmp/')

    # 不存在图片目录则创建
    if not path.exists('./images'):
        makedirs('./images')

    # 清理图片目录
    empty_dir('./images/')


def is_jpg(byte_data):
    """
    通过比特数据判断文件是否为 jpg 格式
    :param byte_data: byte数组
    :return: 如果是 png 格式则返回 True 反之则返回 False
    """

    # jpg 文件的二进制数据总是以 ff d8 ff 开头
    jpg_byte_prefix = [255, 216, 255]
    # 核对数据
    for i in range(3):
        if byte_data[i] != jpg_byte_prefix[i]:
            return False
    return True


def is_png(byte_data):
    """
    通过比特数据判断文件是否为 png 格式
    :param byte_data: byte数组
    :return: 如果是 png 格式则返回 True 反之则返回 False
    """

    # png 文件的二进制数据总是以 89 50 4e 开头
    png_byte_prefix = [137, 80, 78]
    # 核对数据
    for i in range(3):
        if byte_data[i] != png_byte_prefix[i]:
            return False
    return True


def get_extname(file_path):
    """
    传入一个文件的路径，判断其扩展名是 jpg 或是 png
    :param file_path: 被判断的文件的路径
    :return: 成功则返回 jpg 或 png，其他情况返回 None
    """

    # 以 二进制读 的方式打开文件
    file = open(file_path, 'rb')
    # 读取前 24 位二进制数据
    byte_str = file.read(3)
    # 核对文件类型
    if is_jpg(byte_str):
        return 'jpg'
    elif is_png(byte_str):
        return 'png'
    return None


def download_file(url, filename):
    """
    下载文件
    :param url: 文件 url
    :param filename: 保存到本地的文件名
    :return: 返回下载完成的文件路径
    """

    # 文件路径
    filepath = './tmp/' + filename
    # 文件二进制数据
    bin_data = get(url).content
    # 存储二进制数据到本地文件
    with open(filepath, 'wb') as f:
        f.write(bin_data)

    return filepath
