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
 
xml = xml.dom.minidom.parse("test.xml")
liste = xml.getElementsByTagName("food")
print ( "On a", len (liste), "element" )
for element in liste :
    print ( element.getAttribute("price") )