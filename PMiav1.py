import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import os
import sys
import webbrowser


def obtenerRuta(nombreArchivo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, nombreArchivo)
    return os.path.join(os.path.abspath("."), nombreArchivo)




#funcion oculta las ventanas pero muestra el marco
def mostrarMenu():
    ventana1.pack_forget()
    ventana2.pack_forget()
    ventana3.pack_forget()
    ventana4.pack_forget()
    ventana5.pack_forget()
    #ventana6.pack_forget()

    marcoMenu.pack()
    marcoMenuInferior.pack(side="bottom", anchor="e", padx=10, pady=10)
#funcion muestra la ventana si se cumple la condicion y oculta las otras
def mostrarVentana(numeroVentana):
    marcoMenu.pack_forget()
    marcoMenuInferior.pack_forget()  

    ventana1.pack_forget()
    ventana2.pack_forget()
    ventana3.pack_forget()
    ventana4.pack_forget()
    ventana5.pack_forget()
    #ventana6.pack_forget()
 
    
#muestra la ventana si cumple la condicion
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
   # elif numeroVentana == 6:
    #    ventana6.pack()

#barra de progreso que se creara dependiendo de las ventas sujetas a ella.
global barrasProgreso
barrasProgreso = []
cantCarac = None
#funcion para resolver si el texto capturado es mayor a 2000 caracteres lo muestre 
#en un scrollbar en vez de un message.info

def mostrarResultado(titulo, mensaje):
    ventanaResultado = tk.Toplevel()
    ventanaResultado.title(titulo)
    ventanaResultado.geometry("500x400")
    


    miframe = tk.Frame(ventanaResultado)
    miframe.pack(fill="both", expand=True)


    scrollbar = tk.Scrollbar(miframe)
    scrollbar.pack(side="right", fill="y")

    text_widget = tk.Text(miframe, wrap="word", yscrollcommand=scrollbar.set)
    text_widget.pack(fill="both", expand=True)
    text_widget.insert("end", mensaje)
    text_widget.config(state="disabled")  # Solo lectura


    scrollbar.config(command=text_widget.yview)

#funcion que ejecuta el comando cmd, recibe el comando en la variable valor y un valor que indica
#el progressbar al cual va aplicar la animacion de progreso
def ejecutarComando(valor, numBarra):
    print(valor)
    print(numBarra)
    
    global comandoSeleccionado
    comandoSeleccionado = valor

    barrasProgreso[0]["value"] = 0
    global cantCarac
    cantCarac = None
   

    try:
        

        result = subprocess.run(comandoSeleccionado, capture_output=True, text=True, shell=True)
        barrasProgreso[numBarra]["value"] = 100
        #salida = result.stdout + result.stderr
        if result.returncode == 0:
            cantCarac = len(result.stdout)
            cantCarac2 = len(result.stderr)
            print(cantCarac)
            print(cantCarac2)
            if cantCarac <= 2000 :
             print('inferior a 2000')
             messagebox.showinfo("Éxito", f" Ejecución completada!\n{result.stdout}")
             barrasProgreso[numBarra]["value"] = 0

            else:
             print('superior a 2000')
             mostrarResultado("Éxito", f"Ejecución completada!\n{result.stdout}")
             barrasProgreso[numBarra]["value"] = 0

            
         
        else:
            if cantCarac == None :
                barrasProgreso[numBarra]["value"] = 100
                messagebox.showinfo("Éxito", "Ejecución completada!\n")   
                barrasProgreso[numBarra]["value"] = 0
            else: 
                messagebox.showerror("Error", f"Ocurrió un error:\n{result.stderr}")
                barrasProgreso[numBarra]["value"] = 0
    except Exception as e:

        
             messagebox.showerror("Error", f"Excepción:\n{str(e)}")
             barrasProgreso[numBarra]["value"] = 0



#funcion menu principal que ejecuta comandos en la ventana principal o botones rapidos
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

def enlaceNavegador(numeroEnlace):

    enlace= ["https://linktr.ee/barucaguilar", "https://github.com/baruc90/MIA"]
    url = enlace[numeroEnlace]

    webbrowser.open_new_tab(url)
    


