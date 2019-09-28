import cv2
from util import file_utils, constant
from matplotlib import pyplot as plt

'''
图像梯度原理：简单来说就是求导
OpenCV提供了三种不同的梯度滤波器，或者说高通滤波器：Sobel，Scharr和Laplacian。Sobel和Scharr是求一阶或二阶导数。
Scharr是对Sobel（使用小的卷积核求解梯度角度时）的优化，Laplacian是求二阶导数。
'''

def gradient_test():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    dicts = {"img": img, "laplacian": laplacian, "sobelx": sobelx, "sobely": sobely}
    index = 0
    for x, y in dicts.items():
        index += 1
        plt.subplot(2, 2, index)
        if x == "img":
            y = cv2.cvtColor(y, cv2.COLOR_BGR2RGB)
        plt.imshow(y)
        plt.title(x)
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    gradient_test()