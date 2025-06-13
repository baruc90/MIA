import tkinter as tk

def mostrar_menu():
    ventana1.pack_forget()
    ventana2.pack_forget()
    ventana3.pack_forget()
    ventana4.pack_forget()
    ventana5.pack_forget()
    ventana6.pack_forget()
    ventana7.pack_forget()
    ventana8.pack_forget()
    marcoMenu.pack()

def mostrar_ventana(num_ventana):
    marcoMenu.pack_forget() 

    ventana1.pack_forget()
    ventana2.pack_forget()
    ventana3.pack_forget()
    ventana4.pack_forget()
    ventana5.pack_forget()
    ventana6.pack_forget()
    ventana7.pack_forget()
    ventana8.pack_forget()
    

    if num_ventana == 1:
        ventana1.pack()
    elif num_ventana == 2:
        ventana2.pack()
    elif num_ventana == 3:
        ventana3.pack()
    elif num_ventana == 4:
        ventana4.pack()
    elif num_ventana == 5:
        ventana5.pack()
    elif num_ventana == 6:
        ventana6.pack()
    elif num_ventana == 7:
        ventana7.pack()
    elif num_ventana == 8:
        ventana6.pack()




ventana = tk.Tk()
ventana.title("Mia V1 - Programa gratuito de soporte")
ventana.geometry("1200x600")

#estilo
fuente_definida0 = ("Verdana", 20)
fuente_definida1 = ("Verdana", 14)
fuente_definida2 = ("Verdana", 13)
fuente_definida3 = ("Verdana", 11)
fuente_definida4 = ("Verdana", 10)


labelsdl = tk.Label(ventana, text="")
labelsdl.pack()

mensajelbl ="Selecciona una categoría para iniciar un mantenimiento"
label1 = tk.Label(ventana, text=mensajelbl, font=fuente_definida0)
label1.pack()

labelsdl = tk.Label(ventana, text="  ")
labelsdl.pack()


marcoMenu = tk.Frame(ventana)
marcoMenu.pack(fill="both", expand=True)


marcoMenu.columnconfigure((0, 1), weight=1)


