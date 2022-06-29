import tkinter as tk

from setuptools import Command

from coneccionxqllite import Crear_BaseDatos


class Interfaz:
    
    def Pintar_Interfaz(self):
        #Interfaz gráfica
        Root = tk.Tk()
        Root.title('Datos de Usuario')
        #Títulos
        Titulo_ID = tk.Label(text='ID')
        Titulo_ID.grid(row=0, column=0, padx=10)
        Titulo_Nombre = tk.Label(text='Nombre')
        Titulo_Nombre.grid(row=1, column=0, padx=10)
        Titulo_Direccion = tk.Label(text='Dirección')
        Titulo_Direccion.grid(row=1, column=0, padx=10)
        Titulo_Password = tk.Label(text='Contraseña')
        Titulo_Password.grid(row=2, column=0, padx=10)
        Titulo_Comentario = tk.Label(text='Comentario')
        Titulo_Comentario.grid(row=3, column=0, padx=10)
        
        #Entradas
        Entrada_ID = tk.Entry()
        Entrada_ID.grid(row=0, column=1, padx=(10, 10), pady=(10,10), columnspan=3)
        Entrada_Nombre = tk.Entry()
        Entrada_Nombre.grid(row=1, column=1, padx=(10, 10),pady=(10,10), columnspan=3)
        Entrada_Direccion = tk.Entry()
        Entrada_Direccion.grid(row=1, column=1, padx=(10, 10),pady=(10,10), columnspan=3)
        Entrada_Password = tk.Entry()
        Entrada_Password.grid(row=2, column=1, padx=(10, 10), pady=(10,10), columnspan=3)
        Entrada_Comentario = tk.Text(height=10,width=20)
        Entrada_Comentario.grid(ipadx=2,row=3, column=1, padx=(10, 10), pady=(10,10), columnspan=3)
        
        #Botonoes
        Crear_Boton = tk.Button(text='Crear', command=self.Crear)
        Crear_Boton.grid(row=4, padx=10, column=0, pady=10)
        Leer_Boton = tk.Button(text='Leer', command=self.Leer)
        Leer_Boton.grid(row=4, padx=10,column=1, pady=10)
        Actualizar_Boton = tk.Button(text='Actualizar', command=self.Actualizar)
        Actualizar_Boton.grid(row=4, padx=10, column=2, pady=10)
        Eliminar_Boton = tk.Button(text='Eliminar', command=self.Eliminar)
        Eliminar_Boton.grid(row=4, padx=10, column=3, pady=10)
        
        Root.mainloop()
        
    def Crear(self):
        pass
    
    def Leer(self):
        pass
    
    def Actualizar(self):
        pass
    
    def Eliminar(self):
        print('probando botones')
    
    def Recolectar_info(self,GUI):
        datos = {}
        datos.add.ID.get()
        datos.add.N.get()
        datos.add.D.get()
        datos.add.P.get()
        datos.add.C.get()
        return datos
    
    def imprimir_info(self,datos, GUI):
        pass