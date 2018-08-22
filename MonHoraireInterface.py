import tkinter as tk

AffichagePrincipalHoraire = tk.Tk()
AffichagePrincipalHoraire.geometry("1600x800+0+0")
AffichagePrincipalHoraire.title('Planification de l\'horaire de XXX')

def affichageInterfaceAcceuilHoraire():
    horaireComplet()
    AffichagePrincipalHoraire.mainloop()

def horaireComplet():
    #Définition de la section du haut
    frame_Tops = tk.Frame(AffichagePrincipalHoraire,width = 160,bg="powder blue")
    frame_Tops.pack(side=tk.TOP)
    #définition de la section de d'affichage de l'horaire de gauche
    frame_HoraireCompletLeft = tk.Frame(AffichagePrincipalHoraire,width = 130, height= 70,bg="powder blue")
    frame_HoraireCompletLeft.pack(side=tk.LEFT)
    #définition de la section de d'affichage de l'horaire de droit
    frame_HoraireCompletRight = tk.Frame(AffichagePrincipalHoraire,width = 130, height= 70,bg="powder blue")
    frame_HoraireCompletRight.pack(side=tk.RIGHT)

    labelHoraireComplet = tk.Label(frame_Tops, text='Horaire complet',font=("Times", 50, 'bold'), fg="Steel Blue")
    labelHoraireComplet.grid(row=0,column=0)
    labelHoraireComplet.pack()
    #Instentiation du tableau
