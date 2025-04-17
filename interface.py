import tkinter as tk

root = tk.Tk()
root.title("Gestión de Funciones")
root.geometry("800x500")
root.config(bg="#1e1e1e")

def abrir_asientos():
    ventana_asientos.deiconify()

def ventana_principal():
    tk.Label(root, text="Gestión de Funciones", font=("Arial", 20), bg="#1e1e1e", fg="white").pack(pady=20)

    funciones = [
        ("Sala 1 | Harry Potter el mejor | 14:00", True),
        ("Sala 2 | Avatar | 16:00", True),
        ("Sala 3 | Barbie | 18:00", False)
    ]

    for texto, disponible in funciones:
        frame = tk.Frame(root, bg="#2a2a2a", pady=10)
        frame.pack(pady=10, padx=80, fill="x")

        tk.Label(frame, text=texto, font=("Arial", 14), bg="#2a2a2a", fg="white").pack(side="left", padx=10)

        if disponible:
            tk.Button(frame, text="Seleccionar >", bg="#147df5", fg="white", command=abrir_asientos).pack(side="right", padx=10)
        else:
            tk.Label(frame, text="[Agotado]", fg="gray", bg="#2a2a2a").pack(side="right", padx=10)

# Ventana emergente de asientos
ventana_asientos = tk.Toplevel(root)
ventana_asientos.withdraw()
ventana_asientos.title("Selección de Asientos")
ventana_asientos.geometry("600x800")
ventana_asientos.config(bg="#1e1e1e")

asientos = [[False for _ in range(9)] for _ in range(9)]
seleccionados = []
precio = 15000
texto_info = tk.StringVar()

def seleccionar_asiento(i, j, btn):
    asientos[i][j] = not asientos[i][j]
    id = f"F{i+1}C{j+1}"
    if asientos[i][j]:
        seleccionados.append(id)
        btn.config(bg="#147df5")
    else:
        seleccionados.remove(id)
        btn.config(bg="gray")
    texto_info.set(f"Asientos: {', '.join(seleccionados)}\nCosto: ${len(seleccionados) * precio}")

# Título
tk.Label(ventana_asientos, text="Selección de Asientos", font=("Arial", 18), bg="#1e1e1e", fg="white").pack(pady=10)

# Indicador de Pantalla
pantalla = tk.Frame(ventana_asientos, bg="#1e1e1e")
pantalla.pack(pady=(10, 0))

pantalla_label = tk.Label(
    pantalla,
    text="PANTALLA",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="white"
)
pantalla_label.pack()

barra_pantalla = tk.Frame(
    pantalla,
    bg="gray",
    height=4,
    width=300
)
barra_pantalla.pack(pady=2)

# asientos
grid_frame = tk.Frame(ventana_asientos, bg="#1e1e1e")
grid_frame.pack(pady=10)

btn_refs = [[None]*9 for _ in range(9)]  # Inicializar matriz de botones

for i in range(9):
    for j in range(9):
        b = tk.Button(grid_frame, text=f"{i*9 + j + 1}", bg="gray", fg="white", width=4, height=2)
        b.config(command=lambda i=i, j=j, btn=b: seleccionar_asiento(i, j, btn))
        btn_refs[i][j] = b
        b.grid(row=i, column=j, padx=5, pady=5)

# Info de selección
tk.Label(ventana_asientos, textvariable=texto_info, fg="white", bg="#1e1e1e", font=("Arial", 12)).pack(pady=10)

# Botones de acción
botones_frame = tk.Frame(ventana_asientos, bg="#1e1e1e")
botones_frame.pack()

tk.Button(botones_frame, text="Confirmar Compra", bg="#147df5", fg="white", width=20).pack(side="left", padx=10)
tk.Button(botones_frame, text="<< Volver", bg="gray", fg="white", width=15, command=ventana_asientos.withdraw).pack(side="right", padx=10)

ventana_principal()
root.mainloop()