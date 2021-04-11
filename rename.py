import os
import xml.dom.minidom
import shutil
import xml.etree.ElementTree as ET

char_de_separation = '\\'

dossier_ecriture = "DataBase\\Rename"
dossier_lecture = "DataBase"

def traiter_dossier_complet () :
    for filename in os.listdir(os.getcwd() + char_de_separation + dossier_lecture) :
        fichier_a_lire = dossier_lecture + char_de_separation + filename
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

            tree = ET.parse( file )
            root = tree.getroot()
            res = []
            
            for child in root :
                if ( child.tag == "drugbank-id" ) :
                    res.append ( child.text )
                 
            return res
            
            #liste = root.getElementsByTagName("drugbank-id")
            
    except :
        if type(filename) != str : print("[ERROR!] Attention, filename = {} n'est pas une variable string".format(filename))
        else :  print("\n\n\n[ERROR!] Attention, le fichier {} n'existe pas\n\n\n".format(filename))
        return -1


def copier_fichier ( nom, fichier_a_copier ) :
    path_ecriture = dossier_ecriture + char_de_separation + nom + '.xml'
    existe_deja = True
    try:
        f = open( path_ecriture )
    except IOError:
        existe_deja = False
        
    if ( existe_deja ) :
        taille_ancien = os.stat(path_ecriture).st_size
        taille_nouveau = os.stat(fichier_a_copier).st_size
        if ( taille_nouveau > taille_ancien ) :
            shutil.copyfile( fichier_a_copier, path_ecriture )
    else :
        shutil.copyfile( fichier_a_copier, path_ecriture )

    
    
# Main
traiter_dossier_complet()