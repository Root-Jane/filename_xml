import os
import os.path

path = r"L:\bin"  #根目录路径
xml_path = r"L:\Python\test14.xml"   #生成的xml文件储存路径

with open(xml_path,"w",encoding="utf-8") as f:  #创建xml文件 
    for root, dirs, files in os.walk(path):       #os.walk遍历根目录所有文件
        for filename in files:                    #打印出所有文件路径和名称
            filepath=root + '\\' + filename
            filepath=filepath.strip(path).replace("\\","/")
            filename_xml="<file path=\"" + filepath + "\"" + " filename=\"" + filepath +"\""+"/>" +"\n"   #生成xml格式文本
            f.write(filename_xml)