#creacion de ventanas
version = "1.5"
ventana = tk.Tk()
ventana.title(f"Mia V{version} - Programa gratuito de soporte")
ventana.geometry("1200x500")
ventana.resizable(False, False)

icono_path = obtenerRuta("icono.ico")
ventana.iconbitmap(icono_path)


#Estilo personalizado de font
fuentePers = [20,15,13,11,10,'Verdana']
fuente_definida0 = (fuentePers[5], fuentePers[0])
fuente_definida1 = (fuentePers[5], fuentePers[1])
fuente_definida2 = (fuentePers[5], fuentePers[2])
fuente_definida3 = (fuentePers[5], fuentePers[3])
fuente_definida4 = (fuentePers[5], fuentePers[4])

#lista de titulos de las ventanas y marcos
listaTitulo = [
    ' Selecciona una categoría para iniciar un mantenimiento ', 'RED ',' SISTEMA Y LIMPIEZA',' DIAGNÓSTICO ',' INFO DEL SISTEMA ', ' ACTUALIZACIONES, FIREWALL y SEGURIDAD ', ' FUNCIONES ADICIONALES ',' En Contruccion ... '
    ]



mensajelbl =listaTitulo[0]
label1 = tk.Label(ventana, text=mensajelbl, font=fuente_definida0, pady=15)
label1.pack()
marcoMenu = tk.Frame(ventana)
marcoMenu.pack(fill="both", expand=True)

#se crea un marco de 2 columanas utilizando todo el dimencionado disponible de manera pareja
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

#columnas y su contenido compuesto 
# label titulo
# la ubicacion en la columnas, 
# label descripctivo 
# boton entrar al la ventana ejecutando la funcion mostrarVentana
#label descriptivo
#ejecucion de un comando rapido por la funcion ejecutarComando2





