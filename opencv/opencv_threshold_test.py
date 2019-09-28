import cv2
from util import file_utils, constant
from matplotlib import pyplot as plt

path = file_utils.get_data_path(constant.naruto_image, "image")

#当像素值高于阀值时，我们给这个像素赋予一个新值（可能是白色），否则我们给它赋予另外一种颜色（也许是黑色）
#cv2.threshold():第一个参数是原图像，原图像应该是灰度图、第二个参数就是用来对像素值进行分类的阀值，第三个参数就是当像素值高于（或者小于）阀值时，应该被赋予新的像素值。
#不同的阈值方法：cv2.THRESH_BINARY、cv2.THRESH_BINARY_INV、cv2.THRESH_TRUNC、cv2.THRESH_TOZERO、cv2.THRESH_TOZERO_INV
def basis_threshold():
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    res, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
    titles_imgs = {'original image':img,'Binary':thresh1,'binary-inv':thresh2,'trunc':thresh3,'tozero':thresh4,'tozero-inv':thresh5}
    index = 0
    for k,v in titles_imgs.items():
        index += 1
        plt.subplot(2, 3, index), plt.imshow(v, 'gray'), plt.title(k)
        #去掉x,y轴坐标
        plt.xticks([]),plt.yticks([])
    plt.show()

#自适应阀值
#根据图像上的每一个小区域计算与其对应的阀值。因此在同一幅图像上的不同区域采用的是不同的阀值，从而使我们能在亮度不同的情况下得到更好的结果。
def adaptive_threshold():
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # 中值滤波
    img = cv2.medianBlur(img, 5)

    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # 11为block size，2为C值
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    titles_imgs = {'original image': img, 'global thresholding (v=127)': th1, 'Adaptive mean thresholding': th2, 'adaptive gaussian thresholding': th3}
    index = 0
    for k, v in titles_imgs.items():
        index += 1
        plt.subplot(2, 2, index), plt.imshow(v, 'gray'), plt.title(k)
        # 去掉x,y轴坐标
        plt.xticks([]), plt.yticks([])
    plt.show()

#Otsu's会得到图像最好的阈值
def Otsu_binarization():
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # (5,5)为高斯核的大小，0为标准差
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    # 阀值一定要设为0
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    images = [img, 0, th1,
              img, 0, th2,
              img, 0, th3]
    titles = ['original noisy image', 'histogram', 'global thresholding(v=127)',
              'original noisy image', 'histogram', "otsu's thresholding",
              'gaussian giltered image', 'histogram', "otus's thresholding"]
    # 这里使用了pyplot中画直方图的方法，plt.hist要注意的是他的参数是一维数组
    # 所以这里使用了（numpy）ravel方法，将多维数组转换成一维，也可以使用flatten方法
    for i in range(3):
        plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
        plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
        plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
        plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])

    plt.show()

if __name__ == "__main__":
    # basis_threshold()
    # adaptive_threshold()
    Otsu_binarization()