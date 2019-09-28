import cv2
from util import file_utils, constant
import numpy as np

#几何变换
path = file_utils.get_data_path(constant.naruto_image, "image")

#扩展缩放：
#只是改变图像的尺寸大小，cv2.resize()可以实现这个功能。在缩放时推荐cv2.INTER_AREA，在拓展时推荐cv2.INTER_CUBIC（慢）和cv2.INTER_LINEAR。
# 默认情况下所有改变图像尺寸大小的操作使用的是插值法都是cv2.INTER_LINEAR。
def extended_zoom():
    img = cv2.imread(path)
    #src：输入的像素，dsize：变换后的像素，fx：为沿水平轴的比例因子，fy：沿垂直轴的比例因子
    #如下缩放后shape在x,y方向上的大小是img的两倍
    res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    height, width = img.shape[:2]
    res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("res", res)
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

#平移：cv2.warpAffine()函数
def image_pan():
    img = cv2.imread(path)
    rows, cols = img.shape[:2]
    # 定义平移矩阵，需要是numpy的float32类型
    # x轴平移200，y轴平移100, 2*3矩阵
    M = np.float32([[1, 0, 200], [0, 1, 100]])
    # 用仿射变换实现平移
    img_s = cv2.warpAffine(img, M, (cols, rows), borderValue=(155, 150, 200))
    file_utils.write_content_file(img, mode="a")
    print(img.shape, img_s.shape)
    cv2.imshow("img_s", img_s)
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

#旋转：对一个图像旋转角度θ
def image_rotate():
    img = cv2.imread(path)
    rows, cols, _ = img.shape
    # 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
    # 可以通过设置旋转中心，缩放因子以及窗口大小来防止旋转后超出边界的问题。
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.6)
    # 第三个参数是输出图像的尺寸中心
    dst = cv2.warpAffine(img, M, (2 * cols, 2 * rows))
    print("M_shape", M.shape, "dst_shape", dst.shape, "image_shape", img.shape)
    cv2.imshow("dst", dst)
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

#仿射变换:在仿射变换中，原图中所有平行线在结果图像中同样平行。为创建这个矩阵，需要从原图像中找到三个点以及他们在输出图像中的位置，
# 然后cv2.getAffineTransForm()会创建一个2X3的矩阵。最后这个矩阵会被传给函数cv2.warpAffine()
def affine_trans():
    img = cv2.imread(path)
    rows, cols, ch = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    # 行，列，通道数
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (2 * cols, 2 * rows))
    print("M is:", M)
    print("M_shape", M.shape, "dst_shape", dst.shape, "image_shape", img.shape)
    cv2.imshow("dst", dst)
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

#透视变换:对于视角变换，我们需要一个3x3变换矩阵。在变换前后直线还是直线。需要在原图上找到4个点，
# 以及他们在输出图上对应的位置，这四个点中任意三个都不能共线，可以有函数cv2.getPerspectiveTransform()构建，然后这个矩阵传给函数cv2.warpPerspective()
def perspective_transformation():
    img = cv2.imread(path)
    rows, cols, ch = img.shape

    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (rows, cols))
    print("M is:", M)
    print("M_shape", M.shape, "dst_shape", dst.shape, "image_shape", img.shape)
    cv2.imshow("dst", dst)
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # extended_zoom()
    # image_pan()
    # image_rotate()
    # affine_trans()
    perspective_transformation()