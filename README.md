# PythonLibrary
Pythonのライブラリ

# 設定ファイル検証

[JSON, YAML, ini, TOML ざっくり比較](https://gist.github.com/miyakogi/e8631ce5f7c956db2313)を見ながら、
下記の設定ファイルを実際に使ってみて比較します。

* [ini](./SettingFile/ini_file.py)
* [JSON](./SettingFile/json_file.py)
* [YAML](./SettingFile/yaml_file.py)
* [TOML](./SettingFile/toml_file.py)



読み込みを確認する設定値

* コメント
* 整数
* 浮動小数点
* 文字列
* リストor配列 ※文字列のみ扱えるものは読み込み後処理で処置
  * 数値のリスト
  * 文字列のリスト


# 参考にしたサイト

[test.py || PythonでData Augmentation](http://testpy.hatenablog.com/entry/2017/06/02/001901)

[IMACEL ACADEMY || 現役JDと学ぶ画像処理入門①〜openCV入門〜](https://lp-tech.net/articles/qEftT)

[IMACEL ACADEMY || Pythonで画像処理② Data Augmentation (画像の水増し)](https://lp-tech.net/articles/nCvfb)

[kumilog.train || NumPyでの画像のData Augmentationまとめ](http://xkumiyu.hatenablog.com/entry/numpy-data-augmentation)


[Qiita || 機械学習のデータセット画像枚数を増やす方法](https://qiita.com/bohemian916/items/9630661cd5292240f8c7)