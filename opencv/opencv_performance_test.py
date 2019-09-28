import cv2
from util import file_utils, constant

'''
程序性能检测及优化
效率优化技术
有些技术和编程方法可以我们大的发挥 Python 和 Numpy 的威力。 我们仅仅提一下相关的你可以接查找更多细信息。我们 的的一点是先用简单的方式实现你的算法结果正确当结 果正确后再使用上的提到的方法找到程序的瓶来优化它。

尽免使用循环尤其双层三层循环它们天生就是慢的。
算法中尽使用向操作因为 Numpy 和 OpenCV 对向操作 了优化。
利用缓存一致性。
没有必的就不复制数组。使用图来代替复制。数组复制是常浪源的。
'''

'''
使用OpenCV检测程序效率
cv2.getTickCount函数返回从参考点到这个函数被执行的时钟数。在一个函数执行前后都调用它，可以得到这个函数的执行时间。
cv2.getTickFrequency返回时钟频率，或者说每秒钟的时钟数
'''
def check_program_effectiveness():
    path = file_utils.get_data_path(constant.naruto_image, "image")
    img = cv2.imread(path)
    e1 = cv2.getTickCount()
    for i in range(5, 49, 2):
        #中值滤波
        img = cv2.medianBlur(img, i)
    e2 = cv2.getTickCount()
    #转换单位为秒
    time = (e2 - e1) / cv2.getTickFrequency()
    print(time)

#OpenCV中的默认优化-->cv2.useOptimized()来查看优化是否被开启，cv2.setUesOptimized()来开启优化
def default_optimization():
    print("检测是否开启：", cv2.useOptimized())
    cv2.setUseOptimized(False)
    print("检测是否开启：", cv2.useOptimized())

if __name__ == "__main__":
    # check_program_effectiveness()
    default_optimization()