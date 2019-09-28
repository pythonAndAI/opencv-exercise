import os

def get_data_path(file_name, folder_name):
    basis_path = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(basis_path, "data", folder_name, file_name)
    return path

def re_path_content(file_name, folder_name):
    path = get_data_path(file_name, folder_name)
    if os.path.isfile(path):
        try:
            os.remove(path)
        except IOError:
            print("remove file", path, "fail!")
        else:
            print("remove file success!")
    else:
        print("file", path, "not exit!")

def write_content_file(contents, mode="w", fila_name="log"):
    path = get_data_path(fila_name + ".txt", "image")
    with open(path, mode) as f:
        for content in contents:
            try:
                f.write(str(content))
            except IOError:
                print("content writer fail...")

if __name__ == "__main__":
    re_path_content("video_1_1.mp4", "video")