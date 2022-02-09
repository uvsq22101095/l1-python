import tkinter as tk 
CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500


root = tk.Tk()

root.title(" Mon Dessin ")
#création des widgets

boutton_couleur = tk.Button(root, text="Choisir Une Couleur",bg="gray", fg="black", padx=20, font=("Times", "20"))
boutton_cercle = tk.Button(root, text="cercle",bg="gray", fg="black", padx=20, font=("Times", "20"))
boutton_carré = tk.Button(root, text="carré" ,bg="gray", fg="black", padx=20, font=("Times", "20"))
boutton_croix = tk.Button(root, text="croix" ,bg="gray", fg="black", padx=20, font=("Times", "20"))

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="black", bd=10, relief="raised")

boutton_couleur.grid(column=1, row=0)
boutton_cercle.grid(column=0, row=1)
boutton_carré.grid(column=0, row=2)
boutton_croix.grid(column=0, row=3)
canvas.grid(column=1, rowspan=3)

root.mainloop()