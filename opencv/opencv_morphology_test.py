import cv2
from util import file_utils, constant
import numpy as np
from matplotlib import pyplot as plt

'''
形态学转换
函数：cv2.erode(),cv2.dilate(),cv2.morphotogyEx()
基本操作为腐蚀和膨胀，他们的变体构成了开运算，闭运算，梯度等。
'''

def morphology_test():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    kernel = np.ones((5, 5), np.uint8)
    #腐蚀：第一个是原始图像，第二个被称为结构化元素或者核，
    ersion = cv2.erode(img, kernel, iterations=1)
    #膨胀：与腐蚀相反，与卷积核对应的原图像的像素值中只要有一个是1，中心元素的像素值就是1
    dilation = cv2.dilate(img, kernel, iterations=1)
    #开运算：先进行腐蚀再进行膨胀就叫做开运算。被用来去除噪音，函数可以使用cv2.morphologyEx()
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    #闭运算：先膨胀再腐蚀。被用来填充前景物体中的小洞，或者前景上的小黑点。
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    #形态学梯度:其实就是一幅图像膨胀与腐蚀的差别。结果看上去就像前景物体的轮廓。
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    #礼帽：原始图像与进行开运算之后得到的图像的差。
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    #黑帽：进行闭运算之后得到的图像与原始图像的差。
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

    dicts = {"img": img, "ersion": ersion, "dilation": dilation, "opening": opening, "closing": closing, "gradient": gradient, "tophat": tophat, "blackhat": blackhat}
    index = 0
    for x, y in dicts.items():
        index += 1
        plt.subplot(2, 4, index)
        y = cv2.cvtColor(y, cv2.COLOR_BGR2RGB)
        plt.imshow(y)
        plt.title(x)
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    morphology_test()