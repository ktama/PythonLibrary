<!-- $theme: default -->

# Deep Learning勉強会
## データ拡張編

---

# なんでこのテーマ？

* 深層学習にはデータが必要
* 集められるデータには限りがある

---

# AIのアプリリリースに必要な技術

## AI構築

* 教師あり学習
* 教師なし学習
* 強化学習
* etc...

## データサイエンス

* データ収集
* データ拡張
* 可視化
* etc...

---

# ここから本題

---

# 画像のデータ拡張

---

# サイズ変更
![元画像](../Test.bmp) → ![サイズ変更](../resize_image.bmp)

```Python
def resize(self,size=(16,16), file_name='resize_image.bmp'):
  '''引数で指定したサイズへ変更す'''
  resize_image = skimage.transform.resize(
  self.raw_image,size)
  skimage.io.imsave(file_name,resize_image)
  return resize_image
```

---
# 反転（水平）
![元画像](../Test.bmp) → ![サイズ変更](../horizontal_flip_image.bmp)
```
def flip(self,is_horizontal=1,file_name='flip_image.bmp'):
  '''反転する（is_horizontal: True→水平、False→垂直）'''
  flip_image = cv2.flip(self.raw_image,is_horizontal)
  skimage.io.imsave(file_name,flip_image)
  return flip_image
```
---
# 反転（垂直）
![元画像](../Test.bmp) → ![サイズ変更](../vertical_flip_image.bmp)


---
# 回転
![元画像](../Test.bmp) → ![サイズ変更](../rotate45F_image.bmp)
```
def rotate(self,angle=90,is_resize=False,
  file_name='rotate_image.bmp'):
  '''指定した角度[0, 360]回転する（is_resize:
    True→画像が切れないように画像を拡大、
    False→画像が切れる）'''
  rotate_image = skimage.transform.rotate(
    self.raw_image,angle=angle,resize=is_resize)
  skimage.io.imsave(file_name,rotate_image)
  return rotate_image
```

---
# 平行移動
![元画像](../Test.bmp) → ![サイズ変更](../move_image.bmp)
```
def move(self,x=100,y=100,file_name='move_image.bmp'):
  '''x,y方向へ平行移動する'''
  height, width = self.raw_image.shape[:2]
  M = np.float32([[1,0,x],[0,1,y]])
  move_image = cv2.warpAffine(
    self.raw_image, M, (width, height))
  skimage.io.imsave(file_name,move_image)
  return move_image
```

---
# 拡大
![元画像](../Test.bmp) → ![サイズ変更](../expand_image.bmp)

```
def expand(self,rate=0.5,file_name='expand_image.bmp'):
  '''比率を指定して拡大する（例：0.5は50%拡大）'''
  size = self.raw_image.shape[0]
  matrix = skimage.transform.AffineTransform(
    scale=(1-rate,1-rate),
    translation=(size*rate/2,size*rate/2))
  expand_image = skimage.transform.warp(self.raw_image,matrix)
  skimage.io.imsave(file_name,expand_image)
  return expand_image
```

---
# 切り出し
![元画像](../Test.bmp) → ![サイズ変更](../random_crop1_image.bmp)

---
# 切り出し
```
def random_crop(self,input_image,crop_size=(200,200),
  file_name='random_crop_image.bmp'):
  '''サイズを指定してランダムに画像を切り出す'''
  h, w, _ = input_image.shape
  # 0～（画像サイズ - 切り抜きサイズ）の間でtop、leftを決める
  top = np.random.randint(0, h - crop_size[0])
  left = np.random.randint(0, w - crop_size[1])
  # 切り抜きサイズからbottomとrightを
  bottom = top + crop_size[0]
  right = left + crop_size[1]
  crop_image = input_image[top:bottom, left:right, :]
  return crop_image
```

---
# 切り抜き（平均画素）
![元画像](../Test.bmp) → ![サイズ変更](../cutout1_image.bmp)

---
# 切り抜き（平均画素）
```
def cutout(self,input_image,mask_size=100,
  file_name='cutout_image.bmp'):
  '''ランダムに指定したサイズをマスクする'''
  cutout_image = np.copy(input_image)
  mask_value =cutout_image.mean()

  h, w, _ = cutout_image.shape
  # マスクをかける場所をランダムに決定
  top = np.random.randint(0 - mask_size // 2, h - mask_size)
  left = np.random.randint(0 - mask_size // 2, w - mask_size)
  bottom = top + mask_size
  right = left + mask_size

  if top < 0:
      top = 0
  if left < 0:
      left = 0

  cutout_image[top:bottom, left:right, :].fill(mask_value)
  skimage.io.imsave(file_name,cutout_image)
  return cutout_image
```

