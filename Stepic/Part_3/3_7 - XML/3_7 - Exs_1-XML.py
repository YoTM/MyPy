from xml.etree import ElementTree as ET
from lxml import etree

# tree = ElementTree.parsestring(input())
data = input()
root = ET.fromstring(data)


print(root)
for child in root:
    print(child.tag, child.attrib)