
from tkinter import * 




from test import horairefunct


fenetre = Tk()
cadre = Frame(fenetre, borderwidth =10)
cadre.pack(fill = X)

message = Button(cadre, text="Horaire",font = ("Times",16), command = horairefunct)
message.pack(side = "top",fill=X)
message2 = Button(cadre, text="Budget",font = ("Times",16))
message2.pack(side="bottom",fill = X)

fenetre.mainloop()






