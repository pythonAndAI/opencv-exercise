import numpy as np
import cv2

#OpenCV中的绘图函数，窗口左上角默认为原点，向右为x轴，向下为y轴，

def get_img_data():
    return np.zeros((512,512,3),np.uint8)

def create_window(img):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image", 1000, 1000) #定义frame的大小
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyWindow("image")

#画线
def draw_line(img):
    #像素、线段的第一个点(起点)、线段的第二个点(终点)、线颜色、线厚度
    cv2.line(img,(0,0),(260,260),(255,0,0),10)
    create_window(img)

#画矩阵
def draw_rectangle(img):
    cv2.rectangle(img,(100,0),(380,128),(0,255,0),3)
    create_window(img)

#画圆
def draw_circle(img):
    #像素、圆心、半径、颜色、厚度
    cv2.circle(img, (260, 200), 63, (0, 0, 255), -1)  # 圆，-1为向内填充，实心圆
    create_window(img)

#画椭圆
def draw_ellipse(img):
    # 像素、圆心、椭圆主轴尺寸的一半、椭圆旋转角度、椭圆圆弧的起始角、椭圆圆弧的结束角、颜色、厚度
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)
    create_window(img)

#画多边形
def draw_polylines(img):

    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    # 这里reshape的第一个参数为-1，表明这一维度的长度是根据后面的维度计算出来的
    # 像素、多边形曲线数组、关闭标志，指示绘制的折线是否关闭、颜色、厚度
    cv2.polylines(img, [pts], False, (0, 255, 255))
    # 注意第三个参数若是False，我们得到的是不闭合的线
    create_window(img)

#画多边形
def draw_putText(img):
    font = cv2.FONT_HERSHEY_SIMPLEX
    #像素、要绘制的文本字符串、图片文本字符串的左下角、字体类型、尺寸因子，值越大文字越大、文本颜色、厚度
    #不能写入中文，写入中文可以参考https://blog.csdn.net/m0_37606112/article/details/78511381
    cv2.putText(img, '哈娃子', (10, 300), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
    create_window(img)

if __name__ == "__main__":
    img = get_img_data()
    # draw_line(img)
    # draw_rectangle(img)
    # draw_circle(img)
    # draw_ellipse(img)
    # draw_polylines(img)
    draw_putText(img)