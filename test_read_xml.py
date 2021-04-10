'''from xml.etree import ElementTree

xml_iter = ElementTree.iterparse("test.xml", events=('start', 'end'))

for event, elem in xml_iter :
    if event == 'start' :
        string = "<" + elem.tag + ">\n"
        string += elem.text.strip() +"\n"
    elif event == 'end' :
        string = "</" + elem.tag + ">\n"
        print ( string )'''
        
import xml.dom.minidom
 
doc_xml = xml.dom.minidom.parse("test.xml")
root = doc_xml.documentElement
liste = root.getElementsByTagName("food")
print ( "On a", len (liste), "element" )
for element in liste :
    print ( element.getElementsByTagName("name")[0].firstChild.nodeValue )