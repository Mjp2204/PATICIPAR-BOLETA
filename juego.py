import sys
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import font
#from principal import iniciar_pygame

# Rutas de las imágenes
ruta_fondo = 'C:/Users/lenovo/Dropbox/CANDY_GAME/Imagenes/Menu2.png'
ruta_logo = 'C:/Users/lenovo/Dropbox/CANDY_GAME/Imagenes/logo.png'
ruta_juego = 'C:/Users/lenovo/Dropbox/CANDY_GAME/Imagenes/play.jpg'
ruta_fuente = 'ruta/a/8-bit Arcade In.ttf'  # Cambia esto a la ruta de tu fuente

# Inicializar la ventana de Tkinter
root = tk.Tk()
root.title('CANDY')
root.geometry('800x600')

# Cargar la imagen de fondo
try:
    image = Image.open(ruta_fondo)
    background_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen de fondo: {e}")
    sys.exit(1)

# Crear un canvas para poner la imagen de fondo
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")
canvas.image = background_image

# Cargar imagen de juego con filtro
try:
    fondo_jugar = Image.open(ruta_juego)
    distorted_image = fondo_jugar.filter(ImageFilter.BLUR)
    distorted_image_tk = ImageTk.PhotoImage(distorted_image)
except Exception as e:
    print(f"Error al cargar la imagen del juego: {e}")
    sys.exit(1)

# Cargar el logo
try:
    image = Image.open(ruta_logo)
    logo_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen del logo: {e}")
    sys.exit(1)

root.call('wm', 'iconphoto', root._w, logo_image)

# Registrar la fuente personalizada
try:
    custom_font = font.Font(family="8-bit Arcade In", size=16)
except Exception as e:
    print(f"Error al cargar la fuente personalizada: {e}")
    custom_font = ("Arial", 16)  # Fuente de respaldo

def jugar():
    boton_jugar.place_forget()
    boton_salir.place_forget()
    boton_iniciar.place_forget()
    # Mostrar los campos de entrada y botón en el canvas
    nombre_label.place(x=600, y=430)
    nombre_entry.place(x=600, y=450)
    boton_iniciar.place(x=600, y=470)

def iniciar_juego():
    nombre = nombre_entry.get()
    nombre_label.place_forget()
    nombre_entry.place_forget()
    boton_iniciar.place_forget()
    boton_salir.place_forget()
    boton_iniciar.place_forget()

    if nombre:
        # Limpiar el canvas
        canvas.delete("all")
        canvas.create_image(0, 0, image=distorted_image_tk, anchor="nw")
        mensaje = canvas.create_text(400, 300, text=f"Bienvenido, {nombre}! El juego comienza ahora.", fill="black", font=("8-bit Arcade In", 30))
        root.after(5000, lambda: canvas.delete(mensaje))
        root.after(5000, cuenta_regresiva)

def cuenta_regresiva():
    canvas.delete("contador")
    canvas.create_text(400, 300, text="START!", fill="black", font=("8-bit Arcade In", 80))
    #root.after(1000, lambda: [root.destroy(), iniciar_pygame()])

def salir():
    root.quit()

nombre_label = tk.Label(root, text="Ingrese su nombre:", font=custom_font)
nombre_entry = tk.Entry(root, font=custom_font)
boton_iniciar = tk.Button(root, text="Iniciar juego", command=iniciar_juego, font=custom_font, bd=3, fg="black", bg= "white", width=14, height=2)

boton_jugar = tk.Button(root, text="JUGAR", command=jugar, font=custom_font, bd=3, fg="black", bg="white", width=14, height=2)
boton_jugar.place(x=600, y=430)

boton_salir = tk.Button(root, text="SALIR", command=salir, font=custom_font, bd=3, fg="black", bg="white", width=14, height=2)
boton_salir.place(x=600, y=480)

root.mainloop()
