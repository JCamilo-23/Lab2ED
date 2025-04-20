import tkinter as tk
from core.Funcion import Funcion
from core.Asiento import Asiento
from core.Sala import Sala
root = tk.Tk()
root.title("Gestión de Funciones")
root.geometry("800x500")
root.config(bg="#1e1e1e")

sala1 = Sala(1,[[Asiento(h * 9 + l + 1, False) for l in range(9)] for h in range(9)])
sala2 = Sala(2,[[Asiento(h * 9 + l + 1, False) for l in range(9)] for h in range(9)])
sala3 = Sala(3,[[Asiento(h * 9 + l + 1, False) for l in range(9)] for h in range(9)])

def ventana_principal():
    tk.Label(root, text="Gestión de Funciones", font=("Arial", 20), bg="#1e1e1e", fg="white").pack(pady=20)

    funciones = [ Funcion(sala1,"Harry Potter el mejor","14:00",True),
        Funcion(sala2, "Avatar", "16:00", True),
        Funcion(sala3,"Barbie","18:00", False)
    ]
    for i in range(len(funciones)):
        func(funciones[i])

def func(funcion):
        frame = tk.Frame(root, bg="#2a2a2a", pady=10)
        frame.pack(pady=10, padx=80, fill="x")

        tk.Label(frame, text=f"{funcion.sala.numero} | {funcion.pelicula} | {funcion.hora}", font=("Arial", 14), bg="#2a2a2a", fg="white").pack(side="left", padx=10)

        if funcion.estado:
            tk.Button(frame, text="Seleccionar >", bg="#147df5", fg="white", command=lambda: funcion.sala.ventana_sala(root)).pack(side="right", padx=10)
        else:
            tk.Label(frame, text="[Agotado]", fg="gray", bg="#2a2a2a").pack(side="right", padx=10)

ventana_principal()
root.mainloop()