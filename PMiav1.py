import tkinter as tk
from tkinter import messagebox
from tkinter import ttk #importacion individual
import subprocess


def mostrarMenu():
    ventana1.pack_forget()
    ventana2.pack_forget()
    ventana3.pack_forget()
    ventana4.pack_forget()
    ventana5.pack_forget()
    ventana6.pack_forget()

    marcoMenu.pack()

def mostrar_ventana(numeroVentana):
    marcoMenu.pack_forget() 

    ventana1.pack_forget()
    ventana2.pack_forget()
    ventana3.pack_forget()
    ventana4.pack_forget()
    ventana5.pack_forget()
    ventana6.pack_forget()
 
    

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


global barras_progreso
barras_progreso = []




def ejecutarComando(valor, numBar):
    print(valor)
    print(numBar)
    
    global comandoSeleccionado
    comandoSeleccionado = valor

    barras_progreso[0]["value"] = 0
   

    try:
        

        result = subprocess.run(comandoSeleccionado, capture_output=True, text=True, shell=True)
        barras_progreso[numBar]["value"] = 100
        #salida = result.stdout + result.stderr
        if result.returncode == 0:
            
            messagebox.showinfo("Éxito", f" Ejecución completada!\n{result.stdout}")
            barras_progreso[numBar]["value"] = 0
            print(numBar)
         
        else:
            messagebox.showerror("Error", f"Ocurrió un error:\n{result.stderr}")
            barras_progreso[numBar]["value"] = 0
    except Exception as e:
        messagebox.showerror("Error", f"Excepción:\n{str(e)}")
        barras_progreso[numBar]["value"] = 0



#funcion menu principal
def ejecutarComando2(valor2):
    print(valor2)
    
    
    EjeCam2 = [("ipconfig /flushdns && ipconfig /release && ipconfig /renew"),
             ("del /q /f /s %temp%\\*"),
             ("ipconfig /renew"),
             ("taskmgr"),
             ("msinfo32")]

    try:
        
        result = subprocess.run(EjeCam2[valor2], capture_output=True, text=True, shell=True)
        
       
        
        #salida = result.stdout + result.stderr
        if result.returncode == 0:
            


            messagebox.showinfo("Éxito", f" Ejecución completada!\n{result.stdout}")
           

 
        else:
            messagebox.showerror("Error", f"Ocurrió un error!:\n{result.stderr}")

    except Exception as e:
        messagebox.showerror("Error", f"Excepción!:\n{str(e)}")





ventana = tk.Tk()
ventana.title("Mia V1 - Programa gratuito de soporte")
ventana.geometry("1200x600")

#Estilo
fuentePers = [20,15,13,11,10,'Verdana']
fuente_definida0 = (fuentePers[5], fuentePers[0])
fuente_definida1 = (fuentePers[5], fuentePers[1])
fuente_definida2 = (fuentePers[5], fuentePers[2])
fuente_definida3 = (fuentePers[5], fuentePers[3])
fuente_definida4 = (fuentePers[5], fuentePers[4])

listaTitulo = [
    ' Selecciona una categoría para iniciar un mantenimiento ', 'RED ',' SISTEMA Y LIMPIEZA',' DIAGNÓSTICO ',' INFO DEL SISTEMA ', ' ACTUALIZACIONES, FIREWALL y SEGURIDAD ', ' FUNCIONES ADICIONALES ',' En Contruccion ... '
    ]

labelsdl = tk.Label(ventana, text="")
labelsdl.pack()

mensajelbl =listaTitulo[0]
label1 = tk.Label(ventana, text=mensajelbl, font=fuente_definida0)
label1.pack()
marcoMenu = tk.Frame(ventana)
marcoMenu.pack(fill="both", expand=True)


marcoMenu.columnconfigure((0, 1), weight=1)


"""
categorias

1 RED

2 SISTEMA y 4 LIMPIEZA

3 DIAGNÓSTICO

4 ACTUALIZACIONES, FIREWALL y SEGURIDAD

5 INFO DEL SISTEMA

6 FUNCIONES ADICIONALES

 

"""



