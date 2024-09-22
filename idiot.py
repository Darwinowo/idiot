import tkinter as tk
import random

def move_button():  # botón no
    ventana.update()
    max_x = ventana.winfo_width() - no_button.winfo_width()
    max_y = ventana.winfo_height() - no_button.winfo_height() - 120
    new_x = random.randint(0, max_x)
    new_y = random.randint(150, max_y)
    no_button.place(x=new_x, y=new_y)

def respuesta_si():  # botón sí
    etiqueta.config(text="¡Lo sabía! 😉", fg="black", font=("Arial", 20, "bold"))
    si_button.config(state=tk.DISABLED)
    no_button.config(state=tk.DISABLED)

def cerrar_ventana():  # mostrar advertencia en la misma ventana
    advertencia = tk.Toplevel(ventana)
    advertencia.geometry("350x150")  # Ajustar tamaño de la ventana
    advertencia.title("Advertencia")
    advertencia.configure(bg="#FFDD57")

    # Etiqueta con el mensaje de advertencia
    mensaje = tk.Label(advertencia, text="No puedes salir de aquí, pillín", font=("Arial", 14, "bold"), fg="black", bg="#FFDD57")
    mensaje.pack(pady=30)

    # Deshabilitar el cierre de la advertencia con la "X"
    advertencia.protocol("WM_DELETE_WINDOW", lambda: None)

ventana = tk.Tk()
ventana.title("Pregunta importante")
ventana.geometry("300x400")
ventana.configure(bg="#F0F0F0")

# Deshabilitar el cierre con la "X" y mostrar mensaje de advertencia en la ventana
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

etiqueta = tk.Label(ventana, text="¿Eres idiota?", font=("Arial", 24, "bold"), fg="black", bg="#F0F0F0")
etiqueta.pack(pady=40)

si_button = tk.Button(ventana, text="Sí", command=respuesta_si, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), width=10, height=2)
si_button.pack(pady=20)

no_button = tk.Button(ventana, text="No", command=move_button, bg="#F44336", fg="white", font=("Arial", 14, "bold"), width=10, height=2)
no_button.pack(pady=20)

ventana.mainloop()
