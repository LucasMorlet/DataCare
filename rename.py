dossier_ecriture = "Rename"




import xml.etree.ElementTree as ET
 
tree = ET.parse('testpo.xml')
for element in tree.iter('drug'):
    # print (element.find('drugbank-id').text)
    rename = open (element.find('drugbank-id').text, "x")
