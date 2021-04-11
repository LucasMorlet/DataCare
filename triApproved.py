import os
import shutil
import xml.dom.minidom
from datetime import datetime

caractere_de_separation="\\"
caractere_csv = ';'
dossier_lecture = "DataBase" + caractere_de_separation + "Rename"
dossier_ecriture = "DataBase" + caractere_de_separation + "Rename2"
csv_path = "Resultats" + caractere_de_separation

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
            commercial = "commercial"
            # TODO marketing ?

            
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
    csv = create_csv ( filename )
    if csv == None :
        return
    liste_identifiants=traiter_doc_txt(filename)
    for i in range(len(liste_identifiants)):
        res = traiter_fichier_unique_approved_commercial(liste_identifiants[i])
        write_in_csv ( res, csv )
        
    print ( extract_from_csv ( csv, True, False, False, True, True ) )

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
        print ( "Le fichier d'arrivée n'est pas bon" )
        return -1
        
def create_csv ( entree ) :
    filename = csv_path + entree + "_" + datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss") + ".csv"
    try :
        fichier = open( filename, 'x' )
        fichier.close()
        return filename
    except :
        print ( "Impossible de créer le fichier CSV :", filename )
        return None
            

def write_in_csv ( ligne, csv ) :
    try :
        fichier = open( csv, 'a' )
        fichier.write ( ligne + "\n" )
        fichier.close()
    except :
        print ( "Fail : Impossible d'écrire dans ", csv )

    
def extract_from_csv ( csv, app, unk, oth, com, notcom ) :
    data = []
    try :
        fichier = open( csv, 'r' )
        continu = True
        while (continu):
            ligne = fichier.readline()
            if ligne :
                ligne = ligne.split("\n")[0]
                data_line = ligne.split( caractere_csv )
                db_id = data_line[0]
                group = data_line[1]
                comm = data_line[2]
                
                ok_group = False
                if app == True and group == "approved" :
                    ok_group = True
                elif unk == True and group == "unknown" :
                    ok_group = True
                elif oth == True and group == "other" :
                    ok_group = True
                
                ok_comm = False
                if com == True and comm == "commercial" :
                    ok_comm = True
                elif notcom == True and comm == "not-commercial" :
                    ok_comm = True
                    
                if ( ok_group and ok_comm ) :
                    data.append ( db_id )
                
            else:
                continu = False
    except :
        print ( "Fail : Impossible de lire dans", csv )
    return data
        

#traiter_fichier_unique_approved("database-100.xml")
#traiter_doc_txt("identifiant.txt")
juge_fichiers("identifiant.txt")