categoria1 = tk.LabelFrame(marcoMenu, text=" Red ", font=fuente_definida1, padx=10, pady=15)
categoria1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria1, text="Soluciona la mayoría de los problemas de red", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria1, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(1)).pack(anchor="w", side="left")
tk.Label(categoria1, text="Permite ejecutar varias soluciones de red.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria1, text="Ejecución Rápida",command=lambda:ejecutarComando2(0) , font=fuente_definida4).pack(anchor="w", side="right")


categoria2 = tk.LabelFrame(marcoMenu, text=" Sistema y Limpieza", font=fuente_definida1, padx=10, pady=15)
categoria2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria2, text="Mejora el rendimiento de este equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria2, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(2)).pack(anchor="w", side="left")
tk.Label(categoria2, text="Permite mejorar le eficiencia de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria2, text="Limpieza Rápida",command=lambda:ejecutarComando2(1), font=fuente_definida4).pack(anchor="w", side="right")


categoria3 = tk.LabelFrame(marcoMenu, text=" Diagnóstico ", font=fuente_definida1, padx=10, pady=15)
categoria3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria3, text="Emite información útil del equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria3, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(3)).pack(anchor="w", side="left")
tk.Label(categoria3, text="Permite ejecutar varios diagnósticos.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria3, text="Diagnóstico Rápido", command=lambda:ejecutarComando2(2), font=fuente_definida4).pack(anchor="w", side="right")


categoria4 = tk.LabelFrame(marcoMenu, text=" Actualizaciones, Firewall Y Seguridad  ", font=fuente_definida1, padx=10, pady=15)
categoria4.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria4, text="Permite la ejecutar las actualizaciones y protege su equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria4, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(4)).pack(anchor="w", side="left")
tk.Label(categoria4, text="Controla la seguridad para este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria4, text="Administrador de Tareas",command=lambda:ejecutarComando2(3), font=fuente_definida4).pack(anchor="w", side="right")

categoria5 = tk.LabelFrame(marcoMenu, text=" Info del sistema ", font=fuente_definida1, padx=10, pady=15)
categoria5.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria5, text="Reporta la información de hardware, controladores y otros", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria5, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(5)).pack(anchor="w", side="left")
tk.Label(categoria5, text="Revisar la información de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria5, text="información", command=lambda:ejecutarComando2(4), font=fuente_definida4).pack(anchor="w", side="right")

categoria6 = tk.LabelFrame(marcoMenu, text=" Funciones adicionales ", font=fuente_definida1, padx=10, pady=15)
categoria6.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria6, text="Gestión de Servicios y Programas entre algunos.", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria6, text="Entrar", font=fuente_definida4, command=lambda: mostrar_ventana(6)).pack(anchor="w")



marcoMenu.pack()


# Ventana 1 Ok
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
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,0)).grid(row=fila, column=columna+ 1, sticky="w")


barraProgreso = ttk.Progressbar(ventana1, mode='determinate', length=200)
barraProgreso.pack()
tk.Button(ventana1, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barras_progreso.append(barraProgreso)



#Ventana 2 ok
datosCom2 = [("Consulta al DNS","nslookup google.com"),
            ("Muestra el nombre completo del sistema operativo.","wmic os get caption && hostname"),
            ("Borra archivos temporales del usuario", "del /q /f /s %temp%\\*"),
             ("Borra carpeta temp (si no está en uso)","rd /s /q %temp%"),
             ("Limpia archivos del sistema","cleanmgr /sagerun:1")]

ventana2 = tk.Frame(ventana)
tk.Label(ventana2, text=listaTitulo[2],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana2,bg="yellow")
frame.pack(padx=5, pady=5)


for i, (texCom, ejeCam) in enumerate(datosCom2):

    fila = i // 1  
    columna = i % 1


    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,1)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana2, mode='determinate', length=200)
barraProgreso.pack()
tk.Button(ventana2, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barras_progreso.append(barraProgreso)




#Ventana 3ok
datosCom3 = [("Verifica conectividad a internet.","ping 8.8.8.8"),
             ("Verifica DNS y conexión","ping google.com"),
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
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,2)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana3, mode='determinate', length=200)
barraProgreso.pack()
tk.Button(ventana3, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barras_progreso.append(barraProgreso)




#Ventana ok
datosCom4 = [("Fuerza detección de actualizaciones (en versiones antiguas)","wuauclt /detectnow"),
             ("Verifica si el servicio de actualizaciones está activo","sc query wuauserv"),
             ("Muestra estado del firewall","netsh advfirewall show allprofiles"),
             ("Fuerza detección de actualizaciones (en versiones antiguas)","wuauclt /detectnow"),
             ("Verifica si el servicio de actualizaciones está activo","sc query wuauserv")
             ]

ventana4 = tk.Frame(ventana)
tk.Label(ventana4, text=listaTitulo[5],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana4,bg="yellow")
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom4):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,3)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana4, mode='determinate', length=200)
barraProgreso.pack()
tk.Button(ventana4, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barras_progreso.append(barraProgreso)




#Ventana 5 ok
datosCom5 = [("Información detallada del sistema.","systeminfo"),
             ("Diagnóstico DirectX","dxdiag"),
             ("Lista los drivers instalados","driverquery"),
             ("Lista procesos activos","tasklist") ]

ventana5 = tk.Frame(ventana)
tk.Label(ventana5, text=listaTitulo[6],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana5,bg="yellow")
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom5):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,4)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana5, mode='determinate', length=200)
barraProgreso.pack()
tk.Button(ventana5, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barras_progreso.append(barraProgreso)



#Ventana 6 en contruccion

datosCom6 = [("","")]
ventana6 = tk.Frame(ventana)
tk.Label(ventana6, text=listaTitulo[6],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana6,bg="yellow")
frame.pack(padx=5, pady=5)

tk.Label(ventana6, text=listaTitulo[7],  font=fuente_definida1).pack(pady=5)
"""
for i, (texCom, ejeCam) in enumerate(datosCom6):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solucion a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,5)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana6, mode='determinate', length=200)
barraProgreso.pack()
"""
tk.Button(ventana6, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barras_progreso.append(barraProgreso)




ventana.mainloop()

"""
Nota del desarollador(Ideas)
* se podria incluir una opcion de idioma 
* incluir colores intuitivos para la tercera edad o usuarios novatos
* incluir fondo 
* barra de carga -> listo

feedback 




"""