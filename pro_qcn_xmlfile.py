import os
import xml.etree.ElementTree as ET

def qcn_xml():        #加载qcn_xmlfile文件夹内的nv xml文件
    path1=os.path.dirname(__file__)
    path = "./qcn_xmlfile/"
    files= os.listdir(path1 + path)
    file1 = files[0]
    nvdic = {}
    tree = ET.parse(path1 + path + file1)
        #提取出nv xml文件内的 [nv号:nv值]
    root = tree.getroot()
    for child in root:
        try:
            nvdic[child.attrib['id']] = child.text
        except KeyError:
           pass
    return nvdic       
