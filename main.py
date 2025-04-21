import tkinter as tk
from core.Funcion import Funcion
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
    
    funciones = [ Funcion(sala1,"Harry Potter el mejor","14:00",True,"Lab2/images/f1.png"),
                  Funcion(sala1_tarde,"Shrek","17:00",True,"Lab2/images/f2.png"),
                  Funcion(sala2,"Avatar: El Camino del Agua","18:00",True,"Lab2/images/f3.png"),
                  Funcion(sala2_tarde, "Doctor Strange en el Multiverso de la Locura", "14:00", True,"Lab2/images/f4.png"),
                  Funcion(sala3,"Barbie","13:30", True,"Lab2/images/f5.png"),
                  Funcion(sala3_tarde,"Spider-Man: No Way Home","16:30", True,"Lab2/images/f6.png"),
                  Funcion(sala4,"Socrates'", "17:00",False,"Lab2/images/f1.png")
    ]
    pasar=True
    for i in range(len(funciones)):

        if funciones[i].sala.numero <5 and pasar:
            sala_label = tk.Label(content_frame, text=f"Sala {funciones[i].sala.numero}", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
            sala_label.pack(pady=(10, 5))
            pasar = not pasar
        else:
            pasar = not pasar
        frame = tk.Frame(content_frame, bg="#2a2a2a", pady=10)
        frame.pack(pady=10, padx=90, fill="x")
        funciones[i].ventana( frame, content_frame)
        
ventana_principal()
root.mainloop()