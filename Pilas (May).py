import tkinter as tk
from tkinter import messagebox

# Pila para almacenar solicitudes
pila_solicitudes = []

def agregar_solicitud():
    solicitud = entrada_solicitud.get()
    if solicitud:
        pila_solicitudes.append(solicitud)
        entrada_solicitud.delete(0, tk.END)
        actualizar_estado()
    else:
        messagebox.showwarning("Entrada vacia", "Por favor, ingresa una solicitud.")

def procesar_solicitud():
    if pila_solicitudes:
        procesada = pila_solicitudes.pop()
        messagebox.showinfo("Solicitud procesada", f" Procesando: {procesada}")
        actualizar_estado()
    else:
        messagebox.showinfo("Sin solicitudes", "No hay solicitudes para procesar.")

def ver_ultima():
    if pila_solicitudes:
        messagebox.showinfo("Ultima solicitud", f" Ultima solicitud recibida: {pila_solicitudes[-1]}")
    else:
        messagebox.showinfo("Sin solicitudes", "No hay solicitudes en la pila.")

def verificar_vacia():
    if not pila_solicitudes:
        messagebox.showinfo("Pila vacia", "No hay solicitudes pendientes.")
    else:
        messagebox.showinfo("Solicitudes activas", "Hay solicitudes esperando procesamiento.")

def actualizar_estado():
    etiqueta_estado.config(text=f"Solicitudes pendientes: {len(pila_solicitudes)}")

# Interfaz grafica
ventana = tk.Tk()
ventana.title(" Procesador de Solicitudes Web (PILA)")
ventana.geometry("400x300")

# Entrada de solicitud
tk.Label(ventana, text="Descripcion de la solicitud:").pack(pady=5)
entrada_solicitud = tk.Entry(ventana, width=40)
entrada_solicitud.pack(pady=5)

# Botones
tk.Button(ventana, text=" Agregar solicitud", command=agregar_solicitud).pack(pady=5)
tk.Button(ventana, text=" Procesar solicitud", command=procesar_solicitud).pack(pady=5)
tk.Button(ventana, text=" Ver ultima solicitud", command=ver_ultima).pack(pady=5)
tk.Button(ventana, text=" ¿Pila vacia?", command=verificar_vacia).pack(pady=5)

# Estado
etiqueta_estado = tk.Label(ventana, text="Solicitudes pendientes: 0", font=("Arial", 12, "bold"))
etiqueta_estado.pack(pady=10)

ventana.mainloop()
