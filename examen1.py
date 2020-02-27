import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk 
from tkinter import Menu
from tkinter import messagebox as mBox
def funcionR():
    print("ssa")
def calificacion():
    calif=0
    mal=""
    if nombre.get() == "Instituto Tecnologico de Morelia":
        calif += 20
    else:
        mal+= "\nPregunta 1"
    if instituto.get() == "Tecnologico Nacional de Mexico":
        calif += 20
    else:
        mal+= "\nPregunta 2"
    if op.get() == "Sistemas Computacionales":
        calif += 20
    else:
        mal+= "\nPregunta 3"
    if op21.get() == "Soccer":
        calif += 20
    else :
        mal+= "\nPregunta 4"
    cali2=str(calif)
    if mal == "":
        mal="No hubo fallas"
    mBox.showinfo('Calificacion', "Calificacion: \n" +cali2+"\nErrores: "+mal)

    

ventana=tk.Tk()
ventana.title("Examen - Tecnologico")
texto1= ttk.Label(ventana, text="Examen 1. Tecnologico de Morelia")
texto1.grid(column=1,row=1,columnspan=3)
texto2= ttk.Label(ventana, text="Cual es el nombre completo de la institucion?: ")
texto2.grid(column=0,row=3)
texto3= ttk.Label(ventana, text="A que intitucion pertenece el ITM?: ")
texto3.grid(column=0,row=4)
nombre = tk.StringVar()
nombreCap = ttk.Entry(ventana, width=34, textvariable=nombre)
nombreCap.grid(column=1,row=3, columnspan=2)
instituto = tk.StringVar()
intiCap = ttk.Entry(ventana, width=34, textvariable=instituto)
intiCap.grid(column=1,row=4,columnspan=2)
texto4= ttk.Label(ventana, text="Ingenieria que imparte: ")
texto4.grid(column=0,row=5)
op = tk.StringVar()
radio1 = tk.Radiobutton(ventana, text="Sistemas Computacionales", variable=op,value="Sistemas Computacionales",command=funcionR)
radio1.grid(column=1,row=6,sticky=tk.W)
radio1.select()
radio2 = tk.Radiobutton(ventana, text="Gastronomia", variable=op,value="Gastronomia",command=funcionR)
radio2.grid(column=2,row=6,sticky=tk.W)
radio3 = tk.Radiobutton(ventana, text="Psicologia", variable=op,value="Psicologia",command=funcionR)
radio3.grid(column=3,row=6,sticky=tk.W)
texto5= ttk.Label(ventana, text="Deportes que difunde: ")
texto5.grid(column=0,row=7)
op21 = tk.StringVar()
radio4 = tk.Radiobutton(ventana, text="Futbol americano", variable=op21,value="Futbol americano",command=funcionR)
radio4.grid(column=1,row=8,sticky=tk.W)
radio4.select()
radio5 = tk.Radiobutton(ventana, text="Soccer", variable=op21,value="Soccer",command=funcionR)
radio5.grid(column=2,row=8,sticky=tk.W)
radio6 = tk.Radiobutton(ventana, text="Hokey", variable=op21,value="Hokey",command=funcionR)
radio6.grid(column=3,row=8,sticky=tk.W)
texto6= ttk.Label(ventana, text="Carreras que imparte: ")
texto6.grid(column=0,row=10)
op1 = tk.IntVar()
cas1 = tk.Checkbutton(ventana, text="Ingenierias", variable=op1)
cas1.grid(column=0,row=11, sticky=tk.W)
op2 = tk.IntVar()
cas2 = tk.Checkbutton(ventana, text="Sociales", variable=op2)
cas2.grid(column=1,row=11, sticky=tk.W)
op3 = tk.IntVar()
cas3 = tk.Checkbutton(ventana, text="Licenciaturas", variable=op3)
cas3.grid(column=2,row=11, sticky=tk.W)
op4 = tk.IntVar()
cas4 = tk.Checkbutton(ventana, text="Ciencias", variable=op4)
cas4.grid(column=3,row=11, sticky=tk.W)
op5 = tk.IntVar()
cas5 = tk.Checkbutton(ventana, text="Astronomia", variable=op5)
cas5.grid(column=4,row=11, sticky=tk.W)
accion = ttk.Button(ventana,text="Calificar", command = calificacion)
accion.grid(column=3,row=15)

ventana.mainloop() 