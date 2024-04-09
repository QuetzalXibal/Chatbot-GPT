import requests
import json
import tkinter as tk
from tkinter import ttk

API_KEY = "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"

def chatgpt_response(prompt):
    url = "https://api.openai.com/v1/engines/text-davinci-002/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    instruction = "Por favor, responde de manera útil a la siguiente pregunta:"
    data = {
        "prompt": f"{instruction} {prompt}",
        "max_tokens": 100,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        return response_json["choices"][0]["text"].strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Lo siento, hubo un error al obtener una respuesta. Por favor, revisa la consola para más detalles."

def enviar_mensaje(event=None):
    mensaje_usuario = campo_texto.get()
    campo_texto.delete(0, tk.END)
    respuesta = chatgpt_response(mensaje_usuario)

    respuesta_lineas = respuesta.split('\n')
    chat.insert(tk.END, f"Usuario: {mensaje_usuario}\n")
    for linea in respuesta_lineas:
        chat.insert(tk.END, f"ChatGPT: {linea}\n")
    chat.yview(tk.END)

def cambiar_tema(*args):
    if tema_var.get() == 'Oscuro':
        colores_oscuros()
    else:
        colores_claros()

def colores_oscuros():
    ventana.configure(bg='#2c2c2c')
    marco_chat.configure(bg='#2c2c2c')
    chat.configure(fg='#ffffff', bg='#2c2c2c', selectbackground='#2c2c2c', highlightbackground='#2c2c2c')
    campo_texto.configure(fg='#ffffff', bg='#404040', insertbackground='white')
    boton_enviar.configure(fg='#ffffff', bg='#404040', activebackground='#505050', activeforeground='#ffffff')

def colores_claros():
    ventana.configure(bg='white')
    marco_chat.configure(bg='white')
    chat.configure(fg='#000000', bg='white', selectbackground='white', highlightbackground='white')
    campo_texto.configure(fg='#000000', bg='#ffffff', insertbackground='black')
    boton_enviar.configure(fg='#000000', bg='#ffffff', activebackground='#ffffff', activeforeground='#000000')

def ventana_opacidad():
    def ajustar_opacidad(opacidad):
        ventana.attributes("-alpha", float(opacidad))

    top = tk.Toplevel(ventana)
    top.title("Ajustar opacidad")
    top.geometry("250x100")
    scale = tk.Scale(top, from_=0.1, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, command=ajustar_opacidad)
    scale.set(ventana.attributes("-alpha"))
    scale.pack(expand=True, fill=tk.BOTH)

def enviar_mensaje(event=None):
    mensaje_usuario = campo_texto.get()
    campo_texto.delete(0, tk.END)
    respuesta = chatgpt_response(mensaje_usuario)

    respuesta_lineas = respuesta.split('\n')
    chat.insert(tk.END, f"Usuario: {mensaje_usuario}\n")
    for linea in respuesta_lineas:
        chat.insert(tk.END, f"ChatGPT: {linea}\n")
    chat.yview(tk.END)

def cambiar_tema(*args):
    if tema_var.get() == 'Oscuro':
        colores_oscuros()
    else:
        colores_claros()

def colores_oscuros():
    ventana.configure(bg='#2c2c2c')
    marco_chat.configure(bg='#2c2c2c')
    chat.configure(fg='#ffffff', bg='#2c2c2c', selectbackground='#2c2c2c', highlightbackground='#2c2c2c')
    campo_texto.configure(fg='#ffffff', bg='#404040', insertbackground='white')
    boton_enviar.configure(fg='#ffffff', bg='#404040', activebackground='#505050', activeforeground='#ffffff')

def colores_claros():
    ventana.configure(bg='white')
    marco_chat.configure(bg='white')
    chat.configure(fg='#000000', bg='white', selectbackground='white', highlightbackground='white')
    campo_texto.configure(fg='#000000', bg='#ffffff', insertbackground='black')
    boton_enviar.configure(fg='#000000', bg='#ffffff', activebackground='#ffffff', activeforeground='#000000')

ventana = tk.Tk()
ventana.title("ChatGPT")

menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)

# Definir el menú de tema
tema_var = tk.StringVar(value='Oscuro')
tema_menu = tk.Menu(menu_bar, tearoff=0)
tema_menu.add_radiobutton(label="Oscuro", variable=tema_var, value="Oscuro", command=cambiar_tema)
tema_menu.add_radiobutton(label="Claro", variable=tema_var, value="Claro", command=cambiar_tema)
menu_bar.add_cascade(label="Tema", menu=tema_menu)

# Definir el menú de transparencia
transparencia_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Transparencia", menu=transparencia_menu)
transparencia_menu.add_command(label="Ajustar transparencia", command=ventana_opacidad)

# Definir el marco del chat y los widgets relacionados
marco_chat = tk.Frame(ventana)
scrollbar_vertical = tk.Scrollbar(marco_chat)
scrollbar_horizontal = tk.Scrollbar(marco_chat, orient=tk.HORIZONTAL)

chat = tk.Listbox(marco_chat, height=30, width=120, yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
scrollbar_vertical.config(command=chat.yview)
scrollbar_horizontal.config(command=chat.xview)

scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
chat.pack(side=tk.LEFT, fill=tk.BOTH)
chat.pack()
marco_chat.pack()

# Definir el campo de texto y el botón de enviar
campo_texto = tk.Entry(ventana)
campo_texto.bind("<Return>", enviar_mensaje)
campo_texto.pack()

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack()

cambiar_tema()

ventana.mainloop()
