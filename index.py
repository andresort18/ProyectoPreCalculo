import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from sympy import symbols, sympify, factor, Poly, sqrt
import re

x, y, z = symbols('x y z')

def preprocesado(expresion: str) -> str:
    #Convierte 2x^2+3x en 2*x**2+3*x para sympy.
    expresion = expresion.strip().replace('^', '**')
    expresion = re.sub(r'(\d)(?=\s*[A-Za-z(])', r'\1*', expresion)
    expresion = re.sub(r'([A-Za-z\)])(?=\s*[A-Za-z(])', r'\1*', expresion)
    expresion = re.sub(r'([A-Za-z])(?=\s*\d)', r'\1*', expresion)
    return expresion

#validamos si cumple con los casos correspondientes
def esFactorComun(expr):
    f = factor(expr)
    return f != expr

def esDiferenciaCuadrados(expr):
    p = Poly(expr, x)
    if p.degree() == 2 and p.coeffs()[0] > 0:
        try:
            a, b, c = p.all_coeffs()
            return b == 0 and a > 0 and c < 0 and sqrt(-c/a).is_real
        except:
            return False
    return False

def esTrinomioCuadradoPerfecto(expr):
    p = Poly(expr, x)
    if p.degree() == 2:
        a, b, c = p.all_coeffs()
        return b**2 == 4*a*c
    return False

def esTrinomioSimple(expr):
    p = Poly(expr, x)
    return p.degree() == 2 and p.all_coeffs()[0] == 1

def esTrinomioGeneral(expr):
    p = Poly(expr, x)
    return p.degree() == 2 and p.all_coeffs()[0] != 1

def esCubos(expr):
    p = Poly(expr, x)
    if p.degree() == 3 and p.length() == 2:  
        a, c = p.all_coeffs()[0], p.all_coeffs()[-1]
        return (abs(a) == 1) and (round(abs(c)**(1/3))**3 == abs(c))
    return False


#Funcion principal que resuelve segun el caso de factorizacion
def resolverFactorizacion(caso):
    expresionTxt = caja.get("1.0", "end").strip()
    if not expresionTxt:  #mensaje de alerta si no se ingreaa una expresion
        messagebox.showwarning("Error", "Ingrese una expresión")
        return

    try:
        expresionPre = preprocesado(expresionTxt)
        expr = sympify(expresionPre)
        cumple = False

        if caso == "Factor Común":
            cumple = esFactorComun(expr)
        elif caso == "Diferencia De Cuadrados":
            cumple = esDiferenciaCuadrados(expr)
        elif caso == "Trinomio Cuadrado Perfecto":
            cumple = esTrinomioCuadradoPerfecto(expr)
        elif caso == "Trinomio x²+bx+c":
            cumple = esTrinomioSimple(expr)
        elif caso == "Trinomio ax²+bx+c":
            cumple = esTrinomioGeneral(expr)
        elif caso == "Suma o Diferencia de cubos":
            cumple = esCubos(expr)

        salida.config(state="normal")
        salida.delete("1.0", "end")
        salida.insert(tk.END,f"Caso seleccionado: {caso}\n"f"Expresion Ingresada: {expresionTxt}\n"f"Procesada: {expresionPre}\n\n")

        if cumple:
            salida.insert(tk.END, f"SI corresponde a: {caso}\n")
            salida.insert(tk.END, f"Fatorizad@: {factor(expr)}\n")
        else:
            salida.insert(tk.END, f"La expresión NO es del tipo: {caso}\n")
        salida.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", f"Expresión inválida:\n{e}")

#limpia nuestros espacios de textos
def reiniciar():
    caja.delete("1.0", "end")
    salida.config(state="normal")
    salida.delete("1.0", "end")
    salida.config(state="disabled")

def insertarFondo():
    img = Image.open("fondo.png").resize((1280, 730))
    imagenFondo = ImageTk.PhotoImage(img)
    labelFondo = tk.Label(main, image=imagenFondo)
    labelFondo.place(x=0, y=0, relwidth=1, relheight=1)
    labelFondo.image = imagenFondo

def menuPrincipal():
    menuOps = tk.Menu(main)
    main.config(menu=menuOps)
    menuFunciones = tk.Menu(menuOps, tearoff=0)
    imgSalir = Image.open("salir.png").resize((20, 20))
    imagenSalir = ImageTk.PhotoImage(imgSalir)

    menuFunciones.add_command(label="Salir", image=imagenSalir, compound="right", command=main.quit)
    menuFunciones.image = imagenSalir

    menuFunciones.add_command(label="reinicar", image=imagenSalir, compound="right", command=reiniciar)
    menuFunciones.image = imagenSalir

    menuOps.add_cascade(label="Funciones", menu=menuFunciones)

    

    tk.Label(main, text="Ingrese la expresión a factorizar:", font=("Arial", 20)).place(x=415, y=110)



def cajaTexto():
    c = tk.Text(main, height=1, width=35, font=("Arial", 20), bg="#ffffff", fg="#000000", padx=10, pady=10)
    c.place(x=350, y=150)
    return c

def salidaTexto():
    salida = tk.Text(main, height=10, width=90, font=("Arial", 14), bg="#f7f7f7")
    salida.place(x=130, y=220)
    salida.config(state="disabled")
    return salida

def boton(texto, x, y):
    tk.Button( main,text=texto,bg="#ffffff",width=30, height=2,command=lambda t=texto: resolverFactorizacion(t)).place(x=x, y=y)

def botonReiniciar(texto, x, y):
    tk.Button( main,text=texto,bg="#ffffff",width=30, height=2,command=reiniciar).place(x=x, y=y)

main = tk.Tk()
main.title("Casos de factorización")
main.geometry("1280x720")


insertarFondo()
menuPrincipal()
caja = cajaTexto()
salida = salidaTexto()

botonReiniciar("Limpiar", 1050, 50)
boton("Factor Común", 200, 500)
boton("Trinomio Cuadrado Perfecto", 200, 600)
boton("Diferencia De Cuadrados", 500, 500)
boton("Trinomio x²+bx+c", 500, 600)
boton("Trinomio ax²+bx+c", 800, 500)
boton("Suma o Diferencia de cubos", 800, 600)

main.mainloop()
