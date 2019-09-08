# -*- Coding: utf-8 -*-

import yaml


def read(setting_file):
    with open(setting_file, encoding='utf-8') as f:
        yml = yaml.load(f)

        a = yml.get('alpha')
        b = yml.get('beta')
        c = a * b

        alphabet = yml.get('alphabet')
        ja = yml.get('japanese')
        path = yml.get('path')

        hoge = yml.get('hoge')
        piyo = yml.get('piyo')
        hogehoge = yml.get('hogehoge')
        print(a)
        print(b)
        print(c)
        print(alphabet)
        print(ja)
        print(path)
        print(hoge)
        print(piyo)
        print(hogehoge)


if __name__ == '__main__':
    read('./SettingFile/yaml.yaml')
