import os

import pro_excel
import pro_xml

#加载nv_updata_list文件夹内的nv更新表
path = "/nv_updata_list/"
path1=os.path.dirname(__file__)

files= os.listdir(path1 + path)
for file in files:
    print('\n'+file)
    filetype = file.split('.')[-1]
    file = path1 + path + file
    if filetype == 'xlsx' or filetype == 'xls':
        pro_excel.excel(file)
    elif filetype == 'xml':
        pro_xml.xml(file)

input('按回车键退出')
