import os
import os.path

path = r"C:\Users\Root\Documents\GitHub\xml"  #根目录路径
for root, dirs, files in os.walk(path):       #os.walk遍历根目录所有文件
    for filename in files:                    #打印出所有文件路径和名称
        print(root + '\\' + filename)