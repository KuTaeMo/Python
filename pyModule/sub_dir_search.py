import os


def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        name = os.path.splitext(full_filename)
        print("ext : ", ext)
        print("name : ", name)
        if ext == '.py':
            print("fullName : ", full_filename)
        print("==========================================")


search("C:/doit")