---
# 切り抜き（ホワイト）
![元画像](../Test.bmp) → ![サイズ変更](../erase1_image.bmp)

---
# 切り抜き（ホワイト）
```
def erasing(self,input_image,mask_size_range=(0.02, 0.4), 
    aspect_range=(0.3, 3),file_name='erasing_image.bmp'):
    '''ランダムに指定したサイズを消去する'''
    erasing_image = np.copy(input_image)
    mask_value = np.random.randint(0, 256)
    h, w, _ = erasing_image.shape
    mask_area = np.random.randint(
    h*w*mask_size_range[0], h*w*mask_size_range[1])
    mask_aspect_ratio = 
    np.random.rand() * aspect_range[1] + aspect_range[0]
    mask_height = int(np.sqrt(mask_area / mask_aspect_ratio))
    if mask_height > h - 1:
        mask_height = h - 1
    mask_width = int(mask_aspect_ratio * mask_height)
    if mask_width > w - 1:
        mask_width = w - 1
    top = np.random.randint(0, h - mask_height)
    left = np.random.randint(0, w - mask_width)
    bottom = top + mask_height
    right = left + mask_width
    erasing_image[top:bottom, left:right, :].fill(mask_value)
    skimage.io.imsave(file_name,erasing_image)
    return erasing_image
```
---
# ソルトノイズ
![元画像](../Test.bmp) → ![サイズ変更](../salt1_image.bmp)

---
# ソルトノイズ
```
def salt_noise(self,input_image,rate=4,
    file_name='salt_image.bmp'):
    '''ソルトノイズを付与する'''
    salt_image = np.copy(input_image)
    num_salt = np.ceil((rate/100) * salt_image.size)
    coords = [np.random.randint(    0, i-1, int(num_salt)) for i in salt_image.shape]
    salt_image[coords[:-1]] = (255,255,255)
    skimage.io.imsave(file_name,salt_image)
    return salt_image
```
---
# ペッパーノイズ
![元画像](../Test.bmp) → ![サイズ変更](../pepper1_image.bmp)

---
# ペッパーノイズ
```
def pepper_noise(self,input_image,rate=4,
    file_name='pepper_image.bmp'):
    '''ペッパーノイズを付与する'''
    pepper_image = np.copy(input_image)
    num_pepper = np.ceil((rate/100) * pepper_image.size)
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in pepper_image.shape]
    pepper_image[coords[:-1]] = (0,0,0)
    skimage.io.imsave(file_name,pepper_image)
    return pepper_image
```

---

# まとめ

## やったこと
* サイズ変更
* 反転
* 回転
* 平行移動
* 拡大
* 切り出し
* 切り抜き
* ノイズ

## できたこと
1枚の画像を100倍程度に増やせた

---

# 予定

1. データ拡張（済）
2. データ収集（次回）
3. AI構築（次々回）

---


# 参考サイト
[test.py || PythonでData Augmentation](http://testpy.hatenablog.com/entry/2017/06/02/001901)
http://testpy.hatenablog.com/entry/2017/06/02/001901

[IMACEL ACADEMY || 現役JDと学ぶ画像処理入門①〜openCV入門〜](https://lp-tech.net/articles/qEftT)
https://lp-tech.net/articles/qEftT

[IMACEL ACADEMY || Pythonで画像処理② Data Augmentation (画像の水増し)](https://lp-tech.net/articles/nCvfb)
https://lp-tech.net/articles/nCvfb

[kumilog.train || NumPyでの画像のData Augmentationまとめ](http://xkumiyu.hatenablog.com/entry/numpy-data-augmentation)
http://xkumiyu.hatenablog.com/entry/numpy-data-augmentation

[Qiita || 機械学習のデータセット画像枚数を増やす方法](https://qiita.com/bohemian916/items/9630661cd5292240f8c7)
https://qiita.com/bohemian916/items/9630661cd5292240f8c7

---
# 使用したツール
Marp
