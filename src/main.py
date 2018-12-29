import xml.etree.ElementTree as ET

i = 1

def print_xml(elm):
    global i 
    if elm.text != None:
        print(str(i) + '-' + elm.text)
        i = i+1
    elif elm.attrib == {'{http://www.w3.org/2001/XMLSchema-instance}nil': 'true'}:
        print(str(i) + '-' + "true")
        i = i+1
    for child in elm:
        print_xml(child)



tree = ET.parse("data/022901102_512244146_KGM_201812130754_1.xml")
root = tree.getroot()

print_xml(root)