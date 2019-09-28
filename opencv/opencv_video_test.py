import cv2
from util import file_utils
from util.constant import video1_1_name, video1_name, vedio_param

#OpenCV视频操作
def get_video_camera():
    #VideoCapture()中参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
    cap = cv2.VideoCapture(0)
    #cap.isOpened()来检查是否成功初始化了，返回值是True，就没有问题，否则就要使用cap.open()。
    while True:
        #按帧读取视频，ret,frame是获cap.read()方法的两个返回值。其中ret是布尔值，如果读取帧是正确的则返回True，
        # 如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
        ret, frame = cap.read()
        #cvtColor表示色彩空间的转换
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("image", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
            break
    #释放摄像头
    cap.release()
    cv2.destroyAllWindows()

#读取本地视频
def get_video_path():
    path = file_utils.get_data_path(video1_name, "video")
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        #打开视频
        cap.open(video1_name)
        print("please open video.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            print("video read end...")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("image", gray)
        if cv2.waitKey(100) & 0xFF == ord('q'):  # 按q键退出
            break
    cap.release()
    cv2.destroyAllWindows()

def write_video_file():
    path = file_utils.get_data_path(video1_name, "video")
    cap = cv2.VideoCapture(path)
    #创建一个VideoWrite的对象，确定输出文件名，指定FourCC编码，播放频率和帧的大小，最后是isColor标签True为彩色。
    #FourCC是一个4字节码，用来确定视频的编码格式。DIVX , XVID , MJPG , X264 , WMV1 , WMV2
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    #获取原视频的高和宽
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #写入的视频的高和宽必须和原视频的高和宽一样，否则会打不开
    out = cv2.VideoWriter(file_utils.get_data_path(video1_1_name, "video"), fourcc, 20.0, (width, height))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            #图像翻转：1	水平翻转，0	垂直翻转， -1	水平垂直翻转
            frame = cv2.flip(frame, 0)
            #写入图片
            out.write(frame)
            cv2.imshow("image", frame)
            if cv2.waitKey(1) == ord("q"):
                break
        else:
            print("video write end...")
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    file_utils.re_path_content(video1_1_name, "video")

#https://www.cnblogs.com/bellumpara/p/8584226.html cap.get方法的取值
def get_vedio_param():
    path = file_utils.get_data_path(video1_name, "video")
    cap = cv2.VideoCapture(path)
    for k,v in vedio_param.items():
        print(v, "param is==>", cap.get(k))

if __name__ == "__main__":
    # get_video_path()
    # write_video_file()
    get_vedio_param()