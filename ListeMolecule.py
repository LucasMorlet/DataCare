from Molecule import *
from datetime import datetime

#test git

class ListeMolecule :

    def __init__ ( self, n ) :
        self.nom = n
        self.liste = []
        
    def __str__ ( self ) :
        s = "--------------- " + self.nom + " ---------------\n\n"
        for i in range ( len ( self.liste ) ) :
            s += str ( self.liste[i] ) + "\n"
            
        return s
        
    # Ajouter une molécule à la liste
    # TODO : changer la structure de données vers une table de hachage
    def addMolecule ( self, m ) :
        self.liste.append(m)
        
    # Ecriture dans un fichier
    def print_in_file ( self ) :
        filename = "Resultats/" + self.nom + "_" + datetime.now().strftime("%Y_%m_%d_%Hh%M") + ".txt"
        file = open(filename, "x")
        file.write ( str ( self ) )
        file.close()
        
# Méthode de test       
def testListe ( ) :
    L = ListeMolecule ( "Molecule_test" )
    m = Molecule()
    m.setNom ( "Alice" )
    m.setSmile ( "Smile Alice" )
    L.addMolecule ( m )
    m2 = Molecule()
    m2.setNom ( "Bob" )
    m2.setSmile ( "Smile Bob" )
    L.addMolecule ( m2 )
    print(L)
    L.print_in_file()
    
    
testListe()