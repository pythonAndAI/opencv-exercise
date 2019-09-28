import cv2
from util import file_utils, constant
from matplotlib import pyplot as plt

'''
图像金字塔
一般情况下，我们要处理是一副具有固定分辨率的图像。但是特别情况下我们需要对同一个图像的不同分辨率的子图像进行处理，如查找图像中的某个目标，
如人脸，我们不知道目标在图像中的尺寸大小。这种情况下，我们需要创建一组图像，这些图像是具有不同分辨率的原始图像。我们把这组图像叫做图像金字塔。
就是同一图像的不同分辨率的子图集合。我们把最大的图像放在底部，最小的放在顶部，看起来就像一座金字塔。
有两类：高斯金字塔和拉普拉斯金字塔。
可以使用函数cv2.pyrDown()和cv2.pyrUp()构建图像金字塔。
cv2.pyrDown从一个高分辨率大尺寸的图像向上构建一个金字塔（尺寸变小，分辨率降低）
cv2.pyrUp从一个低分辨率小尺寸的图像向上构建一个金字塔（尺寸变大，但分辨率不会增加）
'''

def image_pyramid():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    image_dowm = cv2.pyrDown(img)
    image_up = cv2.pyrUp(img)

    #3个维度不同
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image_dowm = cv2.cvtColor(image_dowm, cv2.COLOR_BGR2RGB)
    image_up = cv2.cvtColor(image_up, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 3, 1); plt.imshow(img); plt.title("img"); plt.xticks([]); plt.yticks([])
    plt.subplot(1, 3, 2); plt.imshow(image_dowm); plt.title("image_dowm"); plt.xticks([]); plt.yticks([])
    plt.subplot(1, 3, 3); plt.imshow(image_up); plt.title("image_up"); plt.xticks([]); plt.yticks([])
    plt.show()


if __name__ == "__main__":
    image_pyramid()