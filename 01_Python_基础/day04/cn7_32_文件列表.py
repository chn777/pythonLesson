import os


def list_dir(dir_path):
    dir_list = os.listdir(dir_path)
    for file_name in dir_list:
        file_path = dir_path+"/"+file_name
        if os.path.isdir(file_path):
            list_dir(file_path)
        else:
            print(file_path)


list_dir('../')





