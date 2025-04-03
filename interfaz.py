import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import Ecuacion_guardar
import Ecuacion_procesar
class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("500x680")
        
        self.ecuaciom=Ecuacion_guardar.Ecuacion_guardar("resolver.txt")
        # Crear un canvas para manejar la transparencia y la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=500, height=680, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Cargar imagen de fondo
        self.fondo = Image.open("Image/Calculadora_limpia.png")
        self.fondo = self.fondo.resize((500, 680), Image.Resampling.LANCZOS)
        self.fondo_tk = ImageTk.PhotoImage(self.fondo)
        self.canvas.create_image(0, 0, image=self.fondo_tk, anchor="nw")
        
        # Mostrar texto sobre el fondo sin caja de entrada
        self.texto=""
        self.texto_anterior=[""]
        self.intervalo=[]


        self.texto_var = tk.StringVar()
        self.anterior=[""]
        self.texto_id = self.canvas.create_text(405, 110, text="", font=("Arial", 29), fill="gray", anchor="e")
        
        # Crear botones con imágenes en el canvas
        self.botones = {}
        botones_info = [
            ("sin(", 20, 200), ("cos(", 100, 200),  ("tan(", 180, 200), ("exp(", 260, 200), ("log(", 340, 200), ("**", 420, 200),
            ("asin(", 20, 260),("acos(", 100, 260), ("atan(", 180, 260),("(", 260, 260),    (")", 340, 260), ("sqrt(", 420, 260),
            ("X", 20, 320),     ("Y", 100, 320),     ("Z", 180, 320),      (";", 260, 320)     , ("Del", 340, 320), ("C",420, 320),
            ("7", 70, 390), ("8", 170, 390),     ("9", 270, 390),     ("*", 370, 390),
            ("4", 70, 460), ("5", 170, 460),      ("6", 270, 460),    ("/", 370, 460),
            ("1", 70, 530), ("2", 170, 530),     ("3", 270, 530),     ("+", 370, 530),
            (".", 70, 600), ("0", 170, 600),      ("=", 270, 600),    ("-", 370, 600)

        ]
        
        self.imagenes = {}
        self.botones_ids = {}
        for texto, x, y in botones_info:
            if texto==".":
                self.imagenes[texto] = PhotoImage(file=f"Image/punto.png")  
            elif texto=="*":
                self.imagenes[texto] = PhotoImage(file=f"Image/por.png")  
            elif texto=="/":
                self.imagenes[texto] = PhotoImage(file=f"Image/division.png")  
            elif texto=="**":
                self.imagenes[texto] = PhotoImage(file=f"Image/^.png")  
            else:
                self.imagenes[texto] = PhotoImage(file=f"Image/{texto}.png")
            boton = self.canvas.create_image(x + 40, y + 30, image=self.imagenes[texto], anchor="center")
            self.canvas.tag_bind(boton, "<Button-1>", lambda event, t=texto, boton_id=boton: self.boton_presionado(t, boton_id))
            self.botones[texto] = boton
        
    def boton_presionado(self, valor, boton_id):
        # Cambiar tamaño de la imagen temporalmente
        self.animar_boton(boton_id)
        self.actualizar_texto()
        if valor == "C":
            self.texto_var.set("")
            self.anterior = [""]
            self.texto=""
            self.texto_anterior = [""]
            self.intervalo=[]
        elif valor == "=":
            ecuacion=Ecuacion_procesar.Ecuacion_procesar(self.texto)
            #print("self.texto")
            try:
                if ecuacion.reconocer():
                    res=str(ecuacion.resultado())
                    if len(res)>15:
                        self.texto_var.set(res[0:14]+"...")
                    else:
                        self.texto_var.set(res)
                    self.texo=res
                else:
                    print("paso")
                    type()
            except Exception:
                if "X" in self.texto:
                    if ecuacion.reconocer():
                        self.ecuaciom.guardar_ecuacion(self.texto)
                        print("ecuacion guardada")
                        if 0<len(self.intervalo)<3:

                            res=ecuacion.resultado(int(self.intervalo[1]))
                            print(res, self.intervalo[1])
                            self.texto=res, self.texto_var.set(res)

                        elif len(self.intervalo)>3:
                            ecuacion.resultado(self.intervalo[3])

                else:
                    self.texto_var.set("Error")
            self.texto_anterior=[""]
            self.anterior = [""]
            self.intervalo=[]
            
        elif valor == "Del":
            self.texto_var.set(self.anterior[len(self.anterior)-1])
            self.texto=self.texto_anterior[len(self.texto_anterior)-1]
            if len(self.anterior) > 1:
                self.anterior.pop()
                self.texto_anterior.pop()
        elif valor==";":
            self.intervalo.append(";"), self.intervalo.append("")
            self.anterior.append(self.texto_var.get())
            self.texto_var.set(self.texto_var.get() + valor)

        else:
            if len(self.intervalo)==0:
                self.texto+=valor
                self.texto_anterior.append(self.texto)
            else:
                self.intervalo[len(self.intervalo)-1]+=valor

            self.anterior.append(self.texto_var.get())
            self.texto_var.set(self.texto_var.get() + valor)
        
        # Actualizar el texto en el canvas
        self.canvas.itemconfig(self.texto_id, text=self.texto_var.get())

    def animar_boton(self, boton_id):
        # Obtener el texto de la imagen
        for texto, boton in self.botones.items():
            if boton == boton_id:
                imagen = self.imagenes[texto]
                break
        
        # Cambiar el tamaño de la imagen para hacerla más grande
        imagen_ampliada = imagen.subsample(8)  # Puedes ajustar el valor para obtener el tamaño deseado
        self.canvas.itemconfig(boton_id, image=imagen_ampliada)
        
        # Restaurar el tamaño original después de un pequeño retraso
        self.root.after(100, lambda: self.restaurar_boton(boton_id, imagen))  # 100 ms de retraso

    def restaurar_boton(self, boton_id, imagen_original):
        # Restaurar la imagen original después de la animación
        self.canvas.itemconfig(boton_id, image=imagen_original)

    def actualizar_texto(self):
        texto = self.texto_var.get()
        if len(texto) > 15:
            self.texto_var.set("..."+texto[-12:])
        else:
            self.texto_var.set(texto)

    def mostrar_texto(self):
        self.texto_var.set("")
        self.anterior = [""]

    def mostrar_texto(self):
        self.texto_var.set("")
        self.anterior = [""]

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
