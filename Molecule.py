class Molecule :


    # Constructeur
    def __init__ ( self ) :
        self.nom = None
        self.smile = None
       
    # toString
    def __str__ ( self ) :
        s = ""
        s += "##### " + self.nom + " #####\n"
        s += self.smile + "\n"
        return s
    
    # Accesseur
    def setNom ( self, n ) :
        self.nom = n
        
    def setSmile ( self, s ) :
        self.smile = s
        
        
        
def testMolecule ( n, s ) :
    m = Molecule()
    m.setNom ( n )
    m.setSmile ( s )
    print ( m )
    
'''   
testMolecule ( "Alice", "Smile 1" )
testMolecule ( "Bob", "Smile 2" )
'''