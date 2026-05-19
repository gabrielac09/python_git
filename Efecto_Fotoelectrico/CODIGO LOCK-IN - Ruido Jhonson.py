# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:52:02 2024

@author: gabri
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:10:01 2024

@author: gabri
"""

import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import time



   
# def current():
#     electrometro.write(':READ?')
#     v=electrometro.read()
#     c=v.split(',')[0]
#     return float(c[:-4])

    
def imprimir_datos_plot(voltajes, corrientes):
    # Graficar los datos
    plt.plot(voltajes, corrientes, marker='o', linestyle='-')
    plt.xlabel('Tension (V)')
    plt.ylabel('Corriente (A)')
    plt.title('Tension vs Corriente \u03BB=450nm menos intensidad 6')
    plt.grid(True)
    plt.show()
    
def conversion_freq_comando(f):
    # selecciona el n2
    n2,m = 0,4
    if( 2 <= f <= 20 ):
        n2,m = 1,2
    elif (20 <= f <= 200):
        n2,m = 2,0
    elif (200 <= f <= 2000):
        n2,m = 3,-2
    elif (2000 <= f <= 20000):
        n2,m = 4,-4
    elif (20000 <= f <= 120000):
        n2,m = 5,-6   
    
    freq=f*10**(n2+m)
    freq = int(freq)
    return 'OF'+ ' '+str(freq)+' '+str(n2)
    #12hz es 12000 en 1  --> OF 12000 1
    #5kHz es 5000 en 4
    #imagen en mi tlf, de 2 pasa a 2000 hasta 20 que pasa a 20000 a todo le multiplica mil pero cambia con el rango de trabajo


#CONVERTIR TAMBIEN SEN A NMERO

def get_NN():
    try:
        n = lock_in.query('NN')
        n = int(n.rstrip('\r'))
        return n
    except Exception as e:
        print('ERROR:', e)
        return None


# busca el instrumento e inicializa la comunicacion
rm = visa.ResourceManager()

# enlista los puertos usb y defino la salida como
rm.list_resources()
lock_in=rm.open_resource('GPIB0::12::INSTR')

#fijo el filtro en flat
lock_in.write('FLT 0')
time.sleep(3)

#fijo el filtro en line reject 2ff
lock_in.write('LF 3')
time.sleep(3)

#fijo el tipo de lockin en noise
lock_in.write('D2 4')
time.sleep(3)

#fijo la constante de tiempoo en 1s
lock_in.write('TC 6')
time.sleep(3)

#agregar otras frecuencias

frecuencias=[0.5,1,1.5,10,15,20,300,400,500,1000,1500,2000,3000,5000] #frecuencias de trabajo (en Hz)
frecuencia=[1,10,100,1000,10000] 
amplitud=[]
desvioestandar=[]

for freq in frecuencias:
    lock_in.write(conversion_freq_comando(freq))
    time.sleep(10) 
    input("Presiona Enter para continuar...")
    mediciones = []
    for _ in range(5):
        medicion = get_NN()
        if medicion is not None:  # Verificar si la medición es válida
            mediciones.append(medicion/100)
        time.sleep(1)
    if mediciones:  # Verificar si hay mediciones válidas
        amplitud_prom = sum(mediciones) / len(mediciones)
        print("Frecuencia seteada:", freq) 
        print("Amplitud medida promedio:", amplitud_prom)      
        print("Desviación estándar de amplitudes:", np.std(mediciones))  
        amplitud.append(amplitud_prom)
        desvioestandar.append(np.std(mediciones))
    else:
        # Si no hay mediciones válidas, agregamos NaN a los vectores para mantener la alineación
        print("No se encontraron mediciones válidas para la frecuencia:", freq)
        amplitud.append(np.nan)
        desvioestandar.append(np.nan)
    

      
      
voltaje_c_d = []
a=len(frecuencias)

for i in range(0,a,1): 
    voltaje_c_d.append([ frecuencias[i],amplitud[i], desvioestandar [i] ])


# Generar una cadena formateada para Excel
cadena_excel = ''
for fila in voltaje_c_d:
    cadena_excel += ','.join(map(str, fila)) + '\n'

# Imprimir la cadena formateada para Excel
print(cadena_excel)
      






# for v in range(int(vi * 100), int(vf * 100), int(step * 100)):
#     v/=100
#     electrometro_set(':SOUR:VOLT ' + str(v))
#     time.sleep(0.1) 
#     mediciones = []
#     for i in range(5):
#         mediciones.append(current())
#     corriente_prom=(sum(mediciones) / len(mediciones))
#     print("Voltaje seteada:", float(v)) 
#     print("Corriente medida promedio:", corriente_prom)      
#     print("Desviacion estandar de corriente:", np.std(mediciones))  
#     voltajes.append(float(v))
#     corrientes.append(-corriente_prom)
#     desvioestandar.append(np.std(mediciones))







        

    # a partir de f, obtiene un numero entre 2000 y 20000.
    # # quiero que, por ejemplo, para n = 2,
    # # si f = 20, me devuelva 2000, y si f = 200, me devuelva 20000.
    # if(n2 <= 5):
    #     lockin_freq = lambda x: 2000 + 18000*(x - 2*10**(n2-1))/(2*10**(n2) - 2*10**(n2-1))
    # command = 'OF {freq} {n2}\r'.format(freq=int(lockin_freq(f))
    #                                   , n2=n2)
    # print(command)
    # lockin.write(command)



 


# # conecta la fuente de voltaje con rl amperimetro (hace andar el electrometro)
# electrometro_set(':SOUR:VOLT:MCON 1')

# #modifica el rango de trabajo de la corriente
# electrometro.write(':SENS:CURR:RANG:AUTO 1')

# #prende la fuete, aca puedo usar directamente el write
# electrometro_set(':SENS:RES:MAN:VSO:OPER 1')
# electrometro.write(comm)

# electrometro.timeout = 1000
# electrometro.encoding = 'ascii'
# electrometro.query_delay = 0.05

# vi = -2  # Voltaje inicial (en mV)
# vf = 3  # Voltaje final (en mV)
# step = 0.05  # Paso (en mV)

# #Creo listas para almacenar los datos 
# voltajes = []
# corrientes = []
# desvioestandar = []

# electrometro_set(':SOUR:VOLT ' +str(vi))

# time.sleep(0.1)

# for v in range(int(vi * 100), int(vf * 100), int(step * 100)):
#     v/=100
#     electrometro_set(':SOUR:VOLT ' + str(v))
#     time.sleep(0.1) 
#     mediciones = []
#     for i in range(5):
#         mediciones.append(current())
#     corriente_prom=(sum(mediciones) / len(mediciones))
#     print("Voltaje seteada:", float(v)) 
#     print("Corriente medida promedio:", corriente_prom)      
#     print("Desviacion estandar de corriente:", np.std(mediciones))  
#     voltajes.append(float(v))
#     corrientes.append(-corriente_prom)
#     desvioestandar.append(np.std(mediciones))



# # apaga la fuente
# electrometro_set(':SENS:RES:MAN:VSO:OPER 0')

# #cierro electrometro
# electrometro.close()

# voltaje_c_d = []
# a=len(voltajes)

# for i in range(0,a,1): 
#     voltaje_c_d.append([ voltajes[i],corrientes[i], desvioestandar [i] ])
    

# # Generar una cadena formateada para Excel
# cadena_excel = ''
# for fila in voltaje_c_d:
#     cadena_excel += ','.join(map(str, fila)) + '\n'

# # Imprimir la cadena formateada para Excel
# print(cadena_excel)

    


# # Llamada a la función
# imprimir_datos_plot(voltajes, corrientes)






#esto no funca, se supone que merchearia pero no lo hace
# matriz_xy = [[float(x), float(y)] for x, y in zip(voltajes, corriente)]

# print("Matriz nx2 formada por las listas x e y:")
# print(matriz_xy)


# plt.plot(voltajes,corrientes, marker='o',linestyle='-')
# plt.xlabel('Tension (V)')
# plt.ylabel('Corriente (A)')
# plt.title('tensión vs. Corriente')
# plt.show()

# # setea 0.1v en la fuente 
# electrometro.write(':SENS:RES:MAN:VSO:AMPL 0.1') === electrometro.write(':SOUR:VOLT 0.1')

# # conecta la fuente de voltaje con rl amperimetro (hace andar el electrometro)
# electrometro.write(':SOUR:VOLT:MCON 1')

# #esto me lee la corriente
# electrometro.write(':DISP:DATA?')
# electrometro.read()

# #este lee la corriente de una forma mas segura
# electrometro.write(':READ?')
# v=electrometro.read()
# c=v.split(',')[0]
# print(float(c[:-4]))