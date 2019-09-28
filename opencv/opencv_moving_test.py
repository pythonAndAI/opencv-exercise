import cv2
import numpy as np

#用滑动条做调色板

def nothing(x):
    print(x)
    pass

#创建一个黑色图像
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')
#创建一个滑动条
#滑动条名字、窗口的名字、滑动条默认的位置、滑动条最大的值、回调函数，每次滑动都会调用回调函数，回调函数通常都会含有一个默认参数，就是滑动条的位置。
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
    #获取滑动条的参数
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    #print(r, g, b, s)
    if s == 0:
        img[:]=0
    else:
        img[:]=[r,g,b]
cv2.destroyAllWindows()