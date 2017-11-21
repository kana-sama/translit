from os import listdir, rename
from os.path import isfile, join
from transliterate import translit

path = "./test"

for file_name in listdir(path):
    if isfile(join(path, file_name)):
        new_file_name = translit(file_name, "ru", reversed=True)
        if file_name != new_file_name:
            print(file_name, ">>>", new_file_name)
            rename(join(path, file_name), join(path, new_file_name))
