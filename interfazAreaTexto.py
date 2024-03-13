#from itertools import tee
#from sqlite3 import adapt
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename

from tkinter.scrolledtext import ScrolledText
#from turtle import width
#from typing import TextIO
from tkinter import ttk
#from click import style
#from analizador import analizador
#from os import startfile

#from matplotlib.pyplot import text

class interfazAreaTexto():

    
    def __init__(self) -> None:
        #self.funciones = analizador()
      
        
        
        def abrirArchivo():
            Tk().withdraw()



            try:
                path = askopenfilename(filetypes=[('*.*','*.*')])
                

                with open(path,encoding='utf-8') as file:
                    txt = file.read().strip()
                    file.close()
            except:
                print("Error")

            
            
            return str(txt)

        def cargarArchivo():

            
            texto= abrirArchivo()
            print(texto)
            t_editor.delete("1.0","end")
            t_editor.insert("1.0",texto)
            pass
        def nuevoArchivo():
            t_editor.delete("1.0","end")

        def guardarArchivo():
            print("Guardar Archivo")

        def analizar():
            texto =t_editor.get("1.0","end")
            print(texto)
            #result1= self.funciones.analizadorLexico(texto)
          
            
            #result2 = self.funciones.analSintactico(result1[0])

            #result3 = self.funciones.analSemantico(result2[0],texto)
     

            #self.funciones.reporteTokens(result1[0])
            #self.funciones.reporteErrores(result1[1],result2[1],result3[2])
            #startfile("dynamicForm.html")
            pass

        
        ventana = Tk()

        ventana.geometry("920x600")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)

        #b_volver = Button(ventana,text="volver")

        b_analizar = Button(ventana,text="Analizar", command=analizar)
        l_Editor = Label(ventana,text="Editor de texto:")
        l_Console = Label(ventana,text="Consola:")

        l_Editor.place(x=35,y=50)
        l_Console.place(x=475,y=50)
        
        #b_reporte = Button(ventana,text="Generar Reportes", command=generarReporte)
        #b_Cargar = Button(ventana, text="Cargar Archivo form", command=cargarArchivo)
         

        #b_Cargar.place(x=30,y=15)

        b_analizar.place(x=50,y=540)

        #b_reporte.place(x=520,y=45)

        t_editor = ScrolledText(ventana,width=50,height=26)
        t_console = ScrolledText(ventana,width=50,height=26)
        #ScrolVer = Scrollbar(ventana, command=t_editor.yview)
        #cajaCombo = ttk.Combobox(ventana,values=["Generar Reporte Tokens","Generar Reporte Errores","Manual de Usuario","Manual Técnico"],state="readonly")
        
        t_editor.place(x=30,y=80)
        t_console.place(x=470,y=80)
        #cajaCombo.place(x=600,y=45)
        #cajaCombo.current(0)

        toolbar = Frame(ventana, bd=1, relief=tk.RAISED)

        button1 = Button(toolbar, text="Nuevo Archivo", command=nuevoArchivo)
        button1.pack(side=tk.LEFT, padx=2, pady=2)

        button2 = Button(toolbar, text="Abrir Archivo", command=cargarArchivo)
        button2.pack(side=tk.LEFT, padx=2, pady=2)
        button3 = Button(toolbar, text="Guardar Archivo", command=guardarArchivo)
        button3.pack(side=tk.LEFT, padx=2, pady=2)


        toolbar.pack(side=tk.TOP, fill=tk.X)


        #ScrolVer.place(x=760,y=80)
        

        ventana.mainloop()
        pass