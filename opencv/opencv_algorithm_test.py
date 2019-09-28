import cv2
import numpy as np
from util import constant, file_utils
#图像上的算术运算

#图像加法
def image_add():
    x = np.uint8([250])
    y = np.uint8([10])
    add_cv2 = cv2.add(x, y) #250+10=260>=255
    add_np = np.add(x, y)  #250+10=260%255=4
    add = x + y #250+10=260%255=4
    print("add_cv2 is:", add_cv2, "\nadd_np is:", add_np, "\nadd is:", add)

#图像混合-->这也是加法，不同的是两幅图像的权重不同，这会给人一种混合或者透明的感觉。图像混合的计算公式如下：
#g(x) = (1−α)f0 (x)+αf1 (x)
#通过修改α的值（0-->1）,可以实现很酷的混合。
def image_mix():
    path1 = file_utils.get_data_path(constant.naruto_image, "image")
    path2 = file_utils.get_data_path(constant.sasuke_image, "image")

    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    #裁剪img1和img2图像的大小
    img1 = img1[0:1021]
    img2 = img2[:, 0:681]
    #img1的shape必须等于img2的shape
    img3 = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
    dict_image = {"naruto_image":img1, "sasuke_image":img2, "add_image":img3}
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    for k,v in dict_image.items():
        cv2.setWindowTitle("image", k)
        cv2.imshow("image", v)
        cv2.waitKey()
    cv2.destroyAllWindows()

#按位计算-->这里包括按位操作有：AND，OR，NOT，XOR等，当我们提取图像的一部分，选择非矩形ROI时，会很有用（下章）。下面进行如何改变一幅图的特定区域。
def bitwise_operation():
    path1 = file_utils.get_data_path(constant.naruto_image, "image")
    path2 = file_utils.get_data_path(constant.spiralpill_image, "image")

    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    # 我想在左上角放置徽标，所以我创建了一个ROI
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]
    # 现在创建一个徽标掩码并创建其反转掩码
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #ret, dst = cv2.threshold(src, thresh, maxval, type)，参数分别是：输入图、阈值、当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值、二值化操作的类型
    #设置图像阈值，如下：大于175的设为255， 小于175的设为0
    ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
    #将二指图片的效果反转既黑色变白色，白色变黑色。
    mask_inv = cv2.bitwise_not(mask)
    # 现在，ROI中的徽标区域变黑
    # 取ROI中与mask中不为零的值对应的像素的值，其让值为0 。
    # 注意这里必须有mask=mask或者mask=mask_inv，其中mask=不能忽略
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
    # 取roi中与mask_inv中不为零的值对应的像素的值，其他值为0
    # 仅从徽标图像中获取徽标区域。
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

    # 在ROI中放置徽标并修改主图像
    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst

    cv2.imshow('res', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_add()
    # image_mix()
    # bitwise_operation()