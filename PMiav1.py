import tkinter as tk
from tkinter import messagebox
from tkinter import ttk #importacion individual
import subprocess
#
def mostrar_menu():
    ventana1.pack_forget()
    ventana2.pack_forget()
    ventana3.pack_forget()
    ventana4.pack_forget()
    ventana5.pack_forget()
    ventana6.pack_forget()
    ventana7.pack_forget()
    #ventana8.pack_forget()
    marcoMenu.pack()

def mostrar_ventana(numeroVentana):
    marcoMenu.pack_forget() 

    ventana1.pack_forget()
    ventana2.pack_forget()
    ventana3.pack_forget()
    ventana4.pack_forget()
    ventana5.pack_forget()
    ventana6.pack_forget()
    ventana7.pack_forget()
    #ventana8.pack_forget()
    

    if numeroVentana == 1:
        ventana1.pack()
    elif numeroVentana == 2:
        ventana2.pack()
    elif numeroVentana == 3:
        ventana3.pack()
    elif numeroVentana == 4:
        ventana4.pack()
    elif numeroVentana == 5:
        ventana5.pack()
    elif numeroVentana == 6:
        ventana6.pack()
    elif numeroVentana == 7:
        ventana7.pack()
#    elif numeroVentana == 8:
#       ventana8.pack()


def ejecutarComando(valor):
    print(valor)

    global comando_seleccionado
    comando_seleccionado = valor
    barraProgreso["value"] = 0
    try:

        barraProgreso["value"] = 50
        result = subprocess.run(comando_seleccionado, capture_output=True, text=True, shell=True)
        barraProgreso["value"] = 100
        salida = result.stdout + result.stderr
        if result.returncode == 0:
            
            messagebox.showinfo("Éxito", f"completada! Reporte:\n{result.stdout}")
            barraProgreso["value"] = 100
 
        else:
            messagebox.showerror("Error", f"Ocurrió un error:\n{result.stderr}")
            barraProgreso["value"] = 100
    except Exception as e:
        messagebox.showerror("Error", f"Excepción:\n{str(e)}")
        barraProgreso["value"] = 100

ventana = tk.Tk()
ventana.title("Mia V1 - Programa gratuito de soporte")
ventana.geometry("1200x600")

#estilo
fuentePers = [20,15,13,11,10,'Verdana']
fuente_definida0 = (fuentePers[5], fuentePers[0])
fuente_definida1 = (fuentePers[5], fuentePers[1])
fuente_definida2 = (fuentePers[5], fuentePers[2])
fuente_definida3 = (fuentePers[5], fuentePers[3])
fuente_definida4 = (fuentePers[5], fuentePers[4])

listaTitulo = [' Selecciona una categoría para iniciar un mantenimiento ', 'RED ',' SISTEMA ',' DIAGNÓSTICO ',' LIMPIEZA ', ' ACTUALIZACIONES, FIREWALL y SEGURIDAD ', ' INFO DEL SISTEMA ',' FUNCIONES ADICIONALES  ',' x ']
#print(listaTitulo[0])

labelsdl = tk.Label(ventana, text="")
labelsdl.pack()

mensajelbl =listaTitulo[0]
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

5 FIREWALL y ACTUALIZACIONES

6 INFO DEL SISTEMA

7 FUNCIONES ADICIONALES

8 

