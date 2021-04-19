from tkinter import *
from PIL import Image, ImageTk

# padx = 30, pady = 20; padding

# ----------------------
# Creación de la ventana
# ----------------------

ventana = Tk() # Ventana/contenedor
ventana.title("Centinela") # Título de la ventana
ventana.resizable(0, 0) # Desactiva el ajuste manual de la ventana
ventana.configure(background = "#20242F") # Color de fondo
ventana.iconbitmap("icono.ico") # Ícono de la ventana
ventana.overrideredirect(1) # Quitar controles de la ventana

# Posicionamiento de la ventana

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

x = (ancho_pantalla // 2) - 500
y = (alto_pantalla // 2) - 300

ventana.geometry("1000x600+" + str(x) + "+" + str(y)) # Dimensiones de la ventana

# ------------------------------
# Función para cerrar la ventana
# ------------------------------

def cerrarVentana(root): 
    root.destroy()

# ------------------------------
# Función para minimizar la ventana
# ------------------------------

def minimizarVentana(root): 
    root.withdraw()

# --------------------------------
# Creación de la sección principal
# --------------------------------

seccionSuperior = Frame(ventana) # Creación del frame
seccionSuperior.config(bg = "#2D3342") # Color del frame
seccionSuperior.place(x = 0, y = 0, width = 1000, height = 60) # Impresión dependiendo de las coordenadas

# Etiqueta para el título

tituloPrincipal = Label(seccionSuperior, text = "Centinela", fg = "#FFFFFF", bg = "#2D3342", font = ("Montserrat", 25)) # Creación de etiqueta
tituloPrincipal.place(x = 10, y = 8)

# Botón de minimizar

imgBtnMinimizar = ImageTk.PhotoImage(Image.open("TEC.JPG").resize((60, 60))) # Creación de la imagen del botón
btnMinimizar = Button(seccionSuperior, image = imgBtnMinimizar, border = 0, command = lambda: minimizarVentana(ventana)) # Creación del botón
btnMinimizar.place(x = 880, y = 8, width = 45, height = 45)  # Impresión del botón

# Botón de cerrar

imgBtnCerrar = ImageTk.PhotoImage(Image.open("TEC.JPG").resize((60, 60)))
btnCerrar = Button(seccionSuperior, image = imgBtnCerrar, border = 0, command = lambda: cerrarVentana(ventana))
btnCerrar.place(x = 940, y = 8, width = 45, height = 45)

# ----------------------------------------
# Creación de la sección lateral izquierda
# ----------------------------------------

seccionLateralI = Frame(ventana)
seccionLateralI.config(bg = "#C4C4C4")
seccionLateralI.place(x = 0, y = 60, width = 80, height = 540)

# Botones

imgBtn_1 = ImageTk.PhotoImage(Image.open("TEC.JPG").resize((60, 60)))
btnAnalizadorEmail = Button(seccionLateralI, image = imgBtn_1, border = 0)
btnAnalizadorEmail.place(x = 10, y = 10, width = 60, height = 60)

imgBtn_2 = ImageTk.PhotoImage(Image.open("TEC.JPG").resize((60, 60)))
btnAnalizadorURL = Button(seccionLateralI, image = imgBtn_2, border = 0)
btnAnalizadorURL.place(x = 10, y = 80, width = 60, height = 60)

imgBtn_3 = ImageTk.PhotoImage(Image.open("TEC.JPG").resize((60, 60)))
btnVerificadorPass = Button(seccionLateralI, image = imgBtn_3, border = 0)
btnVerificadorPass.place(x = 10, y = 150, width = 60, height = 60)

imgBtn_4 = ImageTk.PhotoImage(Image.open("TEC.JPG").resize((60, 60)))
btnVerificadorIntrusos = Button(seccionLateralI, image = imgBtn_4, border = 0)
btnVerificadorIntrusos.place(x = 10, y = 220, width = 60, height = 60)

ventana.mainloop() # Mantener ventana abierta