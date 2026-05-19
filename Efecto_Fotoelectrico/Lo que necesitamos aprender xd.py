# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:24:12 2024

@author: gabri

"""
# Lo que necesitamos hacer e:
#     prender la fuente
    
#     setear un valor de voltaje
#     guardar ese valor en una variable
#     medir la corriente
#     guardar el valor de la corriente 
    
#     repetir



# busca el instrumento e inicializa la comunicacion
rm = visa.ResourceManager()

# enlista los puertos usb
rm.list_resources()

electrometro = rm.open_resource('GPIB0::27::INSTR')


# prende la fuente
electrometro.write(':SENS:RES:MAN:VSO:OPER 1')


# apaga la fuente
electrometro.write('SENS:RES:MAN:VSO:OPER 0'))

# setea 0.1v en la fuente 
electrometro.write(':SENS:RES:MAN:VSO:AMPL 0.1') === electrometro.write(':SOUR:VOLT 0.1')

# conecta la fuente de voltaje con rl amperimetro (hace andar el electrometro)
electrometro.write(':SOUR:VOLT:MCON 1')

#esto me lee la corriente
electrometro.write(':DISP:DATA?')
electrometro.read()

    

    