from tkinter import *

AffichagePrincipalHoraire = Tk()
AffichagePrincipalHoraire.geometry('500x500')
AffichagePrincipalHoraire.title('Planification de l\'horaire de XXX')

def AffichageInterfaceAcceuilHoraire():
    horaireComplet()
    AffichagePrincipalHoraire.mainloop()

def horaireComplet():
    labelHoraireComplet = Label(AffichagePrincipalHoraire, text='Horaire complet',font=("Helvetica", 16))
    labelHoraireComplet.pack()
    #Instentiation du tableau