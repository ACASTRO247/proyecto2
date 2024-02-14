import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random

# Base de datos de preguntas y enlaces a videos
preguntas = {
    "Cálculo Integral": [
        {
            "pregunta": "¿Cuál es la integral definida de x^2 desde 0 hasta 1?",
            "respuesta": "1/3",
            "video_link": "https://youtu.be/h_PAhWsgm-Y?si=TkJ8UKNPlsSKL5dY"
        },
        # Agrega más preguntas aquí

{
    "pregunta": "¿Cuál es la derivada de ln(x) con respecto a x?",

    "respuesta": "1/x",
    "video_link": "https://www.youtube.com/watch?v=abc123"
},


{
    "pregunta": "¿QUE SON LA ECUACIONES LINEALES?",
    "respuesta": "son 10"

},




    ],
    # Agrega más categorías de preguntas aquí
}

# Función para mostrar una pregunta aleatoria
def mostrar_pregunta():
    categoria = categoria_var.get()
    if categoria in preguntas:
        pregunta = random.choice(preguntas[categoria])
        pregunta_label.config(text=pregunta["pregunta"])
        enlace_video.config(text="Ver Video", command=lambda: abrir_video(pregunta["video_link"]))
    else:
        messagebox.showinfo("Error", "Categoría no encontrada")

# Función para verificar la respuesta ingresada
def verificar_respuesta():
    respuesta = respuesta_var.get()

    pregunta_actual = pregunta_label.cget("text")
    for categoria, lista_preguntas in preguntas.items():
        for pregunta in lista_preguntas:
            if pregunta["pregunta"] == pregunta_actual:
                if respuesta == pregunta["respuesta"]:
                    messagebox.showinfo("Correcto", "Respuesta Correcta")
                else:
                    messagebox.showerror("Incorrecto", "Respuesta Incorrecta")

# Función para abrir un enlace de video en el navegador web
import webbrowser
def abrir_video(enlace):

    webbrowser.open(enlace)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Preguntas de Matemáticas III")
ventana.geometry("1280x720")


#Cargar imagen fondo de pantalla
imagen = Image.open("C:\Users\ACER-A315\3D Objects\codigjose\geometry-1044090_1920.jpg")
#cambiar tamaño de la imagen
imagen = imagen.resize((200,200))

#covierte una imagen a un objeto PhotoImage
imagen_tk = ImageTk.PhotoImage(imagen)

#creacion de un widget Label para mostrar la imagen

label_imagen = tk.Label(ventana,image=imagen_tk)
label_imagen.pack()

# Variable para la categoría seleccionada
categoria_var = tk.StringVar(ventana)
categoria_var.set("Cálculo Integral")  # Categoría predeterminada

# Etiqueta para la pregunta
pregunta_label = tk.Label(ventana, text="", wraplength=400)
pregunta_label.pack(pady=10)

# Opción para seleccionar la categoría
categoria_option = tk.OptionMenu(ventana, categoria_var, *preguntas.keys())
categoria_option.pack()

# Botones para mostrar pregunta y verificar respuesta
mostrar_pregunta_btn = tk.Button(ventana, text="Mostrar Pregunta", command=mostrar_pregunta)
mostrar_pregunta_btn.pack()
respuesta_var = tk.StringVar()
respuesta_entry = tk.Entry(ventana, textvariable=respuesta_var)
respuesta_entry.pack()
verificar_btn = tk.Button(ventana, text="Verificar Respuesta", command=verificar_respuesta)
verificar_btn.pack()

# Botón para abrir enlace de video
enlace_video = tk.Button(ventana, text="", command=lambda: abrir_video(""))
enlace_video.pack()

# Ejecutar la aplicación
ventana.mainloop()
