from core.Funcion import Funcion

class Archivo:
    def __init__(self, nombre, salas_dict):
        self.nombre = nombre
        self.salas_dict = salas_dict  
        self.funciones = []  
    def cargar(self):
        try:
            with open(self.nombre, "r", encoding="utf-8") as file:
                for linea in file:
                    
                    if linea.strip():
                        if linea.strip().startswith("#") or not linea.strip():
                            continue
                        
                        sala_id, nombre, hora,estado, img = linea.strip().split(";")
                        sala = self.salas_dict.get(sala_id)
                        if sala:
                           
                            nueva_funcion = Funcion(sala, nombre, hora, estado == "True", img)
                            sala.funciones.agregar(nueva_funcion)
                            self.funciones.append(nueva_funcion)
                        else:
                            print(f"[Error] Sala con ID '{sala_id}' no encontrada.")
        except FileNotFoundError:
            print(f"[Error] El archivo '{self.nombre}' no existe.")
        except Exception as e:
            print(f"[Error] Fallo al cargar funciones: {e}")

    def guardar(self):
        try:
            with open(self.nombre, "w", encoding="utf-8") as file:
                for funcion in self.funciones:
                    linea = f"{funcion.sala.numero};{funcion.nombre};{funcion.hora};{funcion.estado};{funcion.imagen}\n"
                    file.write(linea)
        except Exception as e:
            print(f"[Error] Fallo al guardar archivo: {e}")

    def actualizar(self, funcionMod, nombreMod, horaMod):
        try:
            with open(self.nombre, "r", encoding="utf-8") as file:
                lineas = file.readlines()

            nuevas_lineas = []
            for linea in lineas:
                if linea.strip().startswith("#") or not linea.strip():
                    nuevas_lineas.append(linea)
                    continue
                sala_id, nombre, hora, estado, img = linea.strip().split(";")
                
                if str(funcionMod.sala.numero) == sala_id:
                    
                    nueva_linea = f"{funcionMod.sala.numero};{nombreMod};{horaMod};{funcionMod.estado};{funcionMod.imagen}\n"
                    nuevas_lineas.append(nueva_linea)
                else:
                    nuevas_lineas.append(linea)

            with open(self.nombre, "w", encoding="utf-8") as file:
                file.writelines(nuevas_lineas)

        except Exception as e:
            print(f"[Error] Fallo al actualizar el archivo: {e}")
