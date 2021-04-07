import os
import re


def add_quotes(str):
    return '"{}"'.format(str)


def str_replace(old_str, new_str, src_str):
    """
    字符串替换
    :param old_str:
    :param new_str:
    :param src_str:
    :return:
    """
    return re.sub(old_str, new_str, src_str)


def dei_blankline(str):
    """
    删除字符串中的空行
    :param str:
    :return:
    """
    return "".join([s for s in str.splitlines(True) if s.strip()])


def get_dir_files(path):
    pathnames = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            pathnames += [os.path.join(dirpath, filename)]
    return pathnames
