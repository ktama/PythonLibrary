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
  '''引数で指定したサイズへ変更する
  '''
  resize_image = skimage.transform.resize(
  self.raw_image,size)
  skimage.io.imsave(file_name,resize_image)
  return resize_image
```

---
# 反転（水平）
![元画像](../Test.bmp) → ![サイズ変更](../flip_h_image.bmp)
```
def flip(self,is_horizontal=1,file_name='flip_image.bmp'):
  '''反転する（is_horizontal: True→水平、False→垂直）'''
  flip_image = cv2.flip(self.raw_image,is_horizontal)
  skimage.io.imsave(file_name,flip_image)
  return flip_image
```
---
# 反転（垂直）
![元画像](../Test.bmp) → ![サイズ変更](../flip_v_image.bmp)


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

# まとめ
* サイズ変更
* 反転
* 回転
* 平行移動
* 拡大

---

# 予定

1. データ拡張（済）
2. データ収集（次回）
3. AI構築（次々回）

---


# 参考サイト


