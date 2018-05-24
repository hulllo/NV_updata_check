import os
import pro_qcn_xmlfile
import xml.etree.ElementTree as ET

def xml(file):
    nvupdatadic = {}
    tree = ET.parse(file)
    root = tree.getroot()
    for child in root:
        nvupdatadic[child.attrib['id']] = child.text

    nvdic = pro_qcn_xmlfile.qcn_xml()
                
    for key in nvupdatadic:
        try:
            if nvupdatadic[key] == nvdic[key]:
                print(key, 'OK')        
            else:
                print(key, 'NOK')
        except:
            print(key, 'NOK')
                
                
                
if __name__ == '__main__':
    path = "./nv_updata_list"
    files= os.listdir(path)
    file = files[0]
    filetype = file.split('.')[-1]
    file = "./nv_updata_list/"+file

    print(file)    
    if filetype == 'xml':
        xml(file)
    else: 
        print('no xml file')    