categoria1 = tk.LabelFrame(marcoMenu, text=" Red ", font=fuente_definida1, padx=10, pady=15)
categoria1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria1, text="Soluciona la mayoría de los problemas de red", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria1, text="Entrar", font=fuente_definida4, command=lambda: mostrarVentana(1)).pack(anchor="w", side="left")
tk.Label(categoria1, text="Permite ejecutar varias soluciones de red.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria1, text="Ejecución Rápida",command=lambda:ejecutarComando2(0) , font=fuente_definida4).pack(anchor="w", side="right")


categoria2 = tk.LabelFrame(marcoMenu, text=" Sistema y Limpieza", font=fuente_definida1, padx=10, pady=15)
categoria2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria2, text="Mejora el rendimiento de este equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria2, text="Entrar", font=fuente_definida4, command=lambda: mostrarVentana(2)).pack(anchor="w", side="left")
tk.Label(categoria2, text="Permite mejorar le eficiencia de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria2, text="Limpieza Rápida",command=lambda:ejecutarComando2(1), font=fuente_definida4).pack(anchor="w", side="right")


categoria3 = tk.LabelFrame(marcoMenu, text=" Diagnóstico ", font=fuente_definida1, padx=10, pady=15)
categoria3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria3, text="Emite información útil del equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria3, text="Entrar", font=fuente_definida4, command=lambda: mostrarVentana(3)).pack(anchor="w", side="left")
tk.Label(categoria3, text="Permite ejecutar varios diagnósticos.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria3, text="Diagnóstico Rápido", command=lambda:ejecutarComando2(2), font=fuente_definida4).pack(anchor="w", side="right")


categoria4 = tk.LabelFrame(marcoMenu, text=" Actualizaciones, Firewall Y Seguridad  ", font=fuente_definida1, padx=10, pady=15)
categoria4.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria4, text="Permite la ejecutar las actualizaciones y protege su equipo", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria4, text="Entrar", font=fuente_definida4, command=lambda: mostrarVentana(4)).pack(anchor="w", side="left")
tk.Label(categoria4, text="Controla la seguridad para este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria4, text="Administrador de Tareas",command=lambda:ejecutarComando2(3), font=fuente_definida4).pack(anchor="w", side="right")

categoria5 = tk.LabelFrame(marcoMenu, text=" Info del sistema ", font=fuente_definida1, padx=10, pady=15)
categoria5.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(categoria5, text="Reporta la información de hardware, controladores y otros", font=fuente_definida2).pack(anchor="w")
tk.Button(categoria5, text="Entrar", font=fuente_definida4, command=lambda: mostrarVentana(5)).pack(anchor="w", side="left")
tk.Label(categoria5, text="Revisar la información de este equipo.", font=fuente_definida3).pack(anchor="w", side="left")
tk.Button(categoria5, text="Información", command=lambda:ejecutarComando2(4), font=fuente_definida4).pack(anchor="w", side="right")
"""
categoria6 = tk.LabelFrame(marcoMenu, text=" Funciones adicionales ", font=fuente_definida1, padx=10, pady=15)
categoria6.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(categoria6, text="En Contruccion...", font=fuente_definida2).pack(anchor="w")
"""
#tk.Button(categoria6, text="Entrar", font=fuente_definida4, command=lambda: mostrarVentana(6)).pack(anchor="w")

#pie = tk.Label(text="Creado por:Baruc Fabrizzio Aguilar", font=fuente_definida4, padx=20, pady=20)






#pie.pack( side="center")
#btncontacto = tk.Button(text="contacto")
#btncontacto.pack( side="right")
#se muestra el frame 
marcoMenu.pack()
marcoMenuInferior = tk.Frame(ventana)
marcoMenuInferior.pack(fill="both", expand=True)


botondescarga = tk.Button(marcoMenuInferior, text="¡Descarga la Ultima versión!", command=lambda: enlaceNavegador(1))
botondescarga.pack(side="right", padx=5)

botoncontacto = tk.Button(marcoMenuInferior, text="Contactos", command=lambda: enlaceNavegador(0))
botoncontacto.pack(side="right", padx=5)

labelInfo = tk.Label(marcoMenuInferior, text="Autor: Baruc Fabrizzio Aguilar")
labelInfo.pack(side="right", padx=5)



# Ventana 1 Ok

#tuplas que permite mantener de manera dinamica la generacion de despciones y botones
#contiene una descripcion del comando y el comando a ejecutar

datosCom1 = [("Limpia caché DNS, resuelve bastantes problemas de conexión a internet ","ipconfig /flushdns"),
             ("Reinicia la IP","ipconfig /release"),
             ("Renueva la IP","ipconfig /renew"),
             ("Abre la Conexiones de Red","ncpa.cpl")]

#crea frame principal contenedor ventana1
#crea un frame que contrendra los las descipciones y botones


ventana1 = tk.Frame(ventana)
tk.Label(ventana1, text=listaTitulo[1],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana1)
frame.pack(padx=5, pady=5)

#ejecuta ciclos dependiendo el contenido de la tupla, a medidas que se ejcua el for
#va contruyendo 1 filas y desde la columnas 0  
#el label muestra el valor de las descipciones y los acomoda en la fila y en la columnas en tabla con grid
#cabe mencionar que pack y grid son administradores de geometria y son incompatibles entre si

for i, (texCom, ejeCam) in enumerate(datosCom1):

    fila = i // 1  
    columna = 0
    
    tk.Label(frame, text=f"Solución a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,0)).grid(row=fila, column=columna+ 1, sticky="w")

#creacion del progressbar indicando el frame a mostrar, tambien se van agregando a un array para luego
# ser ejecutado segun su indice y solo ejecutar el que es necesario 
#boton de volver que ejecuta la funcion mostrarMenu ocultando todas las ventanas y mostrando menu principal
barraProgreso = ttk.Progressbar(ventana1, mode='determinate', length=200)
barraProgreso.pack(pady=10)
tk.Button(ventana1, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barrasProgreso.append(barraProgreso)



#Ventana 2 ok
datosCom2 = [("Abrir administrador de usuario", "control userpasswords2"),
             ("Abrir administrador de dispositivos", "devmgmt.msc"),
             ("Abrir administrador de discos", "diskmgmt.msc"),
             ("Opciones de energía","powercfg.cpl"),
            ("Muestra la versión  de Windows y nombre completo del sistema operativo.","wmic os get caption && hostname"),
            ("Borrar archivos temporales del usuario", "del /q /f /s %temp%\\*"),
             ("Borrar carpeta temp (si no está en uso)","rd /s /q %temp%"),
             ("Limpia los archivos del sistema","cleanmgr /sagerun:1")]

ventana2 = tk.Frame(ventana)
tk.Label(ventana2, text=listaTitulo[2],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana2)
frame.pack(padx=5, pady=5)


for i, (texCom, ejeCam) in enumerate(datosCom2):

    fila = i // 1  
    columna = i % 1


    tk.Label(frame, text=f"Solución a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,1)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana2, mode='determinate', length=200)
barraProgreso.pack(pady=10)
tk.Button(ventana2, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barrasProgreso.append(barraProgreso)




#Ventana 3ok
datosCom3 = [("Verifica conectividad a internet.","ping 8.8.8.8"),
             ("Verifica DNS y conexión","ping google.com"),
             ("Ver puertos y conexiones abiertas","netstat -an"),
             ("Abrir panel de control","control panel"),
             ("Consulta al DNS","nslookup google.com") ]

ventana3 = tk.Frame(ventana)
tk.Label(ventana3, text=listaTitulo[3],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana3)
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom3):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solución a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,2)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana3, mode='determinate', length=200)
barraProgreso.pack(pady=10)
tk.Button(ventana3, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barrasProgreso.append(barraProgreso)




#Ventana ok
datosCom4 = [("Fuerza detección de actualizaciones (en versiones antiguas)","wuauclt /detectnow"),
             ("Verifica si el servicio de actualizaciones se mantiene activo","sc query wuauserv"),
             ("Muestra estado del firewall","netsh advfirewall show allprofiles"),
             ("Fuerza detección de actualizaciones (en versiones antiguas)","wuauclt /detectnow"),
             ("Abrir Firewall","control firewall.cpl")
             ]

ventana4 = tk.Frame(ventana)
tk.Label(ventana4, text=listaTitulo[5],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana4)
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom4):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solución a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,3)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana4, mode='determinate', length=200)
barraProgreso.pack(pady=10)
tk.Button(ventana4, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barrasProgreso.append(barraProgreso)




#Ventana 5 ok
datosCom5 = [("Información detallada del sistema.","systeminfo"),
             ("Diagnóstico DirectX","dxdiag"),
             ("Lista los drivers instalados","driverquery"),
             ("Lista procesos activos","tasklist") ]

ventana5 = tk.Frame(ventana)
tk.Label(ventana5, text=listaTitulo[6],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana5)
frame.pack(padx=5, pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom5):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solución a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,4)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana5, mode='determinate', length=200)
barraProgreso.pack(pady=10)
tk.Button(ventana5, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barrasProgreso.append(barraProgreso)



#Ventana 6 en contruccion
"""
datosCom6 = [("","")]
ventana6 = tk.Frame(ventana)
tk.Label(ventana6, text=listaTitulo[6],  font=fuente_definida1).pack(pady=5)
frame = tk.Frame(ventana6,bg="yellow")
frame.pack(padx=5, pady=5)

tk.Label(ventana6, text=listaTitulo[7],  font=fuente_definida1).pack(pady=5)

for i, (texCom, ejeCam) in enumerate(datosCom6):

    fila = i // 1  
    columna = i % 1
    

    tk.Label(frame, text=f"Solución a Ejecutar: {texCom}",  font=fuente_definida2).grid(row=fila, column=columna, sticky="w")
    tk.Button(frame, text=f"Ejecutar",  font=fuente_definida2, command=lambda cmd=ejeCam: ejecutarComando(cmd,5)).grid(row=fila, column=columna+ 1, sticky="w")



barraProgreso = ttk.Progressbar(ventana6, mode='determinate', length=200)
barraProgreso.pack()

tk.Button(ventana6, text="Volver al menú", command=mostrarMenu,  font=fuente_definida1).pack()
barrasProgreso.append(barraProgreso)

"""


ventana.mainloop()

