import tkinter as tk
from core.Archivo import Archivo
from core.Asiento import Asiento
from core.Sala import Sala
import time
root = tk.Tk()
root.geometry("800x700+300-10")
root.config(bg="#1e1e1e")
root.title("The Movie Theather")

def crear_asientos():
    return [[Asiento(h * 10 + l + 1, False) for l in range(10)] for h in range(8)]



sala1 = Sala(1, crear_asientos())
sala1_tarde = Sala(1, crear_asientos())
sala2 = Sala(2, crear_asientos())
sala2_tarde = Sala(2, crear_asientos())
sala3 = Sala(3, crear_asientos())
sala3_tarde = Sala(3, crear_asientos())
sala4 = Sala(4, crear_asientos())
sala4_tarde = Sala(4, crear_asientos())


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
    resumen_ventana.geometry("650x500+300+100")
    resumen_ventana.config(bg="#1e1e1e")

    canvas = tk.Canvas(resumen_ventana, bg="#1e1e1e")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(resumen_ventana, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    content_frame = tk.Frame(canvas, bg="#1e1e1e")
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    tk.Label(content_frame, text="Resumen de Salas", font=("Arial", 24, "bold"), bg="#1e1e1e", fg="white").pack(pady=20)
    contenedor = tk.Frame(content_frame, bg="#1e1e1e")
    contenedor.pack(padx=30, pady=10, fill="both", expand=True)

    for funcion in funciones:
        total, ganancia = funcion.sala.resumen_ocupacion()

        card = tk.Frame(contenedor, bg="#2a2a2a", padx=20, pady=15)
        card.pack(pady=10, fill="x")

        tk.Label(card, text=f"Sala {funcion.sala.numero} - {funcion.nombre}", font=("Arial", 16, "bold"), bg="#2a2a2a", fg="white", anchor="w").pack(fill="x")
        tk.Label(card, text=f"Horario: {funcion.hora}", font=("Arial", 12), bg="#2a2a2a", fg="white", anchor="w").pack(fill="x", pady=(5, 0))
        tk.Label(card, text=f"Asientos ocupados: {total}", font=("Arial", 12), bg="#2a2a2a", fg="#90ee90", anchor="w").pack(fill="x")
        tk.Label(card, text=f"Ganancias: ${ganancia:,}", font=("Arial", 12), bg="#2a2a2a", fg="#90ee90", anchor="w").pack(fill="x")

    tk.Button(content_frame, text="<< Cerrar", bg="gray", fg="white", width=15, command=resumen_ventana.destroy).pack(pady=20)

def ventana_archivo(funciones,archivo):
    archivo_ventana = tk.Toplevel()
    archivo_ventana.title("Actualizar Datos")
    archivo_ventana.geometry("650x500+300+100")
    archivo_ventana.config(bg="#1e1e1e")

    canvas = tk.Canvas(archivo_ventana, bg="#1e1e1e")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(archivo_ventana, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    content_frame = tk.Frame(canvas, bg="#1e1e1e")
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    tk.Label(content_frame, text="Actualizar Datos", font=("Arial", 24, "bold"), bg="#1e1e1e", fg="white").pack(pady=20)
    contenedor = tk.Frame(content_frame, bg="#1e1e1e")
    contenedor.pack(padx=30, pady=10, fill="both", expand=True)

    for funcion in funciones:
        crear_boton(contenedor, funcion, archivo)

    tk.Button(content_frame, text="<< Cerrar", bg="gray", fg="white", width=15, command=archivo_ventana.destroy).pack(pady=20)

def crear_boton(contenedor,funcion,archivo):
        card = tk.Frame(contenedor, bg="#2a2a2a", padx=20, pady=15)
        card.pack(pady=10, fill="x")

        tk.Label(card, text=f"Sala {funcion.sala.numero} - {funcion.nombre}", font=("Arial", 16, "bold"), bg="#2a2a2a", fg="white", anchor="w").pack(fill="x")
        tk.Label(card,text = "Cambiar nombre:",font=("Arial", 12, "bold"), bg="#2a2a2a", fg="#90ee90", anchor="w").pack(fill = "x")
        nombre_funcion = tk.Entry(card, bg = "#3a3a3a", fg = "#90ee90", font = ("Arial", 11),width=30)
        nombre_funcion.pack(fill = "x")
        nombre_funcion.insert(0,funcion.nombre)

        tk.Label(card,text = "Cambiar hora:",font=("Arial", 12, "bold"), bg="#2a2a2a", fg="#90ee90", anchor="w").pack(fill = "x")
        hora_funcion = tk.Entry(card,bg = "#3a3a3a", fg = "#90ee90", font = ("Arial", 11))
        hora_funcion.pack(fill = "x")
        hora_funcion.insert(0, funcion.hora)

        tk.Button(card, text="Guardar", bg="#147df5", fg="white", width=15, command=lambda: archivo.actualizar(funcion,nombre_funcion.get(),hora_funcion.get())).pack(pady=20)

def ventana_principal():
    
    def actualizar_Hora():
        for f in funciones:
            f.verificar_horario()
        etiqueta.config(text=time.strftime("Hora actual\n%H:%M"))
        content_frame.after(60000,actualizar_Hora)
    
    canvas = tk.Canvas(root, bg="#1e1e1e")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    content_frame = tk.Frame(canvas, bg="#1e1e1e")
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    tk.Label(content_frame, text="Cronograma de Funciones", font=("Arial", 20), bg="#1e1e1e", fg="white").pack(pady=20)

    etiqueta = tk.Label(content_frame, text="")

    etiqueta.configure(bg="#1e1e1e",fg="White",font=("Arial",20))
    etiqueta.pack(pady=10)
    
    
    archivo = Archivo("cartelera.txt", salas_dict)
    archivo.cargar()
    funciones = archivo.funciones
    actualizar_Hora()

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
    tk.Button(content_frame, text="Actualizar Informacion", command=lambda: ventana_archivo(funciones, archivo),
              bg="#147df5", fg="white", font=("Arial", 12), width=30).pack(pady=20)
    

ventana_principal()
root.mainloop()
