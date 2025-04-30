import tkinter as tk
from core.Archivo import Archivo
from core.Asiento import Asiento
from core.Sala import Sala
root = tk.Tk()
root.geometry("800x700+300-10")
root.config(bg="#1e1e1e")

sala1 = Sala(1,[[Asiento(h * 10 + l + 1, False) for l in range(10)] for h in range(8)])
sala1_tarde =Sala(1,[[Asiento(h * 10 + l + 1, False) for l in range(10)] for h in range(8)])
sala2 = Sala(2,[[Asiento(h * 10 + l + 1, False) for l in range(10)] for h in range(8)])
sala2_tarde =Sala(2,[[Asiento(h * 10 + l + 1, False) for l in range(10)] for h in range(8)])
sala3 = Sala(3,[[Asiento(h * 10 + l + 1, False) for l in range(10)] for h in range(8)])
sala3_tarde =Sala(3,[[Asiento(h * 10 + l + 1, False) for l in range(10)] for h in range(8)])
sala4 = Sala(4,[[Asiento(h * 10 + l + 1, False) for l in range(10)] for h in range(8)])
sala4_tarde = Sala(4,[[Asiento(h * 10 + l + 1, False) for l in range(10)] for h in range(8)])

salas_dict = {
    "1": sala1,
    "1t": sala1_tarde,
    "2": sala2,
    "2t": sala2_tarde,
    "3": sala3,
    "3t": sala3_tarde,
    "4": sala4,
    "4t": sala4_tarde
}

def mostrar_resumen(funciones):
    resumen_ventana = tk.Toplevel()
    resumen_ventana.title("Resumen de Salas")
    resumen_ventana.geometry("600x500+300+100")
    resumen_ventana.config(bg="#1e1e1e")

    tk.Label(resumen_ventana, text="Resumen de Salas", font=("Arial", 24, "bold"), bg="#1e1e1e", fg="white").pack(pady=20)

    contenedor = tk.Frame(resumen_ventana, bg="#1e1e1e")
    contenedor.pack(padx=30, pady=10, fill="both", expand=True)

    for funcion in funciones:
        total, ganancia = funcion.sala.resumen_ocupacion()

        card = tk.Frame(contenedor, bg="#2a2a2a", padx=20, pady=15)
        card.pack(pady=10, fill="x")

        tk.Label(card, text=f"Sala {funcion.sala.numero} - {funcion.nombre}", font=("Arial", 16, "bold"), bg="#2a2a2a", fg="white", anchor="w").pack(fill="x")
        tk.Label(card, text=f"Horario: {funcion.hora}", font=("Arial", 12), bg="#2a2a2a", fg="white", anchor="w").pack(fill="x", pady=(5, 0))
        tk.Label(card, text=f"Asientos ocupados: {total}", font=("Arial", 12), bg="#2a2a2a", fg="#90ee90", anchor="w").pack(fill="x")
        tk.Label(card, text=f"Ganancias: ${ganancia:,}", font=("Arial", 12), bg="#2a2a2a", fg="#90ee90", anchor="w").pack(fill="x")
    
    # Botón cerrar
    tk.Button(resumen_ventana, text="<< Cerrar", bg="gray", fg="white", width=15, command=resumen_ventana.destroy).pack(pady=20)


def ventana_principal():
    canvas = tk.Canvas(root, bg="#1e1e1e")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    content_frame = tk.Frame(canvas, bg="#1e1e1e")
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    tk.Label(content_frame, text="Cronograma de Funciones", font=("Arial", 20), bg="#1e1e1e", fg="white").pack(pady=20)

    # ✅ Cargar funciones desde archivo (crea nuevas salas por función)
    archivo = Archivo("Lab2/cartelera.txt",salas_dict)
    archivo.cargar()
    funciones = archivo.funciones

    # ✅ Agrupar por sala visualmente
    funciones_agrupadas = {}
    for funcion in funciones:
        num_sala = funcion.sala.numero
        funciones_agrupadas.setdefault(num_sala, []).append(funcion)

    for sala_num, lista_funciones in funciones_agrupadas.items():
        sala_label = tk.Label(content_frame, text=f"Sala {sala_num}", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
        sala_label.pack(pady=(10, 5))

        for funcion in lista_funciones:
            frame = tk.Frame(content_frame, bg="#2a2a2a", pady=10)
            frame.pack(pady=10, padx=90, fill="x")
            funcion.ventana(frame, content_frame)
    
    tk.Button(content_frame, text="📊 Ver resumen de salas", command=lambda: mostrar_resumen(funciones),
          bg="#147df5", fg="white", font=("Arial", 12), width=30).pack(pady=20)



ventana_principal()
root.mainloop()
