import cv2
from util import file_utils, constant
from matplotlib import pyplot as plt

'''
Canny边缘检测：cv2.Canny()
cv2.Canny（）第一个参数是输入图像，第二和第三个分别是minVal和maxVal。第三个参数设置用来计算图像梯度的Sobel卷积核的大小，默认值为3。
最后一个参数是L2gradient，它可以用来设定求梯度大小的方程。如果设为True，就睡使用我们上面提到过的方程，否则使用方程：代替，默认值为False。
'''

def canny_edge():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    edges = cv2.Canny(img, 100, 200)

    plt.subplot(1, 2, 1); plt.imshow(img); plt.title("img"); plt.xticks([]); plt.yticks([])
    plt.subplot(1, 2, 2); plt.imshow(edges); plt.title("edges"); plt.xticks([]); plt.yticks([])
    plt.show()

if __name__ == "__main__":
    canny_edge()
