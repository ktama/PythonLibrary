import numpy as numpy
import cv2
import matplotlib.pyplot as plt
import skimage
from skimage import io
from skimage import transform

class DataAugmentation:
    def __init__(self):
        # read image
        self.raw_image = skimage.io.imread('Test.bmp')

    def resize(self.size(16,16), file_name='resize_image.bmp'):
        resize_image = skimage.transform.resize(self.raw_image)
        skimage.io.imsave(file_name,resize_image)
        return resize_image

    def flip(self.is_horizontal=1,file_name='flip_image.bmp'):
        flip_image = skimage.transform.resize(self.raw_image,is_horizontal)
        skimage.io.imsave(file_name,flip_image)
        return flip_image

    def rotate(self.angle=90,is_resize=False,file_name='rotate_image.bmp'):
        rotate_image = skimage.transform.rotate(self.raw_image,angle=angle,resize=is_resize)
        skimage.io.imsave(file_name,rotate_image)
        return rotate_image

    def expand(self.rate=0.5,file_name='expand_image.bmp'):
        size = self.raw_image.shape[0]
        matrix = skimage.transform.AffineTransform(scale=(1-rate,1-rate),translation=(size*rate/2,size*rate/2))
        expand_image = skimage.transform.warp(self.raw_image,matrix)
        skimage.io.imsave(file_name,expand_image)
        return expand_image                                                   
      

if __name__ == '__main':
