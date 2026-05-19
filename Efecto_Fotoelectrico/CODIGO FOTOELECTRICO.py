# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:10:01 2024

@author: gabri
"""

import pyvisa as visa
import matplotlib.pyplot as plt
import time


def electrometro_set(comm):
    electrometro.write(comm)
    
    
def current():
    electrometro.write(':READ?')
    v=electrometro.read()
    c=v.split(',')[0]
    return float(c[:-4])


def current_promedio5():
    mediciones = []
    for i in range(5):
        mediciones.append(current())
        time.sleep(0.01)   
    return (sum(mediciones) / len(mediciones))

    
def imprimir_datos_plot(voltajes, corrientes):
    # Graficar los datos
    plt.plot(voltajes, corrientes, marker='o', linestyle='-')
    plt.xlabel('Tension (V)')
    plt.ylabel('Corriente (A)')
    plt.title('Voltaje vs Corriente \u03BB=449nm')
    plt.grid(True)
    plt.show()
    
    


# busca el instrumento e inicializa la comunicacion
rm = visa.ResourceManager()
electrometro = rm.open_resource('GPIB0::27::INSTR')

# conecta la fuente de voltaje con rl amperimetro (hace andar el electrometro)
electrometro_set(':SOUR:VOLT:MCON 1')

#modifica el rango de trabajo de la corriente
electrometro.write(':SENS:CURR:RANG:AUTO 1')

#prende la fuete
electrometro_set(':SENS:RES:MAN:VSO:OPER 1')

electrometro.timeout = 1000
electrometro.encoding = 'ascii'
electrometro.query_delay = 0.05

vi = 0  # Voltaje inicial (en mV)
vf = 1.5  # Voltaje final (en mV)
step = 0.05  # Paso (en mV)

#Creo listas para almacenar los datos 
voltajes = []
corrientes = []

electrometro_set(':SOUR:VOLT ' +str(vi))

time.sleep(0.5)

for v in range(int(vi * 100), int(vf * 100), int(step * 100)):
    v/=100
    electrometro_set(':SOUR:VOLT ' + str(v))
    time.sleep(0.5) 
    print("Voltaje seteada:", float(v))      
    corriente = current_promedio5();
    print("Corriente medida promedio:", corriente)       #solo puedo medir la corriente
    voltajes.append(float(v))
    corrientes.append(-corriente)



# apaga la fuente
electrometro_set(':SENS:RES:MAN:VSO:OPER 0')

#cierro electrometro
electrometro.close()


# Llamada a la función
imprimir_datos_plot(voltajes, corrientes)


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