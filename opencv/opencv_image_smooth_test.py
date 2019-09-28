import cv2
from util import file_utils,constant
import numpy as np
from matplotlib import pyplot as plt
#图像平滑

path = file_utils.get_data_path(constant.naruto_image, "image")

#2D卷积，用5*5大小的滤波器乘以对应的图像像素点的和再求平均值，代替像素的值
def conv2d():
    img = cv2.imread(path)
    kernel = np.ones([5, 5], np.float32) / 32
    dst = cv2.filter2D(img, -1, kernel)
    print(dst.shape, img.shape)
    plt.subplot(121), plt.imshow(img), plt.title('original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

#这是由一个归一化卷积框完成的，他只是用卷积框覆盖区域所有像素的平均值来代替中心元素
def average():
    img = cv2.imread(path)
    dst = cv2.blur(img, (5, 5))
    # 高斯模糊：相对于blur，原来的求平均数变成求加权平均数，权就是方框里的值
    dst1 = cv2.GaussianBlur(img, (5, 5), 0)
    #中值模糊:就是用与卷积框对应像素的中值来替代中心像素的值，这个滤波器经常用来去除椒盐噪声
    dst2 = cv2.medianBlur(img,5)
    #双边滤波
    dst3 = cv2.bilateralFilter(img,9,75,75)
    cv2.imshow("img", img)
    cv2.imshow("blur", dst)
    cv2.imshow("gaussianBlur", dst1)
    cv2.imshow("medianBlur", dst2)
    cv2.imshow("bilateralFilter", dst3)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # conv2d()
    average()
