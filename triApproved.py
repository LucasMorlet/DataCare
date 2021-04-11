import os
import shutil
import xml.dom.minidom

fichierTrie=""
caractere_de_separation="\\"
dossier_lecture = "DataBase\\Rename"
dossier_ecriture = "DataBase\\Rename2"

def traiter_doc_txt(filename):
    try :
        with open(filename,"r") as file :
            data=[]
            continu=True
            while (continu):
                ligne=file.readline()
                if ligne :
                    ligne=ligne.split("\n")[0]
                    data.append(ligne)
                else:
                    continu = False
            return data

    except :
        if type(filename) != str : print("[ERROR!] Attention, filename = {} n'est pas une variable string".format(filename))
        else :  print("\n\n[ERROR!] Attention, le fichier doc {} n'existe pas\n\n".format(filename))
        return -1
 
def traiter_fichier_unique_approved(filename):
    try :
        path_lecture= dossier_lecture + caractere_de_separation + filename+".xml"
        with open(path_lecture,"r") as file :

            doc_xml = xml.dom.minidom.parse(file)
            root = doc_xml.documentElement

            group = root.getElementsByTagName("group")
            #print ( "On a", len (group), "element :" )
            result=[]
            # parcours le tag "group"
            for i in range( len( group ) ):
                result.append(group[i].firstChild.nodeValue)
            print (result)
            for i in range (len(result)) :
                elem=result[i]
                print ("elelel",elem)
                if elem =="approved":
                    copie_fichiers(file)
                    print("je copie le fichier")

            
    except :
        if type(filename) != str : print("[ERROR!] Attention, filename = {} n'est pas une variable string".format(filename))
        else :  print("\n\n[ERROR!] Attention, le fichier {} n'existe pas\n\n".format(filename))
        return -1

def juge_fichiers(filename):
    liste_identifiants=traiter_doc_txt(filename)
    print(liste_identifiants)
    for i in range(len(liste_identifiants)):
        traiter_fichier_unique_approved(liste_identifiants[i])

def copie_fichiers(nomDepart):
    path_ecriture= dossier_ecriture + caractere_de_separation + nomDepart
    path_lecture= dossier_lecture + caractere_de_separation + nomDepart

    with open( path_ecriture, 'x' ) as fileArrive:
        with open (path_lecture,'r') as fichierDepart:
            continu=True
            while (continu):
                ligne=file.readline()
                if ligne :
                    fileArrive.write(ligne)
                else:
                    continu = False
            

        
        
        

#traiter_fichier_unique_approved("database-100.xml")
#traiter_doc_txt("identifiant.txt")
juge_fichiers("identifiant.txt")