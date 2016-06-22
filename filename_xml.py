import os
import os.path

path = r"L:\bin"  #根目录路径
with open(r"L:\Python\test14.xml","w",encoding="utf-8") as f:  #创建xml文件 
	for root, dirs, files in os.walk(path):       #os.walk遍历根目录所有文件
		for filename in files:                    #打印出所有文件路径和名称
			filepath=root + '\\' + filename
			filepath1=filepath.replace("\\","/").strip('L:/bin')
			filepath1="<file path=\"" + filepath1 + "\"" + " filename=\"" + filepath1 +"\""+"/>" +"\n"
			f.write(filepath1)

	
	
   