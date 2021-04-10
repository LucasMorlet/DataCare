import xml.dom.minidom

# Récupération du doc XML
doc_xml = xml.dom.minidom.parse("../DataBase/database.xml")
root = doc_xml.documentElement


liste = root.getElementsByTagName("drug")
print ( "On a", len (liste), "element" )
for element in liste :
    print ( element.getElementsByTagName("name")[0].firstChild.nodeValue )
    
    
    
# Récupération du contenu du dossier (pour chaque fichier)
def traite_dossier ():
    None


# Extrait l'id et créer un fichier de ce nom dans le dossier Rename
def range_fichier () :
    None