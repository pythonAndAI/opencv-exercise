import cv2
from util import file_utils, constant
import numpy as np

#颜色空间转换:涉及函数cv2.cvtColor(),cv2.inRange()

#常用的类型转换为：BGR↔Gray 和 BGR↔HSV
# 对于BGR↔Gray的转换，我们使用的ﬂag就是cv2.COLOR_BGR2GRAY。
#同样对于BGR↔HSV的转换我们用的ﬂag就是cv2.COLOR_BGR2HSV
#在 OpenCV 的 HSV 格式中，H（色彩/色度）的取值范围是 [0，179]， S（饱和度）的取值范围 [0，255]，V（亮度）的取值范围 [0，255]。但是不同的软件使用的值可能不同。
# 所以当你拿 OpenCV 的 HSV 值与其他软件的 HSV 值对比时，一定要记得归一化。
def print_all_color():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    cv2.namedWindow("image")
    colors = [x for x in dir(cv2) if x.startswith("COLOR_")]
    print(len(colors))
    dicts = {"COLOR_BGR2GRAY":cv2.COLOR_BGR2GRAY, "COLOR_BGR2HSV": cv2.COLOR_BGR2HSV}
    for k, y in dicts.items():
        cv2.setWindowTitle("image", k)
        img1 = cv2.cvtColor(img, y)
        cv2.imshow("image", img1)
        cv2.waitKey()
    cv2.destroyAllWindows()

'''
物体跟踪
现在我们知怎样将一幅图像从 BGR 换到 HSV 了，我们可以利用 一点来提取带有某个特定色的物体。在 HSV 颜色空间中要比在 BGR 空间中更容易表示一个特定颜色。
在我们的程序中，我们提取的是一个蓝色的物体。下就是就是我们做的几步：
• 从视频中获取每一帧图像
• 将图像换到 HSV 空间
• 设置 HSV 阀值到蓝色范围。
• 获取蓝色物体，当然我们可以做其他任何我们想做的事
'''
def object_tracking():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    # 转换到HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 设定蓝色的阀值
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # 根据阀值构建掩模->把lower_red~upper_red的范围值变为225，其他范围变为0吧
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 对原图和掩模进行位运算
    res = cv2.bitwise_and(img, img, mask=mask)
    # 显示图像
    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.waitKey()
    # 关闭窗口
    cv2.destroyAllWindows()

#怎样找到要跟踪对象的HSV值-->现在需要传入的参数是RGB的值而不是一幅图。例如要找到绿色的HSV值
def get_HSV_value():
    #现在你可以分别用 [H-100，100，100] 和 [H+100，255，255] 做上下阀值
    green = np.uint8([[[0, 255, 0]]])
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    print(hsv_green)

if __name__ == "__main__":
    # print_all_color()
    # object_tracking()
    get_HSV_value()