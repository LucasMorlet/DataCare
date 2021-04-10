import xml.dom.minidom

# Récupération du doc XML
doc_xml = xml.dom.minidom.parse("test.xml")
root = doc_xml.documentElement


"""liste = root.getElementsByTagName("drug")
print ( "On a", len (liste), "element" )
for element in liste :
    print ( element.getElementsByTagName("name")[0].firstChild.nodeValue )"""
    
    
    
# Récupération du contenu du dossier (pour chaque fichier)
def extraire_id_fichier (filename):
    try :
        with open(filename,"r") as file :
            # Récupération du doc XML

            doc_xml = xml.dom.minidom.parse(file)
            root = doc_xml.documentElement

            liste = root.getElementsByTagName("drugbank-id")
            print ( "On a", len (liste), "element :" )
            for i in range(len(liste)):
                return liste[i].firstChild.nodeValue
    except :
        if type(filename) != str : print("[ERROR!] Attention, filename = {} n'est pas une variable string".format(filename))
        else :  print("\n\n\n[ERROR!] Attention, le fichier {} n'existe pas\n\n\n".format(filename))
        return -1

# Extrait l'id et créer un fichier de ce nom dans le dossier Rename
def traite_fichier () :
    None

print(traite_dossier ("test.xml"))