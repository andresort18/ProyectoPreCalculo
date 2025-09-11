import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk,Text,Button,ttksol


#creamos nuestra ventana, le damos nombre y tamaño
class interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Casos de factorizacion")
        self.ventana.geometry("1280x720")
        #Agregar una caja de texto para que sea la pantalla de la calculadora

def menuPrincipal():
    menuOps = tk.Menu(main)
    main.config(menu=menuOps)


    #primer submenu
    menuFunciones = tk.Menu(menuOps, tearoff=0)
    imgSalir = Image.open("salir.png")
    imgSalirResize = imgSalir.resize((20,20))
    imagenSalir = ImageTk.PhotoImage(imgSalirResize)
    menuFunciones.add_command(label="Salir", image=imagenSalir, compound="right", command=main.quit)
    menuFunciones.image = imagenSalir

    menuOps.add_cascade(label="Funciones",menu=menuFunciones)
    menuFunciones.add_separator()



#insertar imagen de fondo
def insertarFondo():
    
    img = Image.open("fondo.png")
    imgRedimensionada = img.resize((1280, 730))
    imagenFondo = ImageTk.PhotoImage(imgRedimensionada)

    #creamos el label para insertar el fondo
    labelFondo = tk.Label(main,image=imagenFondo)
    labelFondo.place(x=0, y=0, relwidth=1, relheight=1)

    labelFondo.image = imagenFondo

def cajaTexto():
    cajaTexto = tk.Text(main, height=1, width=30)
    cajaTexto.config(font=("Arial", 2), bg="#ffffff", fg="#000000", padx=10, pady=10)
    cajaTexto.place(x=350, y=50)



#botones    
def botonFactorComun():
    btnFactorComun = tk.Button(main, text="Factor Común", bg="#ffffff",command="")
    btnFactorComun.config(command="left",padx=10,width=30, height=2)
    btnFactorComun.place(x=50,y=550)


def botonTCP():
    btnTCP = tk.Button(main, text="Trinomio Cuadrado Perfecto", bg="#ffffff",command="")
    btnTCP.config(command="left",padx=10,width=30, height=2)
    btnTCP.place(x=50,y=650)


def botonDiferenciaCuadrados():
    btnDifCuadrados = tk.Button(main, text="Diferencia De Cuadrados", bg="#ffffff",command="")
    btnDifCuadrados.config(command="left",padx=10, width=30, height=2)
    btnDifCuadrados.place(x=350,y=550)

def botonTrinomioForma1():
    btnTrinomioForma1 = tk.Button(main, text="Trinomio x²+bx+c", bg="#ffffff",command="")
    btnTrinomioForma1.config(command="left",padx=10, width=30, height=2)
    btnTrinomioForma1.place(x=350,y=650)


def botonTrinomioForma2():
    btnTrinomioForma2 = tk.Button(main, text="Trinomio ax²+bx+c", bg="#ffffff",command="")
    btnTrinomioForma2.config(command="left",padx=10, width=30, height=2)
    btnTrinomioForma2.place(x=650,y=550)


def botonSumaDifCubos():
    btnSumaDifCubos = tk.Button(main, text="Suma o Diferencia de cubos", bg="#ffffff",command="")
    btnSumaDifCubos.config(command="left",padx=10, width=30, height=2)
    btnSumaDifCubos.place(x=650,y=650)










main = tk.Tk()

#llamada al fondo
insertarFondo()

calculadora = interfaz(main)


#llamada al menuPrincipal
menuPrincipal()

#llamada de botones
cajaTexto()
botonFactorComun()
botonTCP()
botonDiferenciaCuadrados()
botonTrinomioForma1()
botonTrinomioForma2()
botonSumaDifCubos()
main.mainloop()