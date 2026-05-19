# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyvisa as visa
import time

def electrometro_set(comm):
    electrometro.write(comm)

def electrometro_read():
    return electrometro.query_ascii_values('READ?')[0]  # Suponiendo que 'READ?' es el comando para obtener la corriente
        
rm = visa.ResourceManager()

electrometro = rm.open_resource('GPIB0::27::INSTR')

# Configura los parámetros de comunicación del electrometro
#electrometro.baud_rate = 115200
#electrometro.data_bits = 8
#electrometro.parity = visa.constants.Parity.even
#electrometro.stop_bits = visa.constants.StopBits.one
electrometro.timeout = 1000
electrometro.encoding = 'ascii'
electrometro.query_delay = 0.05
#electrometro.write_termination = '\n'
# electrometro.read_termination = '\n'

# Configura los parámetros de la fuente
#electrometro = rm.open_resource('dirección_de_tu_fuente')

vi = 0  # Voltaje inicial (en mV)
vf = 1000  # Voltaje final (en mV)
step = 100  # Paso (en mV)

electrometro_set('svoltage ' + str(vi))

time.sleep(5.0)
for v in range(vi, vf, step):
    electrometro_set('svoltage ' + str(v))
    vset = electrometro_read()  # No se usa electrometro_set aquí, sino electrometro_read
    print("Voltaje seteado:", float(vset))      
    corriente = electrometro_read()
    print("Corriente medida:", corriente)       #solo puedo medir la corriente
    time.sleep(1.0)

electrometro.close()
fuente.close()