import tkinter as tk

class Funcion:
    def __init__(self,sala,nombre,hora,estado,imagen):
        self.sala=sala
        self.nombre = nombre
        self.hora=hora
        self.estado=estado
        self.imagen = imagen

    def ventana(self,frame,content_frame):
        titulo_funcion = f"{self.sala.numero} - {self.hora} - {self.nombre}"
        try:
                imagen_tk = tk.PhotoImage(file=self.imagen)
                boton_pelicula = tk.Button(frame, image=imagen_tk, command=lambda titulo=titulo_funcion: self.sala.ventana_sala(content_frame))
                boton_pelicula.image = imagen_tk  
                boton_pelicula.pack(side="left", padx=10)

                info_pelicula = tk.Label(frame, text=f"{self.hora} - {self.nombre}", font=("Arial", 15), bg="#2a2a2a", fg="white")
                info_pelicula.pack(side="left", padx=5)

        except tk.TclError as e:
                
                tk.Label(content_frame, text=f"Error al cargar imagen: {self.imagen} ({e})", fg="red", bg="#2a2a2a").pack(side="left", padx=10)
                info_pelicula = tk.Label(frame, text=f"{self.hora} - {self.nombre}", font=("Arial", 15), bg="#2a2a2a", fg="white")
                info_pelicula.pack(side="left", padx=5)