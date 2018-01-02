import numpy as np
import cv2
import matplotlib.pyplot as plt
import skimage
from skimage import io
from skimage import transform
from scipy.misc import imresize
from scipy.ndimage.interpolation import rotate

class DataAugmentation:
    '''画像のデータ拡張するためのクラス（bmpのみ対応）
    '''
    def __init__(self, original_file='Test.bmp'):
        '''インスタンス作成時に引数で画像ファイルのパスを指定する
        '''
        self.raw_image = skimage.io.imread(original_file)

    def resize(self,input_image,size=(16,16), file_name='resize_image.bmp'):
        '''引数で指定したサイズへ変更する
        '''
        resize_image = skimage.transform.resize(input_image,size)
        skimage.io.imsave(file_name,resize_image)
        return resize_image

    def flip(self,input_image,is_horizontal=1,file_name='flip_image.bmp'):
        '''反転する（is_horizontal: True→水平、False→垂直）
        '''
        flip_image = cv2.flip(input_image,is_horizontal)
        skimage.io.imsave(file_name,flip_image)
        return flip_image

    def horizontal_flip(self,input_image,file_name='horizontal_flip_image.bmp'):
        '''水平方向に反転
        '''
        flip_image = input_image[:,::-1,:]
        skimage.io.imsave(file_name,flip_image)
        return flip_image

    def vertical_flip(self,input_image,file_name='vertical_flip_image.bmp'):
        '''垂直方向に反転
        '''
        flip_image = input_image[::-1,:,:]
        skimage.io.imsave(file_name,flip_image)
        return flip_image


    def rotate(self,input_image,angle=90,is_resize=False,file_name='rotate_image.bmp'):
        '''指定した角度[0, 360]回転する（is_resize: True→画像が切れないように画像を拡大、False→画像が切れる）
        '''
        rotate_image = skimage.transform.rotate(input_image,angle=angle,resize=is_resize)
        skimage.io.imsave(file_name,rotate_image)
        return rotate_image

    def random_rotation(self,input_image,angle_range=(0,360),file_name='random_rotate.bmp'):
        h, w, _ = input_image.shape
        angle = np.random.randint(*angle_range)
        rotate_image = rotate(input_image, angle)
        rotate_image = imresize(rotate_image, (h,w))
        skimage.io.imsave(file_name,rotate_image)
        return rotate_image

    def move(self,input_image,x=100,y=100,file_name='move_image.bmp'):
        '''x,y方向へ平行移動する
        '''
        height, width = input_image.shape[:2]
        # 変換行列の作成
        M = np.float32([[1,0,x],[0,1,y]])
        move_image = cv2.warpAffine(input_image, M, (width, height))
        skimage.io.imsave(file_name,move_image)
        return move_image

    def expand(self,input_image,rate=0.5,file_name='expand_image.bmp'):
        '''比率を指定して拡大する（例：0.5は50%拡大）
        '''
        size = input_image.shape[0]
        matrix = skimage.transform.AffineTransform(scale=(1-rate,1-rate),translation=(size*rate/2,size*rate/2))
        expand_image = skimage.transform.warp(input_image,matrix)
        skimage.io.imsave(file_name,expand_image)
        return expand_image                                                   

    def bright(self,input_image,brightness=50,file_name='bright_image.bmp'):
        '''輝度を比率で変更する（例：1.2は2倍） 調査中
        '''
        bright_image = np.minimum(input_image+brightness,255)
        # cv2.imwrite(file_name,bright_image)
        skimage.io.imsave(file_name,bright_image)
        return bright_image

    def random_crop(self,input_image,crop_size=(200,200),file_name='random_crop_image.bmp'):
        h, w, _ = input_image.shape

        # 0～（画像サイズ - 切り抜きサイズ）の間でtop、leftを決める
        top = np.random.randint(0, h - crop_size[0])
        left = np.random.randint(0, w - crop_size[1])

        # 切り抜きサイズからbottomとrightを
        bottom = top + crop_size[0]
        right = left + crop_size[1]

        crop_image = input_image[top:bottom, left:right, :]
        skimage.io.imsave(file_name,crop_image)
        return crop_image

    def scale_random_crop(self,input_image,scale_range=(350,600), crop_size=(340,340),file_name='scale_random_crop_image.bmp'):
        scale_size = np.random.randint(*scale_range)
        crop_image = imresize(input_image, (scale_size, scale_size))
        crop_image = self.random_crop(crop_image, crop_size)
        skimage.io.imsave(file_name,crop_image)
        return crop_image

    def cutout(self,input_image,mask_size=100,file_name='cutout_image.bmp'):
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

    def erasing(self,input_image,mask_size_range=(0.02, 0.4), aspect_range=(0.3, 3),file_name='erasing_image.bmp'):
        erasing_image = np.copy(input_image)
        mask_value = np.random.randint(0, 256)

        h, w, _ = erasing_image.shape
        mask_area = np.random.randint(h*w*mask_size_range[0], h*w*mask_size_range[1])
        mask_aspect_ratio = np.random.rand() * aspect_range[1] + aspect_range[0]

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

if __name__ == '__main__':
    aug = DataAugmentation()
    # aug.resize(input_image=aug.raw_image,size=(100,100))
    # for i in range(1, 8):
    #     angle = i * 45
    #     false_file_name = "rotate"+str(angle)+"F_image.bmp"
    #     true_file_name = "rotate"+str(angle)+"T_image.bmp"
    #     aug.rotate(input_image=aug.raw_image,angle=angle, is_resize=False, file_name=false_file_name)
    #     aug.rotate(input_image=aug.raw_image,angle=angle, is_resize=True, file_name=true_file_name)

    # aug.move(input_image=aug.raw_image)
    # aug.expand(input_image=aug.raw_image)
    # あとで修正
    # aug.bright(input_image=aug.raw_image,0.8,'bright1_image.bmp')
    # aug.bright(input_image=aug.raw_image,1.2,'bright2_image.bmp')

    # aug.horizontal_flip(input_image=aug.raw_image)
    # aug.vertical_flip(input_image=aug.raw_image)
    # for i in range(10):
        # crop_name = 'random_crop' + str(i) + '_image.bmp'
        # aug.random_crop(input_image=aug.raw_image,file_name=crop_name)
        # scale_crop_name = 'scale_random_crop' + str(i) + '_image.bmp'
        # aug.scale_random_crop(input_image=aug.raw_image,file_name=scale_crop_name)
        # rotation_random_name = 'rotation_random_crop' + str(i) + '_image.bmp'
        # aug.random_rotation(input_image=aug.raw_image,file_name=rotation_random_name)
        # cutout_name = 'cutout' + str(i) + '_image.bmp'
        # aug.cutout(input_image=aug.raw_image,file_name=cutout_name)
        # erase_name = 'erase' + str(i) + '_image.bmp'
        # aug.erasing(input_image=aug.raw_image,file_name=erase_name)