"""
categorias

1 RED

2 SISTEMA

3 DIAGNÓSTICO

4 LIMPIEZA

5 ACTUALIZACIONES

6 FIREWALL

7 INFO DEL SISTEMA

8 FUNCIONES ADICIONALES

"""
listaTitulo = [' ', 'RED ',' SISTEMA ',' Diagnóstico ',' DIAGNÓSTICO ',' LIMPIEZA ', ' ACTUALIZACIONES ', ' FIREWALL ',' INFO DEL SISTEMA ',' FUNCIONES ADICIONALES ']
print(listaTitulo[0])
categoria1 = tk.LabelFrame(marcoMenu, text=" Red ", font=fuente_definida1, padx=10, pady=15)
categoria1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria1, text="Soluciona la mayoría de los problemas de red", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria1, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(1)).pack(anchor="w", side="left")
tk.Label(categoria1, text="Permite ejecutar varias soluciones de red.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria1, text="Ejecución Rápida", font=fuente_definida4).pack(anchor="w", side="right")
#tk.Label(categoria1, text="Ejecuta una correcion de red rapida").pack(anchor="w", side="left")

categoria2 = tk.LabelFrame(marcoMenu, text=" Sistema y rendimiento", font=fuente_definida1, padx=10, pady=15)
categoria2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria2, text="Mejora el rendimiento de este equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria2, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(2)).pack(anchor="w", side="left")
tk.Label(categoria2, text="Permite mejorar le eficiencia de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria2, text="Mejora Rápido", font=fuente_definida4).pack(anchor="w", side="right")


categoria3 = tk.LabelFrame(marcoMenu, text=" Diagnóstico ", font=fuente_definida1, padx=10, pady=15)
categoria3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria3, text="Emite información útil del equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria3, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(3)).pack(anchor="w", side="left")
tk.Label(categoria3, text="Permite ejecutar varios diagnósticos.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria3, text="Diagnóstico Rápido", font=fuente_definida4).pack(anchor="w", side="right")

categoria4 = tk.LabelFrame(marcoMenu, text=" Limpieza ", font=fuente_definida1, padx=10, pady=15)
categoria4.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria4, text="Limpia y desecha componentes innecesarios", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria4, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(4)).pack(anchor="w", side="left")
tk.Label(categoria4, text="Ejecuta una limpieza Rápida a este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria4, text="Limpieza Rápida", font=fuente_definida4).pack(anchor="w", side="right")


categoria5 = tk.LabelFrame(marcoMenu, text=" Actualizaciones ", font=fuente_definida1, padx=10, pady=15)
categoria5.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria5, text="Permite la ejecutar las actualizaciones de este equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria5, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(5)).pack(anchor="w", side="left")
tk.Label(categoria5, text="Entrar a las opciones de actualización.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria5, text="Forzar actualización", font=fuente_definida4).pack(anchor="w", side="right")

categoria6 = tk.LabelFrame(marcoMenu, text=" Firewall Y Seguridad ", font=fuente_definida1, padx=10, pady=15)
categoria6.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria6, text="Protege este equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria6, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(6)).pack(anchor="w", side="left")
tk.Label(categoria6, text="Previene y controla la seguridad para este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria6, text="Análisis de antivirus", font=fuente_definida4).pack(anchor="w", side="right")


categoria7 = tk.LabelFrame(marcoMenu, text=" Info del sistema ", font=fuente_definida1, padx=10, pady=15)
categoria7.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria7, text="Reporta la información de hardware, controladores y otros", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria7, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(7)).pack(anchor="w", side="left")
tk.Label(categoria7, text="Revisar la información de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria7, text="Emitir informe", font=fuente_definida4).pack(anchor="w", side="right")

categoria8 = tk.LabelFrame(marcoMenu, text=" Funciones adicionales ", font=fuente_definida1, padx=10, pady=15)
categoria8.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria8, text="Gestión de Servicios y Programas entre algunos.", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria8, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(8)).pack(anchor="w")

marcoMenu.pack()


# Ventana 1
#ventana1 = tk.Frame(ventana,bg="lightgray" ,borderwidth=2, relief="solid" )
#ventana1.pack(pady=50)
#ventana1.pack(fill="both", expand=True,padx=10, pady=10)
#ventana1.pack(padx=10, pady=10)
datosCom1 = [("comando1ambia de fila cada 2 elementosambia de fila cada 2 elementos","ejecucion1"),
             ("comando2","ejecucion2"),
             ("comando3","ejecucion3"),
             ("comando4","ejecucion4"),
             ("comando5","ejecucion5"),
             ("comando6","ejecucion6"),
             ("comando7","ejecucion7"),
             ("comando8","ejecucion8") ]

ventana1 = tk.Frame(ventana)
tk.Label(ventana1, text=listaTitulo[1],  font=fuente_definida1).pack(pady=20)
frame = tk.Frame(ventana1,bg="yellow")
frame.pack(padx=10, pady=10)

for i, (numero, nombre) in enumerate(datosCom1):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Número: {numero}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Fruta: {nombre}",  font=fuente_definida2).grid(row=fila, column=columna+ 1, sticky="w")




tk.Button(ventana1, text="Volver al menú", command=mostrar_menu,  font=fuente_definida1).pack()


#Ventana 2
ventana2 = tk.Frame(ventana)
tk.Label(ventana2, text=listaTitulo[2], font=fuente_definida1).pack(pady=20)

datosCom2 = [("cxxxxa de fila cada 2 elementosambia de fila cada 2 elementos","ejecucion1"),
            ("comando2","ejecucion2"),
            ("comando3","ejecucion3"),
            ("comando4","ejecucion4"),
            ("comando5","ejecucion5"),
            ("comando6","ejecucion6"),
            ("comando7","ejecucion7"),
            ("comando8","ejecucion8") ]

frame = tk.Frame(ventana2,bg="yellow")
frame.pack(padx=10, pady=10)

for i, (numero, nombre) in enumerate(datosCom2):

    fila = i // 1 
    columna = i % 1 
    

    tk.Label(frame, text=f"Número: {numero}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Fruta: {nombre}", font=fuente_definida2).grid(row=fila, column=columna+ 1, sticky="w")


tk.Button(ventana2, text="Volver al menú", command=mostrar_menu).pack()
#Ventana 3
ventana3 = tk.Frame(ventana)
tk.Label(ventana3, text=listaTitulo[3], font=fuente_definida1).pack(pady=20)

datosCom3 = [("cqqqqq   a de fila cada 2 elementosambia de fila cada 2 elementos","ejecucion1"),
            ("comando2","ejecucion2"),
            ("comando3","ejecucion3"),
            ("comando4","ejecucion4"),
            ("comando5","ejecucion5"),
            ("comando6","ejecucion6"),
            ("comando7","ejecucion7"),
            ("comando8","ejecucion8") ]

frame = tk.Frame(ventana3,bg="yellow")
frame.pack(padx=10, pady=10)

for i, (numero, nombre) in enumerate(datosCom3):

    fila = i // 1  
    columna = i % 1 
    
    tk.Label(frame, text=f"Número: {numero}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Fruta: {nombre}", font=fuente_definida2).grid(row=fila, column=columna+ 1, sticky="w")


tk.Button(ventana3, text="Volver al menú", command=mostrar_menu).pack()


#Ventana 4
ventana4 = tk.Frame(ventana)
tk.Label(ventana4, text=listaTitulo[4], font=fuente_definida1).pack(pady=20)

datosCom4 = [("cqqqqq   a de fila cada 2 elementosambia de fila cada 2 elementos","ejecucion1"),
            ("comando2","ejecucion2"),
            ("comando3","ejecucion3"),
            ("comando4","ejecucion4"),
            ("comando5","ejecucion5"),
            ("comando6","ejecucion6"),
            ("comando7","ejecucion7"),
            ("comando8","ejecucion8") ]

frame = tk.Frame(ventana4,bg="yellow")
frame.pack(padx=10, pady=10)

for i, (numero, nombre) in enumerate(datosCom4):

    fila = i // 1 
    columna = i % 1 

    tk.Label(frame, text=f"Número: {numero}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Fruta: {nombre}", font=fuente_definida2).grid(row=fila, column=columna+ 1, sticky="w")


tk.Button(ventana4, text="Volver al menú", command=mostrar_menu).pack()

#Ventana 5
ventana5 = tk.Frame(ventana)
tk.Label(ventana4, text=listaTitulo[5], font=fuente_definida1).pack(pady=20)

datosCom5 = [("cqqqqq   a de fila cada 2 elementosambia de fila cada 2 elementos","ejecucion1"),
            ("comando2","ejecucion2"),
            ("comando3","ejecucion3"),
            ("comando4","ejecucion4"),
            ("comando5","ejecucion5"),
            ("comando6","ejecucion6"),
            ("comando7","ejecucion7"),
            ("comando8","ejecucion8") ]

frame = tk.Frame(ventana5,bg="yellow")
frame.pack(padx=10, pady=10)

for i, (numero, nombre) in enumerate(datosCom5):

    fila = i // 1 
    columna = i % 1 
    

    tk.Label(frame, text=f"Número: {numero}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Fruta: {nombre}", font=fuente_definida2).grid(row=fila, column=columna+ 1, sticky="w")


tk.Button(ventana5, text="Volver al menú", command=mostrar_menu).pack()

#Ventana 6 
ventana6 = tk.Frame(ventana)
tk.Label(ventana6, text=listaTitulo[6], font=fuente_definida1).pack(pady=20)

datosCom6 = [("cqqqqq   a de fila cada 2 elementosambia de fila cada 2 elementos","ejecucion1"),
            ("comando2","ejecucion2"),
            ("comando3","ejecucion3"),
            ("comando4","ejecucion4"),
            ("comando5","ejecucion5"),
            ("comando6","ejecucion6"),
            ("comando7","ejecucion7"),
            ("comando8","ejecucion8") ]

frame = tk.Frame(ventana6,bg="yellow")
frame.pack(padx=10, pady=10)

for i, (numero, nombre) in enumerate(datosCom6):

    fila = i // 1 
    columna = i % 1 
    

    tk.Label(frame, text=f"Número: {numero}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Fruta: {nombre}", font=fuente_definida2).grid(row=fila, column=columna+ 1, sticky="w")


tk.Button(ventana6, text="Volver al menú", command=mostrar_menu).pack()

#Ventana 7
ventana7 = tk.Frame(ventana)
tk.Label(ventana7, text=listaTitulo[7], font=fuente_definida1).pack(pady=20)

datosCom7 = [("cqqqqq   a de fila cada 2 elementosambia de fila cada 2 elementos","ejecucion1"),
            ("comando2","ejecucion2"),
            ("comando3","ejecucion3"),
            ("comando4","ejecucion4"),
            ("comando5","ejecucion5"),
            ("comando6","ejecucion6"),
            ("comando7","ejecucion7"),
            ("comando8","ejecucion8") ]

frame = tk.Frame(ventana7,bg="yellow")
frame.pack(padx=10, pady=10)

for i, (numero, nombre) in enumerate(datosCom7):

    fila = i // 1 
    columna = i % 1 

    tk.Label(frame, text=f"Número: {numero}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Fruta: {nombre}", font=fuente_definida2).grid(row=fila, column=columna+ 1, sticky="w")


tk.Button(ventana7, text="Volver al menú", command=mostrar_menu).pack()

#Ventana 8
ventana8 = tk.Frame(ventana)
tk.Label(ventana8, text=listaTitulo[8], font=fuente_definida1).pack(pady=20)

datosCom8 = [("cqqqqq   a de fila cada 2 elementosambia de fila cada 2 elementos","ejecucion1"),
            ("comando2","ejecucion2"),
            ("comando3","ejecucion3"),
            ("comando4","ejecucion4"),
            ("comando5","ejecucion5"),
            ("comando6","ejecucion6"),
            ("comando7","ejecucion7"),
            ("comando8","ejecucion8") ]

frame = tk.Frame(ventana8,bg="yellow")
frame.pack(padx=10, pady=10)

for i, (numero, nombre) in enumerate(datosCom8):

    fila = i // 1 
    columna = i % 1

    tk.Label(frame, text=f"Número: {numero}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Fruta: {nombre}", font=fuente_definida2).grid(row=fila, column=columna+ 1, sticky="w")


tk.Button(ventana8, text="Volver al menú", command=mostrar_menu).pack()


ventana.mainloop()

"""
Nota del desarollador(Ideas)
* se podria incluir una opcion 
* incluir colores intuitivos para la tercera edad o usuarios novatos
* incluir fondo
* barra de carga

"""