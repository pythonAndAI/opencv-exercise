import cv2
from util import file_utils
from util import constant
#OpenCV图像的基本操作

path = file_utils.get_data_path(constant.naruto_image, "image")

#获取并修改像素值:读取一副图像，根据像素的行和列的坐标获取它的像素值，对于RGB图像而言，返回RGB的值，对于灰度图则返回灰度值
def get_modify_pixel():
    img = cv2.imread(path)
    px = img[100, 100]
    print(px)
    blue = img[100, 100, 0]
    print(blue)
    img[101, 101] = [255, 255, 255]
    print(img[101, 101])
    #img.item也可以获取像素值
    print(img.item(10, 10, 2))
    img.itemset((10, 10, 2), 100)
    print(img.item(10, 10, 2))

#获取图像的属性-->图像属性包括：行，列，通道，图像数据类型，像素数目等
def get_image_attribute():
    img = cv2.imread(path)
    print("shape is:", img.shape)
    #img.size可以返回图像的像素数目
    print("size is:", img.size)
    #返回图像的数据类型
    print("dtype is:", img.dtype)

#对图像的特定区域操作。ROI是使用numpy索引来获得的。
#例：选择球的部分并拷贝到其他区域
def image_roi():
    img = cv2.imread(path)
    #可以利用鼠标事件获取像素值，[480:550, 600:640]第0位为y轴坐标，第1位为x轴坐标
    ball = img[480:550, 600:640]
    img[415:485, 355:395] = ball
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyWindow("image")

#拆分及合并图像通道：有时需要对RGB三个通道分别操作，这就需要拆分RGB为单个通道。有时需要把独立的通道的图片合成一个RGB。
def splite_merge_image():
    img = cv2.imread(path)
    #拆分图像通道
    r, g, b = cv2.split(img)
    print("r is:", r, "\n g is:", g, "\n b is:", b)
    dicts = {"r_image": r, "g_image": g, "b_image": b}
    cv2.namedWindow("image")
    for k, y in dicts.items():
        cv2.setWindowTitle("image", k)
        cv2.imshow("image", y)
        cv2.waitKey()
    cv2.destroyWindow("image")

    #合并图像通道
    img2 = cv2.merge([r, g, b])
    cv2.namedWindow("image2")
    cv2.setWindowTitle("image2", "merge_image")
    cv2.imshow("image2", img2)
    cv2.waitKey()
    cv2.destroyWindow("image2")

    #假如想使所有红色通道值都为0，不必拆分再赋值，可以使用numpy索引，这样更快
    img3 = img2[:, :, 2]
    cv2.namedWindow("image3")
    #修改窗口的标题
    cv2.setWindowTitle("image3", "index_image")
    cv2.imshow("image3", img3)
    cv2.waitKey()
    cv2.destroyWindow("image3")

'''
为图像扩边（填充）->想为图像周围建一个边可以使用cv2.copyMakeBorder()函数。这经常在卷积运算或0填充时被用到
5.1：src输入图像
5.2：top,bottom,left,right对应边界的像素数目
5.3：borderType要添加哪种类型的边界：
5.3.1：cv2.BORDER_CONSTANT添加有颜色的常数值边界，还需要下一个参数（value）
5.3.2：cv2.BORDER_REFLIECT边界元素的镜像。例如：fedcba | abcdefgh | hgfedcb
5.3.3：cv2.BORDER_101或者cv2.BORDER_DEFAULT跟上面一样，但稍作改动，例如：gfedcb | abcdefgh | gfedcba
5.3.4：cv2.BORDER_REPLICATE复后一个元素。例如: aaaaaa| abcdefgh|hhhhhhh
5.3.5：cv2.BORDER_WRAP 不知怎么了, 就像样: cdefgh| abcdefgh|abcdefg
5.4：value边界颜色
'''
def image_filling():
    img = cv2.imread(path)
    value = [255, 0, 0]
    img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=value)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # get_modify_pixel()
    # get_image_attribute()
    # image_roi()
    # splite_merge_image()
    image_filling()