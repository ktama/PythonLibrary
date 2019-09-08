# -*- Coding: utf-8 -*-

import configparser


def read(setting_file):
    config = configparser.ConfigParser()
    config.read(setting_file, encoding='utf-8')

    a = int(config.get('number', 'alpha'))
    b = float(config.get('number', 'beta'))
    c = a * b

    alphabet = config.get('text', 'alphabet')
    ja = config.get('text', 'japanese')
    path = config.get('text', 'path')

    hoge = config.get('list', 'hoge').split()
    piyo = config.get('list', 'piyo').split()
    print(a)
    print(b)
    print(c)
    print(alphabet)
    print(ja)
    print(path)
    print(hoge)
    print(piyo)


if __name__ == '__main__':
    read('./SettingFile/ini.ini')
