import cv2
from util import file_utils
from util import constant

'''
OpenCV处理鼠标事件
理论主要就是两点，
一是监控鼠标操作，鼠标点击，移动，松开，然后通过mouse_event识别判断出那一种鼠标的操作，根据不同的操作然后进行处理，
二是在主函数中加入鼠标的回调函数，将鼠标操作与程序的窗口绑定。
'''

#查看所有被支持的鼠标事件
def find_all_event():
    events = [ i for i in dir(cv2) if 'EVENT' in i ]
    for event in events:
        print(event)
    print("共有", len(events), "种，分别是:", events)

'''
setMouseCallback(windowName, onMouse, param=None)
windowName:windows视窗名称，对名为winname的视窗进行鼠标监控,onMouse:鼠标响应处理函数，监听鼠标的点击，移动，松开，判断鼠标的操作类型，并进行响应的函数处理
onMouse:on_mouse(int event,int x,int y,int flags,void *ustc)回调函数
    event：鼠标操作时间的整数代号，共12种
    x,y：代表鼠标位于窗口的（x，y）坐标位置，窗口左上角默认为原点，向右为x轴，向下为y轴
    flags:代表鼠标的拖拽事件，以及键盘鼠标联合事件，共32种
event代号：
    EVENT_MOUSEMOVE	0	滑动
    EVENT_LBUTTONDOWN	1	左键点击
    EVENT_RBUTTONDOWN	2	右键点击
    EVENT_MBUTTONDOWN	3	中间点击
    EVENT_LBUTTONUP	4	左键释放
    EVENT_RBUTTONUP	5	右键释放
    EVENT_MBUTTONUP	6	中间释放
    EVENT_LBUTTONDBLCLK	7	左键双击
    EVENT_RBUTTONDBLCLK	8	右键双击
    EVENT_MBUTTONDBLCLK	9	中间双击
    EVENT_MOUSEWHEEL 10    滚动条向上，flags>0。向下，flags<0
    EVENT_MOUSEHWHEEL = 11		滚动条向左，flags>0。向右，flags<0
flags代号：
    EVENT_FLAG_LBUTTON 1      左鍵拖曳  
    EVENT_FLAG_RBUTTON 2      右鍵拖曳  
    EVENT_FLAG_MBUTTON 4      中鍵拖曳  
    EVENT_FLAG_CTRLKEY 8      (8~15)按Ctrl不放事件  
    EVENT_FLAG_SHIFTKEY 16    (16~31)按Shift不放事件  
    EVENT_FLAG_ALTKEY 32      (32~39)按Alt不放事件 
'''
def mouse_test_case():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("image", mouse_event)
    while True:
        cv2.imshow("image", img)
        if cv2.waitKey(1) == ord("s"):
            break
    cv2.destroyWindow("image")

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("111")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("22")
    elif flags ==cv2.EVENT_FLAG_RBUTTON:
        print("33")
    elif event == cv2.EVENT_MOUSEMOVE:
        print("44")
    elif flags == cv2.EVENT_FLAG_CTRLKEY:
        print("55")
    else:
        print("===")

if __name__ == "__main__":
    mouse_test_case()
