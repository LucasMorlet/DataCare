from tkinter import * 
import tkinter.font as font
from triApproved import *
 
fenetre = Tk()
# fenetre['bg']='#f9eac3' #jaunatre
#fenetre['bg']='#f7dfdb' #rosé
fenetre['bg']='#ace0e4' #tollens
fenetre.geometry("800x600")
fenetre.title('Recherche de Molécule')

app = BooleanVar()
unk = BooleanVar()
oth = BooleanVar()

com = BooleanVar()
notcom = BooleanVar()

csv = StringVar()
 
# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack( padx=100, pady=20)
 
# Entrée
value = StringVar() 
entree = Entry(Frame1, width=30)
entree.place(x=130, y= 70)
 
# frame 3 dans frame 1
Frame3 = Frame(Frame1, bg="white", borderwidth=2, relief=GROOVE) #bg="#0f056b"
Frame3.pack(padx=5, pady=5)
 
# frame principale
Frame4 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame4.pack(side=LEFT,padx=10, pady=10)
 
# Entrée
entree2 = Entry(Frame4, width=30)
 
''' Fonction dessineDisqueOrange à remplacer par la bonne fonction '''
 
def dessineDisqueOrange():
    dessineDisqueOrange = Label(fenetre, text="Texte par défaut", bg="yellow")
    dessineDisqueOrange = dessineDisqueOrange.pack()
 
def clic_bouton_go():
    csv.set ( transforme_csv ("identifiant.txt") )
    
    
def clic_bouton_refresh() :
    text.delete('1.0', END)
    liste = extract_from_csv ( csv.get(), app.get(), unk.get(), oth.get(), com.get(), notcom.get() )
    for i in range ( len ( liste ) ) :
        text.insert(END, liste[i])
        text.insert(END, "\n")

# Valider le nom de molécule grace a la touche entrée
def touche(event):
    t = event.keysym
    dessineDisqueOrange()
 
fenetre.bind('<Return>', touche)
 
# Button go
boutongo=Button(fenetre, text="GO", command = clic_bouton_go) #La aussi il faut changer la fonction
boutongo.place(x=680, y=90)
 
# checkbutton 1 Approved
#value = BooleanVar()
bouton1 = Checkbutton(fenetre, text="Approved", var=app)
bouton1.place(x=600, y=250)
 
# checkbutton 2 Unknow
bouton2 = Checkbutton(fenetre, text="Unknow", var=unk)
bouton2.place(x=600, y=300)
 
# checkbutton 3 All Others
bouton3 = Checkbutton(fenetre, text="All Others", var=oth)
bouton3.place(x=600, y=350)
 
# checkbutton 4 Commercial
bouton4 = Checkbutton(fenetre, text="Commercial", var=com)
bouton4.place(x=600, y=400)
 
# checkbutton 4 Non-Commercial
bouton5 = Checkbutton(fenetre, text="Non-Commercial", var=notcom)
bouton5.place(x=600, y=450)
 
# Boutton extraire
boutonextract=Button(fenetre, text="Extraire", command = clic_bouton_refresh)
boutonextract.place(x=550, y=520)
 
# Ajout de labels
Label(Frame1).pack(padx=150, pady=20)
Label(Frame3, text="Nom de la molécule",bg="white").pack(padx=150, pady=10)
# Label(Frame4, text="Base de donnée").pack(padx=150, pady=150)
 
f = font.Font(size = 12, weight = "bold")
label1 = Label(fenetre, text="FILTRES :", bg = '#ace0e4')
label1['font'] = f
label1.place(x = 600, y = 200)
 
f1 = font.Font(size = 9, weight = "bold")
label2 = Label(fenetre, text="Statut du médicament :", bg = '#ace0e4')
label2['font'] = f1
label2.place(x = 440, y = 250)
 
label3 = Label(fenetre, text="Marché :", bg = '#ace0e4')
label3['font'] = f1
label3.place(x = 520, y = 400)
 
# Boutton sortir
boutonsortir=Button(fenetre, text="Fermer", command=fenetre.quit)
boutonsortir.place(x=650, y=520)
 
# Zone de texte pour la base de donnée
text = Text(Frame4, height=26, width=50)
scroll = Scrollbar(Frame4, command=text.yview)
 
text.configure(yscrollcommand=scroll.set)
                   
text.tag_configure('groove', 
                   relief=GROOVE, 
                   borderwidth=2)
                   
text.tag_bind('bite', 
              '<1>', 
              lambda e, t=text: t.insert(END, "Text"))
 
text.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
 
print(value.get())
fenetre.mainloop()