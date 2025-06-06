import tkinter as tk

ventana = tk.Tk()
ventana.title("Mia V1 - Programa gratuito de soporte")
ventana.geometry("1200x600")

fuente_definida0 = ("Verdana", 20)
fuente_definida1 = ("Verdana", 14)
fuente_definida2 = ("Verdana", 13)
fuente_definida3 = ("Verdana", 11)
fuente_definida4 = ("Verdana", 10)

labelsdl = tk.Label(ventana, text="  ")
labelsdl.pack()

#estilo

label1 = tk.Label(ventana, text="Selecciona una categoría para iniciar un mantenimiento", font=fuente_definida0)
label1.pack()

labelsdl = tk.Label(ventana, text="  ")
labelsdl.pack()
#recuadro del frame
marco1 = tk.Frame(ventana)
marco1.pack(fill="both", expand=True)

#determinar la configuracion de las columnas
marco1.columnconfigure((0, 1), weight=1)



#fila 1
"""
categorias

1 Red

2 Sistema

3 Diagnóstico

4 Limpieza

5 Actualizaciones

6 Firewall


7 Info del sistema

"""


categoria1 = tk.LabelFrame(marco1, text=" Red ", font=fuente_definida1, padx=10, pady=15)
categoria1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria1, text="Soluciona la mayoría de los problemas de red", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria1, text="Entrar", font=fuente_definida4).pack(anchor="w", side="left")
tk.Label(categoria1, text="Permite ejecutar varias soluciones de red.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria1, text="Ejecución Rápida", font=fuente_definida4).pack(anchor="w", side="right")
#tk.Label(categoria1, text="Ejecuta una correcion de red rapida").pack(anchor="w", side="left")


categoria2 = tk.LabelFrame(marco1, text=" Sistema y rendimiento", font=fuente_definida1, padx=10, pady=15)
categoria2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria2, text="Mejora el rendimiento de este equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria2, text="Entrar", font=fuente_definida4).pack(anchor="w", side="left")
tk.Label(categoria2, text="Permite mejorar le eficiencia de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria2, text="Mejora Rápido", font=fuente_definida4).pack(anchor="w", side="right")

categoria3 = tk.LabelFrame(marco1, text=" Diagnóstico ", font=fuente_definida1, padx=10, pady=15)
categoria3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria3, text="Emite información útil del equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria3, text="Entrar", font=fuente_definida4).pack(anchor="w", side="left")
tk.Label(categoria3, text="Permite ejecutar varios diagnósticos.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria3, text="Diagnóstico Rápido", font=fuente_definida4).pack(anchor="w", side="right")

categoria4 = tk.LabelFrame(marco1, text=" Limpieza ", font=fuente_definida1, padx=10, pady=15)
categoria4.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria4, text="Limpia y desecha componentes innecesarios", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria4, text="Entrar", font=fuente_definida4).pack(anchor="w", side="left")
tk.Label(categoria4, text="Ejecuta una limpieza Rápida a este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria4, text="Limpieza Rápida", font=fuente_definida4).pack(anchor="w", side="right")



categoria5 = tk.LabelFrame(marco1, text=" Actualizaciones ", font=fuente_definida1, padx=10, pady=15)
categoria5.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria5, text="Permite la ejecutar las actualizaciones de este equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria5, text="Entrar", font=fuente_definida4).pack(anchor="w", side="left")
tk.Label(categoria5, text="Entrar a las opciones de actualización.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria5, text="Forzar actualización", font=fuente_definida4).pack(anchor="w", side="right")

categoria6 = tk.LabelFrame(marco1, text=" Firewall Y Seguridad ", font=fuente_definida1, padx=10, pady=15)
categoria6.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria6, text="Protege este equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria6, text="Entrar", font=fuente_definida4).pack(anchor="w", side="left")
tk.Label(categoria6, text="Previene y controla la seguridad para este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria6, text="Análisis de antivirus", font=fuente_definida4).pack(anchor="w", side="right")

categoria7 = tk.LabelFrame(marco1, text=" Info del sistema ", font=fuente_definida1, padx=10, pady=15)
categoria7.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria7, text="Reporta la información de hardware, controladores y otros", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria7, text="Entrar", font=fuente_definida4).pack(anchor="w", side="left")
tk.Label(categoria7, text="Revisar la información de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria7, text="Emitir informe", font=fuente_definida4).pack(anchor="w", side="right")

categoria8 = tk.LabelFrame(marco1, text=" Funciones adicionales ", font=fuente_definida1, padx=10, pady=15)
categoria8.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria8, text="Gestión de Servicios y Programas entre algunos.", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria8, text="Entrar", font=fuente_definida4).pack(anchor="w")




"""
marco2 = tk.Frame(ventana)
marco2.pack(fill="both", expand=True)

#determinar la configuracion de las columnas
marco2.columnconfigure((0), weight=1)



#fila 2
categoria3 = tk.LabelFrame(marco2, text="Categoría 1", padx=10, pady=10)
categoria3.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria3, text="Texto 1").pack(anchor="w")
tk.Button(categoria3, text="Botón 1").pack(anchor="w")


"""

#




ventana.mainloop()

"""
Nota del desarollador(Ideas)
* se podria incluir una opcion 
* incluir colores intuitivos para la tercera edad o usuarios novatos
* incluir fondo
* barra de carga

"""