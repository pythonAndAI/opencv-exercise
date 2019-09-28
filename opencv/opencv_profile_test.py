import cv2
from util import file_utils, constant
from matplotlib import pyplot as plt

'''
1.OpenCV中的轮廓
轮廓可以简单认为成连续的点（连着边界）连在一起的曲线，具有相同的颜色或者灰度。轮廓在形状分析和物体的检测和识别中很有用。
2.如何在一个二值图像中查找轮廓。
函数cv2.findContours()有三个参数，第一个是输入图像，第二个是轮廓检索模式，第三个是轮廓近似方法。返回值有三个，第一个是轮廓，第二个是（轮廓的）层析结构
3.怎样绘制轮廓
函数cv2.drawContours()可以被用来绘制轮廓。它可以根据你提供的边界点绘制任何形状。它的第一个参数是原始图像，第二个参数是轮廓，一个python列表，
第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设置为-1时绘制所有轮廓）
'''
def profile():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    imag = cv2.drawContours(img, contours, 3, (0, 255, 0), 3)
    cv2.imshow('img', img)
    cv2.imshow('imgray', imgray)
    cv2.imshow('imag', imag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def contour_feature():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    #1.图像的矩可以帮助我们计算图像的质心，面积等。函数cv2.moments()会将计算得到的矩以一个字典的形式返回。
    M = cv2.moments(cnt)
    #2.轮廓面积:可以使用函数cv2.contourArea()计算得到，也可以用矩（0阶矩），M['m00']。
    area = cv2.contourArea(cnt)
    #3.轮廓周长:也被称为弧长。可以使用函数cv2.arcLength()计算得到。这个函数的第二参数可以用来指定对象的形状是闭合的（True），还是打开的（一条曲线）。
    perimeter = cv2.arcLength(cnt, True)
    #4.轮廓近似:假设我们要在一幅图像中查找一个矩形，但是由于图像的种种原因我们不能得到一个完美的矩形，而是一个“坏形状”，现在就可以使用这个函数来近似这个形状，
    # 第二个参数是epsilon，它是从原始轮廓到近似轮廓的最大距离，它是一个准确度参数。
    epsilon = 0.1 * perimeter
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    #5.凸包:函数cv2.convexHull()可以用来检测一个曲线是否具有凸性缺陷，并能纠正缺陷。
    hull = cv2.convexHull(cnt)
    #6.凸性检测:函数cv2.isContourConvex()可以检测一个曲线是不是凸的。它只能返回True或者False。
    k=cv2.isContourConvex(cnt)
    #7.边界矩形:直边界矩形，一个直矩形，没有旋转。不会考虑对象是否旋转
    x, y, w, h = cv2.boundingRect(cnt)
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #8.最小外接圆:函数cv2.minEnclosingCircle(),可以帮我们找到一个对象的外接圆。它是所有能够包括对象的圆中面积最小的一个。
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    img3 = cv2.circle(img, center, radius, (0, 255, 0), 2)
    #9.椭圆拟合:使用函数cv2.ellipse()，返回值其实就是旋转边界矩形的内切圆。
    ellipse = cv2.fitEllipse(cnt)
    img4 = cv2.ellipse(img,ellipse,(0,255,0),2)
    #10.直线拟合:可以根据一组点拟合出一条直线，同样我们也可以为图像中的白色点拟合出一条直线。
    rows, cols = img.shape[:2]
    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    lefty = int((x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    img5 = cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
    contents = {"图像的矩": M, "轮廓面积": area, "轮廓周长": perimeter, "轮廓近似": approx, "凸包": hull, "凸性检测": k}
    images = {"image": img,"rectangle": img2,"circle": img3,"ellipse": img4,"line": img5}
    for k, v in contents.items():
        print(k + "===>", v)
    index = 0
    for k, v in images.items():
        index += 1
        v_img = cv2.cvtColor(v, cv2.COLOR_BGR2RGB)
        plt.subplot(2, 3, index); plt.imshow(v_img); plt.title(k); plt.xticks([]); plt.yticks([])
    plt.show()

if __name__ == "__main__":
    # profile()
    contour_feature()
