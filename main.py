import tkinter as tk
from tkinter import ttk, messagebox

# Configuración inicial
meta_diaria = 8
vasos_tomados = 0
intervalo_minutos = 60


def registrar_vaso(event=None):
    global vasos_tomados

    if vasos_tomados < meta_diaria:
        vasos_tomados += 1

    actualizar_pantalla()


def actualizar_pantalla():
    progreso = min(vasos_tomados / meta_diaria * 100, 100)

    etiqueta_vasos.config(
        text=f"Vasos tomados: {vasos_tomados}/{meta_diaria}"
    )
    barra_progreso["value"] = progreso
    etiqueta_porcentaje.config(text=f"Progreso: {progreso:.0f}%")

    if vasos_tomados >= meta_diaria:
        etiqueta_estado.config(text="¡Meta diaria alcanzada! 🎉")
    else:
        etiqueta_estado.config(text="¡Sigue hidratándote! 💧")


def recordar_agua():
    if vasos_tomados < meta_diaria:
        messagebox.showinfo(
            "Recordatorio de agua 💧",
            "¡Es hora de beber un vaso de agua!"
        )

    ventana.after(intervalo_minutos * 60 * 1000, recordar_agua)


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Recordatorio de Agua")
ventana.geometry("360x330")
ventana.resizable(False, False)
ventana.configure(bg="#EAF8FF")

# Título
titulo = tk.Label(
    ventana,
    text="💧 ¡Hora de hidratarte!",
    font=("Arial", 18, "bold"),
    bg="#EAF8FF",
    fg="#087EBC"
)
titulo.pack(pady=15)

# Meta diaria
etiqueta_meta = tk.Label(
    ventana,
    text=f"Meta diaria: {meta_diaria} vasos",
    font=("Arial", 12),
    bg="#EAF8FF"
)
etiqueta_meta.pack(pady=5)

# Cantidad de vasos
etiqueta_vasos = tk.Label(
    ventana,
    text=f"Vasos tomados: 0/{meta_diaria}",
    font=("Arial", 14, "bold"),
    bg="#EAF8FF"
)
etiqueta_vasos.pack(pady=10)

# Barra de progreso
barra_progreso = ttk.Progressbar(
    ventana,
    length=280,
    mode="determinate",
    maximum=100
)
barra_progreso.pack(pady=5)

etiqueta_porcentaje = tk.Label(
    ventana,
    text="Progreso: 0%",
    font=("Arial", 11),
    bg="#EAF8FF"
)
etiqueta_porcentaje.pack(pady=5)

# Estado
etiqueta_estado = tk.Label(
    ventana,
    text="¡Empieza a tomar agua!",
    font=("Arial", 11),
    bg="#EAF8FF",
    fg="#087EBC"
)
etiqueta_estado.pack(pady=5)

# Botón B
boton_b = tk.Button(
    ventana,
    text="B - Registrar vaso 🥤",
    font=("Arial", 12, "bold"),
    bg="#20A4F3",
    fg="white",
    activebackground="#087EBC",
    command=registrar_vaso,
    width=22
)
boton_b.pack(pady=12)

# También permite registrar un vaso pulsando la tecla B
ventana.bind("<KeyPress-b>", registrar_vaso)
ventana.bind("<KeyPress-B>", registrar_vaso)

# Iniciar recordatorios periódicos
ventana.after(intervalo_minutos * 60 * 1000, recordar_agua)

# Ejecutar aplicación
ventana.mainloop()

