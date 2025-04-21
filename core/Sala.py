from core.Asiento import Asiento
import tkinter as tk

    
class Sala:
    def __init__(self,numero,asientos):
        self.numero = numero
        self.asientos = asientos
        self.botones = [[None]*10 for _ in range(8)]
        self.b=None
    
    def get_botones(self,boton,i,j):
        self.botones[i][j] = boton

    def seleccionar_asiento(self,i,j,btn,label):
        self.asientos[i][j].estado = not self.asientos[i][j].estado
    
        if self.asientos[i][j].estado:
            btn.config(bg="#147df5")
        else:
            self.asientos[i][j].estado = False
            btn.config(bg="gray")
        cont=0
        for h in range(8):
            for l in range(10):
                if self.asientos[h][l].estado == True:
                    cont+=1
        label.set(f"Asientos: {cont}\nCosto: ${cont * 15000}")

    def ventana_sala(self,root):
        ventana_asientos = tk.Toplevel(root)
        ventana_asientos.title("Selección de Asientos")
        ventana_asientos.geometry(f"900x650+250+30")
        ventana_asientos.config(bg="#1e1e1e")
        texto_info = tk.StringVar()
        # Título
        tk.Label(ventana_asientos, text="Selección de Asientos", font=("Arial", 25,"bold"), bg="#1e1e1e", fg="white").pack(pady=10)
        # Indicador de Pantalla
        pantalla = tk.Frame(ventana_asientos, bg="#1e1e1e")
        pantalla.pack(pady=(5, 0))

        pantalla_label = tk.Label(
            pantalla,
            text=f"PANTALLA\nSala: {self.numero}",
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

        for i in range(8):
            for j in range(10):
                if self.asientos[i][j].estado == "asignado":
                    self.b = tk.Button(grid_frame, text=f"{i*10 + j + 1}", bg="Red", fg="white", width=4, height=2)
                elif not self.asientos[i][j].estado:
                    self.b = tk.Button(grid_frame, text=f"{i*10 + j + 1}", bg="grey", fg="white", width=4, height=2)
                    self.b.config(command=lambda i=i, j=j, btn=self.b: self.seleccionar_asiento(i, j, btn,texto_info))
                else: 
                    self.b = tk.Button(grid_frame, text=f"{i*10 + j + 1}", bg="#147df5", fg="white", width=4, height=2)
                    self.b.config(command=lambda i=i, j=j, btn=self.b: self.seleccionar_asiento(i, j, btn,texto_info))
                
                self.get_botones(self.b,i,j)
                self.b.grid(row=i, column=j, padx=5, pady=5)

        # Info de selección

        tk.Label(ventana_asientos, textvariable=texto_info, fg="white", bg="#1e1e1e", font=("Arial", 12)).pack(pady=10)

        # Botones de acción
        botones_frame = tk.Frame(ventana_asientos, bg="#1e1e1e")
        botones_frame.pack()

        
        tk.Button(botones_frame, text="<< Volver", bg="gray", fg="white", width=15, command=ventana_asientos.withdraw).pack(side="right", padx=10)
        tk.Button(botones_frame, text="Confirmar Compra", command= lambda: self.asiento_asignado(ventana_asientos) ,bg="#147df5", fg="white", width=20).pack(side="left", padx=10)
    
    def asiento_asignado(self,ventana_asientos):
        for i in range(8):
            for j in range(10):
                if self.asientos[i][j].estado:
                    self.asientos[i][j].estado = "asignado"
        ventana_asientos.withdraw()
    
    def verificar_capacidad(self):
        for i in range(8):
            for j in range(10):
                if self.asientos[i][j].estado == "asignado":
                    lleno = True
                else:
                    lleno = False
        if lleno:
            return False
        else:
            return True