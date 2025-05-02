from core.Asiento import Asiento
from core.ListaCircular import ListaCircular
from core.ListaEnlazada import ListaEnlazada
import tkinter as tk

class Sala:
    def __init__(self, numero, asientos_raw):
        self.numero = numero
        self.funciones = ListaCircular()
        self.asientos = []
        self.iniciar = False
        
        for fila in asientos_raw:
            fila_enlazada = ListaEnlazada()
            for asiento in fila:
                fila_enlazada.agregar(asiento)
            self.asientos.append(fila_enlazada)

        self.botones = [[None]*10 for _ in range(8)]
        self.b = None

    def get_botones(self, boton, i, j):
        self.botones[i][j] = boton

    def seleccionar_asiento(self, i, j, btn, label):
        asiento = self.asientos[i].obtener(j)
        asiento.estado = not asiento.estado

        if asiento.estado:
            btn.config(bg="#147df5")
        else:
            asiento.estado = False
            btn.config(bg="gray")

        cont = 0
        for fila in self.asientos:
            for asiento in fila.recorrer():
                if asiento.estado == True:
                    cont += 1
        label.set(f"Asientos: {cont}\nCosto: ${cont * 15000}")

    def resumen_ocupacion(self):
        ocupados = 0
        for fila in self.asientos:
            for asiento in fila.recorrer():
                if asiento.estado == "asignado":
                    ocupados += 1
        ganancia = ocupados * 15000
        return ocupados, ganancia

    def ventana_sala(self, root):
        
        if self.iniciar == True:
            
            advertencia = tk.Toplevel()
            advertencia.title("¡Advertencia!")
            advertencia.geometry("350x90+500+300")
            advertencia.resizable(False, False)
            advertencia.config(bg="#1e1e1e")
            tk.Label(advertencia,text = "La pelicula ya ha iniciado", bg = "#1e1e1e", fg="white",font= ("Arial",12)).pack(pady=5)
            boton_cerrar = tk.Button(advertencia, text="Cerrar", command=advertencia.destroy)
            boton_cerrar.pack(pady=10)
            return False
        
        ventana_asientos = tk.Toplevel(root)
        ventana_asientos.title("Selección de Asientos")
        ventana_asientos.geometry("900x650+250+30")
        ventana_asientos.config(bg="#1e1e1e")
        texto_info = tk.StringVar()

        tk.Label(ventana_asientos, text="Selección de Asientos", font=("Arial", 25,"bold"), bg="#1e1e1e", fg="white").pack(pady=10)

        pantalla = tk.Frame(ventana_asientos, bg="#1e1e1e")
        pantalla.pack(pady=(5, 0))

        tk.Label(pantalla, text=f"PANTALLA\nSala: {self.numero}", font=("Arial", 14, "bold"), bg="#1e1e1e", fg="white").pack()
        tk.Frame(pantalla, bg="gray", height=4, width=300).pack(pady=2)

        grid_frame = tk.Frame(ventana_asientos, bg="#1e1e1e")
        grid_frame.pack(pady=10)

        for i in range(8):
            for j in range(10):
                asiento = self.asientos[i].obtener(j)
                estado = asiento.estado
                texto = f"{i*10 + j + 1}"

                if estado == "asignado":
                    self.b = tk.Button(grid_frame, text=texto, bg="Red", fg="white", width=4, height=2)
                elif not estado:
                    self.b = tk.Button(grid_frame, text=texto, bg="gray", fg="white", width=4, height=2)
                    self.b.config(command=lambda i=i, j=j, btn=self.b: self.seleccionar_asiento(i, j, btn, texto_info))
                else:
                    self.b = tk.Button(grid_frame, text=texto, bg="#147df5", fg="white", width=4, height=2)
                    self.b.config(command=lambda i=i, j=j, btn=self.b: self.seleccionar_asiento(i, j, btn, texto_info))

                self.get_botones(self.b, i, j)
                self.b.grid(row=i, column=j, padx=5, pady=5)

        tk.Label(ventana_asientos, textvariable=texto_info, fg="white", bg="#1e1e1e", font=("Arial", 12)).pack(pady=10)

        botones_frame = tk.Frame(ventana_asientos, bg="#1e1e1e")
        botones_frame.pack()

        tk.Button(botones_frame, text="<< Volver", bg="gray", fg="white", width=15, command=ventana_asientos.withdraw).pack(side="right", padx=10)
        tk.Button(botones_frame, text="Confirmar Compra", command=lambda: self.asiento_asignado(ventana_asientos), bg="#147df5", fg="white", width=20).pack(side="left", padx=10)

    def asiento_asignado(self, ventana_asientos):
        for fila in self.asientos:
            for asiento in fila.recorrer():
                if asiento.estado:
                    asiento.estado = "asignado"
        ventana_asientos.withdraw()

    def verificar_capacidad(self):
        lleno = True
        for fila in self.asientos:
            for asiento in fila.recorrer():
                if asiento.estado != "asignado":
                    lleno = False
                    break
        return not lleno

    def set_iniciar(self,iniciar):
        self.iniciar = iniciar