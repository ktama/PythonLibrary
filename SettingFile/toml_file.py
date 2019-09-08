# -*- Coding: utf-8 -*-

import toml


def read(setting_file):
    with open(setting_file, encoding='utf-8') as f:
        toml_dic = toml.load(f)

        a = toml_dic['number']['alpha']
        b = toml_dic['number']['beta']
        c = a * b

        alphabet = toml_dic['text']['alphabet']
        ja = toml_dic['text']['japanese']
        path = toml_dic['text']['path']

        hoge = toml_dic['list']['hoge']
        piyo = toml_dic['list']['piyo']
        print(a)
        print(b)
        print(c)
        print(alphabet)
        print(ja)
        print(path)
        print(hoge)
        print(piyo)


if __name__ == '__main__':
    read('./SettingFile/toml.toml')
