import os
import xml.dom.minidom
import shutil
import xml.etree.ElementTree as ET

dossier_ecriture = "DataBase/Rename"
dossier_lecture = "DataBase"

def traiter_dossier_complet () :
    for filename in os.listdir(os.getcwd() + "\\" + dossier_lecture) :
        fichier_a_lire = dossier_lecture + "\\" + filename
        print ( fichier_a_lire )
        traiter_fichier_unique ( fichier_a_lire )
    
def traiter_fichier_unique ( filename ) :
    liste_id = extraire_ids_fichier ( filename )
    if ( liste_id == -1 ) :
        return
    else :
        for i in range ( len ( liste_id ) ) :
            copier_fichier ( liste_id[i], filename )

def extraire_ids_fichier (filename):
    try :
        with open(filename,"r") as file :
            # Récupération du doc XML

            
            tree = ET.parse( file )
            root = tree.getroot()
            res = []
            ### Ca marche pas ici :/
            for child in root :
                print (child)
                if ( child.nodeName == "drugbank-id" ) :
                    res.append ( liste[i].firstChild.nodeValue )
            ### LA haut dessus :/      
            print ( res )
            return -1
            return res
            
            '''
            doc_xml = xml.dom.minidom.parse(file)
            root = doc_xml.documentElement'''
            
            
            #liste = root.getElementsByTagName("drugbank-id")
            
    except :
        if type(filename) != str : print("[ERROR!] Attention, filename = {} n'est pas une variable string".format(filename))
        else :  print("\n\n\n[ERROR!] Attention, le fichier {} n'existe pas\n\n\n".format(filename))
        return -1


def copier_fichier ( nom, fichier_a_copier ) :
    path_ecriture = dossier_ecriture + '/' + nom + '.xml'
    existe_deja = True
    try:
        f = open( path_ecriture )
    except IOError:
        existe_deja = False
        
    if ( existe_deja ) :
        None
    else :
        shutil.copyfile( fichier_a_copier, path_ecriture )

    
    
# Main
traiter_dossier_complet()
    
    

'''
import xml.etree.ElementTree as ET
 
tree = ET.parse('testpo.xml')
for element in tree.iter('drug'):
    # print (element.find('drugbank-id').text)
    '''