"""

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


categoria5 = tk.LabelFrame(marcoMenu, text=" Actualizaciones, Firewall Y Seguridad  ", font=fuente_definida1, padx=10, pady=15)
categoria5.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria5, text="Permite la ejecutar las actualizaciones y protege su equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria5, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(5)).pack(anchor="w", side="left")
tk.Label(categoria5, text="Controla la seguridad para este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria5, text="Análisis de antivirus", font=fuente_definida4).pack(anchor="w", side="right")

categoria6 = tk.LabelFrame(marcoMenu, text=" Info del sistema ", font=fuente_definida1, padx=10, pady=15)
categoria6.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria6, text="Reporta la información de hardware, controladores y otros", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria6, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(6)).pack(anchor="w", side="left")
tk.Label(categoria6, text="Revisar la información de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria6, text="Emitir informe", font=fuente_definida4).pack(anchor="w", side="right")

categoria7 = tk.LabelFrame(marcoMenu, text=" Funciones adicionales ", font=fuente_definida1, padx=10, pady=15)
categoria7.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria7, text="Gestión de Servicios y Programas entre algunos.", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria7, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(7)).pack(anchor="w")
"""
categoria7 = tk.LabelFrame(marcoMenu, text=" Funciones adicionales ", font=fuente_definida1, padx=10, pady=15)
categoria7.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria7, text="Gestión de Servicios y Programas entre algunos.", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria7, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(7)).pack(anchor="w", side="left")
tk.Label(categoria7, text="Revisar la información de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria7, text="Emitir informe", font=fuente_definida4).pack(anchor="w", side="right")

categoria8 = tk.LabelFrame(marcoMenu, text=" Funciones adicionales ", font=fuente_definida1, padx=10, pady=15)
categoria8.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria8, text="Gestión de Servicios y Programas entre algunos.", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria8, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(8)).pack(anchor="w")
"""
marcoMenu.pack()


# Ventana 1
#ventana1 = tk.Frame(ventana,bg="lightgray" ,borderwidth=2, relief="solid" )
#ventana1.pack(pady=50)
#ventana1.pack(fill="both", expand=True,padx=10, pady=10)
#ventana1.pack(padx=10, pady=10)
datosCom1 = [("Limpia caché DNS, resuelve bastantes problemas de conexion a internet ","ipconfig /flushdns"),
             ("Reinicia la IP","ipconfig /release"),
             ("Renueva la IP","ipconfig /renew"),
             ("Restablece la configuracion del socketWinsock  ","netsh int ip reset ")]

ventana1 = tk.Frame(ventana)
tk.Label(ventana1, text=listaTitulo[1],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana1,bg="yellow")
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom1):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd)).grid(row=fila, column=columna+ 1, sticky="w")
  #  tk.Button(frame, text=f"Fruta: {nombre}",  font=fuente_definida2, command=comando).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana1, mode='determinate', length=200)

barraProgreso.pack()
tk.Button(ventana1, text="Volver al menú", command=mostrar_menu,  font=fuente_definida1).pack()


#Ventana 2
datosCom2 = [("Corrige archivos del sistema. Muy usado en soporte.","sfc /scannow"),
             ("DISM /Online /Cleanup-Image /RestoreHealth","Repara la imagen del sistema. Recomendado si sfc falla."),
             ("Renueva la IP","ipconfig /renew"),
             ("chkdsk C: /f /r","Detecta sectores dañados. Tarda más, pero efectivo.") ]

ventana2 = tk.Frame(ventana)
tk.Label(ventana2, text=listaTitulo[2],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana2,bg="yellow")
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom2):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana2, mode='determinate', length=200)

barraProgreso.pack()
tk.Button(ventana2, text="Volver al menú", command=mostrar_menu,  font=fuente_definida1).pack()

#Ventana 3
datosCom3 = [("Verifica conectividad a internet.","ping 8.8.8.8"),
             ("Verifica DNS y conexión","ping google.com"),
             ("Ruta de conexión al servido","tracert google.com"),
             ("Ver puertos y conexiones abiertas","netstat -an"),
             ("Consulta al DNS","nslookup google.com") ]

ventana3 = tk.Frame(ventana)
tk.Label(ventana3, text=listaTitulo[3],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana3,bg="yellow")
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom3):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana3, mode='determinate', length=200)

barraProgreso.pack()
tk.Button(ventana3, text="Volver al menú", command=mostrar_menu,  font=fuente_definida1).pack()


#Ventana 4
datosCom4 = [("Borra archivos temporales del usuario", "del /q /f /s %temp%\\*"),
             ("rd /s /q %temp%","Borra carpeta temp (si no está en uso)"),
             ("Limpia archivos del sistema","cleanmgr /sagerun:1")]

ventana4 = tk.Frame(ventana)
tk.Label(ventana4, text=listaTitulo[4],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana4,bg="yellow")
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom4):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana4, mode='determinate', length=200)

barraProgreso.pack()
tk.Button(ventana4, text="Volver al menú", command=mostrar_menu,  font=fuente_definida1).pack()


#Ventana 5
datosCom5 = [("Fuerza detección de actualizaciones (en versiones antiguas)","wuauclt /detectnow"),
             ("Verifica si el servicio de actualizaciones está activo","sc query wuauserv"),
             ("Muestra estado del firewall","netsh advfirewall show allprofiles"),
             ("Restaura configuración del firewall","netsh advfirewall reset"),
             ("Fuerza detección de actualizaciones (en versiones antiguas)","wuauclt /detectnow"),
             ("Verifica si el servicio de actualizaciones está activo","sc query wuauserv"),
             ("Consulta al DNS","nslookup google.com")
             ]

ventana5 = tk.Frame(ventana)
tk.Label(ventana5, text=listaTitulo[5],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana5,bg="yellow")
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom5):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana5, mode='determinate', length=200)

barraProgreso.pack()
tk.Button(ventana5, text="Volver al menú", command=mostrar_menu,  font=fuente_definida1).pack()

#Ventana 6 
datosCom6 = [("Información detallada del sistema.","systeminfo"),
             ("Abre ventana con info completa del sistema","msinfo32"),
             ("Diagnóstico DirectX","dxdiag"),
             ("Lista los drivers instalados","driverquery"),
             ("Lista procesos activos","tasklist") ]

ventana6 = tk.Frame(ventana)
tk.Label(ventana6, text=listaTitulo[6],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana6,bg="yellow")
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom6):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana6, mode='determinate', length=200)

barraProgreso.pack()
tk.Button(ventana6, text="Volver al menú", command=mostrar_menu,  font=fuente_definida1).pack()

#Ventana 7
datosCom7 = [("Verifica conectividad a internet.","ping 8.8.8.8"),
             ("Verifica DNS y conexión","ping google.com"),
             ("Ruta de conexión al servido","tracert google.com"),
             ("Ver puertos y conexiones abiertas","netstat -an"),
             ("Consulta al DNS","nslookup google.com") ]

ventana7 = tk.Frame(ventana)
tk.Label(ventana7, text=listaTitulo[7],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana7,bg="yellow")
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom7):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana7, mode='determinate', length=200)

barraProgreso.pack()
tk.Button(ventana7, text="Volver al menú", command=mostrar_menu,  font=fuente_definida1).pack()

"""
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
"""

ventana.mainloop()

"""
Nota del desarollador(Ideas)
* se podria incluir una opcion 
* incluir colores intuitivos para la tercera edad o usuarios novatos
* incluir fondo
* barra de carga

"""