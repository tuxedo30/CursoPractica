import tkinter as tk
from tkinter import messagebox as mb

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Datos de Usuario')
        #Títulos
        self.Titulo_ID = tk.Label(text='ID')
        self.Titulo_ID.grid(row=0, column=0, padx=10)
        self.Titulo_Nombre = tk.Label(text='Nombre')
        self.Titulo_Nombre.grid(row=1, column=0, padx=10)
        self.Titulo_Direccion = tk.Label(text='Dirección')
        self.Titulo_Direccion.grid(row=2, column=0, padx=10)
        self.Titulo_Password = tk.Label(text='Contraseña')
        self.Titulo_Password.grid(row=3, column=0, padx=10)
        self.Titulo_Comentario = tk.Label(text='Comentario')
        self.Titulo_Comentario.grid(row=4, column=0, padx=10)
        
        #Entradas
        self.Entrada_ID = tk.Entry()
        self.Entrada_ID.grid(row=0, column=1, padx=(10, 10), pady=(10,10), columnspan=3)
        self.Entrada_Nombre = tk.Entry()
        self.Entrada_Nombre.grid(row=1, column=1, padx=(10, 10),pady=(10,10), columnspan=3)
        self.Entrada_Direccion = tk.Entry()
        self.Entrada_Direccion.grid(row=2, column=1, padx=(10, 10),pady=(10,10), columnspan=3)
        self.Entrada_Password = tk.Entry()
        self.Entrada_Password.grid(row=3, column=1, padx=(10, 10), pady=(10,10), columnspan=3)
        self.Entrada_Comentario = tk.Text(height=10,width=20)
        self.Entrada_Comentario.grid(ipadx=2,row=4, column=1, padx=(10, 10), pady=(10,10), columnspan=3)
        
        #Botonoes
        self.Crear_Boton = tk.Button(text='Crear', command=lambda : self.Crea_Actualiza('CREAR'))
        self.Crear_Boton.grid(row=5, padx=10, column=0, pady=10)
        self.Leer_Boton = tk.Button(text='Leer', command=lambda: self.Lee_Elimina('LEER'))
        self.Leer_Boton.grid(row=5, padx=10,column=1, pady=10)
        self.Actualizar_Boton = tk.Button(text='Actualizar', command=lambda : self.Crea_Actualiza('ACTUALIZAR'))
        self.Actualizar_Boton.grid(row=5, padx=10, column=2, pady=10)
        self.Eliminar_Boton = tk.Button(text='Eliminar', command=lambda: self.Lee_Elimina('ELIMINAR'))
        self.Eliminar_Boton.grid(row=5, padx=10, column=3, pady=10)
        
        #Popup
        self.Popup = ''
         
    def Recolectar_info(self):
        ID = self.Entrada_ID.get()
        N = self.Entrada_Nombre.get()
        P = self.Entrada_Password.get()
        C = self.Entrada_Comentario.get("1.0","end-1c")
        D = self.Entrada_Direccion.get()
        if ID!='' and N!='' and P!='' and C!='' and D!='':
            return [ID,N,P,C,D]
        else:
            self.Popup = mb.showinfo("Message","Debe llenar todos los campos")
        
            
    def Recolectar_id(self):
        ID = self.Entrada_ID.get()
        if ID != '':
            return ID
        else:
            self.Popup = mb.showinfo("Message","Debe especificar el ID")
            e3ed      
    def Crea_Actualiza(self, accion):
        datos = self.Recolectar_info()
        return [datos, accion]
            
    def Lee_Elimina(self, accion):
        id = self.Recolectar_id()
        return [id, accion]

    
    