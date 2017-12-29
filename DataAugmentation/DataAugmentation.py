import numpy as np
import cv2
import matplotlib.pyplot as plt
import skimage
from skimage import io
from skimage import transform

class DataAugmentation:
    '''画像のデータ拡張するためのクラス（bmpのみ対応）
    '''
    def __init__(self, original_file='Test.bmp'):
        '''インスタンス作成時に引数で画像ファイルのパスを指定する
        '''
        self.raw_image = skimage.io.imread(original_file)

    def resize(self,size=(16,16), file_name='resize_image.bmp'):
        '''引数で指定したサイズへ変更する
        '''
        resize_image = skimage.transform.resize(self.raw_image,size)
        skimage.io.imsave(file_name,resize_image)
        return resize_image

    def flip(self,is_horizontal=1,file_name='flip_image.bmp'):
        '''反転する（is_horizontal: True→水平、False→垂直）
        '''
        flip_image = cv2.flip(self.raw_image,is_horizontal)
        skimage.io.imsave(file_name,flip_image)
        return flip_image

    def rotate(self,angle=90,is_resize=False,file_name='rotate_image.bmp'):
        '''指定した角度[0, 360]回転する（is_resize: True→画像が切れないように画像を拡大、False→画像が切れる）
        '''
        rotate_image = skimage.transform.rotate(self.raw_image,angle=angle,resize=is_resize)
        skimage.io.imsave(file_name,rotate_image)
        return rotate_image

    def move(self,x=100,y=100,file_name='move_image.bmp'):
        '''x,y方向へ平行移動する
        '''
        height, width = self.raw_image.shape[:2]
        # 変換行列の作成
        M = np.float32([[1,0,x],[0,1,y]])
        move_image = cv2.warpAffine(self.raw_image, M, (width, height))
        skimage.io.imsave(file_name,move_image)
        return move_image

    def expand(self,rate=0.5,file_name='expand_image.bmp'):
        '''比率を指定して拡大する（例：0.5は50%拡大）
        '''
        size = self.raw_image.shape[0]
        matrix = skimage.transform.AffineTransform(scale=(1-rate,1-rate),translation=(size*rate/2,size*rate/2))
        expand_image = skimage.transform.warp(self.raw_image,matrix)
        skimage.io.imsave(file_name,expand_image)
        return expand_image                                                   


if __name__ == '__main__':
    aug = DataAugmentation()
    aug.resize((100,100))
    aug.flip(1, "flip_h_image.bmp")
    aug.flip(0, "flip_v_image.bmp")
    for i in range(1, 8):
        angle = i * 45
        false_file_name = "rotate"+str(angle)+"F_image.bmp"
        true_file_name = "rotate"+str(angle)+"T_image.bmp"
        aug.rotate(angle, False, false_file_name)
        aug.rotate(angle, True, true_file_name)

    aug.move()
    aug.expand()
