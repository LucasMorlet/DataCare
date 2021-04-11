import os
import shutil
import xml.dom.minidom

caractere_de_separation="\\"
caractere_csv = ';'
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
 
def traiter_fichier_unique_approved_commercial(filename):
    
    try :
        path_lecture= dossier_lecture + caractere_de_separation + filename+".xml"
        with open(path_lecture,"r") as file :

            # Racine du XML
            doc_xml = xml.dom.minidom.parse(file)
            root = doc_xml.documentElement

            # Etat : approved/unknow/other
            group = root.getElementsByTagName("group")
            result=[]
            etat = "unknown"
            for i in range( len( group ) ):
                result.append(group[i].firstChild.nodeValue)
            for i in range (len(result)) :
                etat = "other"
                elem=result[i]
                if elem =="approved":
                    etat = "approved"
                    break
                    
            # Commercial/Non Commercial

            marketDebut = root.getElementsByTagName("started-marketing-on")
            marketFin = root.getElementsByTagName("ended-marketing-on")
   
            if len(marketDebut)>0:
                commercial="commercial"
            else:
                commercial="non-commercial"

            
            resultat = ""
            resultat += filename 
            resultat += caractere_csv 
            resultat += etat 
            resultat += caractere_csv
            resultat += commercial
            return resultat
            
    except :
        if type(filename) != str : print("[ERROR!] Attention, filename = {} n'est pas une variable string".format(filename))
        else :  print("\n\n[ERROR!] Attention, le fichier {} n'existe pas\n\n".format(filename))
        return -1

def juge_fichiers(filename):
    liste_identifiants=traiter_doc_txt(filename)
    for i in range(len(liste_identifiants)):
        print ( "\nMolécule",i+1,":\n")
        res = traiter_fichier_unique_approved_commercial(liste_identifiants[i])
        print ( res )

def copie_fichiers(nomDepart):
    path_ecriture= dossier_ecriture + caractere_de_separation + nomDepart + ".xml"
    path_lecture= dossier_lecture + caractere_de_separation + nomDepart + ".xml"

    try :
        with open( path_ecriture, 'x' ) as fileArrive:
            with open ( path_lecture,'r' ) as fichierDepart:
                continu=True
                while (continu):
                    ligne = fichierDepart.readline()
                    if ligne :
                        fileArrive.write(ligne)
                    else:
                        continu = False
    except :
        print ( "Le fichier d'arrivée n'est aps bon" )
        return -1
            

        
        
        

#traiter_fichier_unique_approved("database-100.xml")
#traiter_doc_txt("identifiant.txt")
juge_fichiers("identifiant.txt")