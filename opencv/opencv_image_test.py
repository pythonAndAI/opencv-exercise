import cv2
from util import file_utils
from util.constant import naruto_image

#OpenCV的图像读取显示及保存
def cv2_read_write_image():
    img_path = file_utils.get_data_path(naruto_image, "image")
    #cv2.IMREAD_COLOR读入彩色图像 cv2.IMREAD_GRAYSCALE以灰度模式读入图像
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyWindow("image")

'''
cv2.waitKey(delay=None),delay默认值为0，单位为毫秒
当delay等于0或者不写时，函数则延时无限长，必须有键按下才继续执行。
当delay > 0 函数返回值为按下的键的ASCII码值，如果大于delay还没有按键，则会超时则返回-1。
ord('s')为获取一个按键的ASCII码值
'''
def cv2_waitkey_func_test():
    img_path = file_utils.get_data_path(naruto_image, "image")
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    cv2.imshow("image", img)
    k = cv2.waitKey()
    if k == 27:
        cv2.destroyWindow("image")
    elif k == ord('s'):
        cv2.imwrite(file_utils.get_data_path("cv2_test.jpg", "image"), img)
        file_utils.re_path_content("cv2_test.jpg", "image")
        cv2.destroyWindow("image")

if __name__ == "__main__":
    cv2_waitkey_func_test()