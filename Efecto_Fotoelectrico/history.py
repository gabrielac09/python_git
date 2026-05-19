5.499090833946989e-12,
1.6601518002881543e-10,
8.376156636548777e-12,
3.878143885933059e-12,
1.3266499161421596e-12,
1.4696938456699074e-12,
1.5999999999999998e-12,
1.4142135623730954e-12,
2.3380333616097096e-11,
2.729395537477117e-11,
2.135415650406263e-12,
1.5999999999999996e-12,
9.797958971132711e-13,
1.16619037896906e-12,
1.5999999999999996e-12,
8.519765254982088e-11,
5.7758116312774615e-12,
1.6248076809271914e-12,
1.7435595774162683e-12,
1.9595917942265422e-12,
1.3266499161421592e-12,
1.469693845669908e-12,
6.324555320336757e-13,
1.5999999999999996e-12,
1.6248076809271904e-12,
6.324555320336757e-13,
3.666060555964671e-12,
4.195235392680606e-12,
1.4675149062275316e-11,
9.797958971132703e-13,
1.939071942966532e-12,
2.135415650406262e-12,
7.483314773547878e-13,
4.000000000000012e-13,
1.496662954709576e-12,
2.785677655436825e-12,
1.85472369909914e-12,
8.000000000000001e-13,
1.7435595774162697e-12,
2.4132965006397374e-11,
1.2043521079817148e-10,
4.33589667773576e-12,
1.4142135623730947e-12,
1.2649110640673505e-12,
1.3564659966250537e-12,
1.7204650534085241e-12,
1.8330302779823347e-12,
3.3704599092705444e-12,
2.1939917957914067e-11,
3.1368774282716257e-12,
6.770524351924303e-12,
2.8705400188814638e-12,
4.223742416388576e-12,
6.086049621881174e-12,
8.64869932417586e-12]
voltaje_c_d = []
a=len(voltajes)

for i in range(0,a,1): 
    voltaje_c_d.append([ voltajes[i],corrientes[i], desvioestandar [i] ])
    
cadena_excel = ''
for fila in voltaje_c_d:
    cadena_excel += ','.join(map(str, fila)) + '\n'

# Imprimir la cadena formateada para Excel
print(cadena_excel)
corrientes=[1.139028e-07,
1.1262899999999998e-07,
1.114022e-07,
1.1008700000000001e-07,
1.0884879999999999e-07,
1.073444e-07,
1.05894e-07,
1.045034e-07,
1.028162e-07,
1.01349e-07,
9.96668e-08,
9.773359999999999e-08,
9.60178e-08,
9.400039999999999e-08,
9.20794e-08,
9.00488e-08,
8.78626e-08,
8.576820000000001e-08,
8.36488e-08,
8.123140000000002e-08,
7.88672e-08,
7.622419999999999e-08,
7.4002e-08,
7.143740000000001e-08,
6.86782e-08,
6.616999999999999e-08,
6.33178e-08,
6.05422e-08,
5.777059999999999e-08,
5.494199999999999e-08,
5.200239999999999e-08,
4.89744e-08,
4.61644e-08,
4.3112599999999995e-08,
4.0017999999999995e-08,
3.69354e-08,
3.41384e-08,
3.0957599999999997e-08,
2.91464e-08,
2.4966799999999997e-08,
2.2078e-08,
1.9461200000000002e-08,
1.6871e-08,
1.46382e-08,
1.2276e-08,
1.0289399999999999e-08,
9.696599999999999e-09,
6.8914000000000004e-09,
5.2994e-09,
4.045599999999999e-09,
3.0722e-09,
2.2098e-09,
1.5185999999999997e-09,
9.800000000000001e-10,
5.869999999999999e-10,
2.644e-10,
2.5999999999999997e-11,
-1.234e-10,
-2.4380000000000003e-10,
-3.432e-10,
-3.716e-10,
-4.008e-10,
-4.278e-10,
-4.412e-10,
-4.498e-10,
-4.614e-10,
-4.6360000000000003e-10,
-4.759999999999999e-10,
-4.548e-10,
-4.69e-10,
-4.772e-10,
-4.766e-10,
-3.6880000000000006e-10,
-4.716e-10,
-4.836000000000001e-10,
-4.89e-10,
-4.892e-10,
-4.935999999999999e-10,
-4.948e-10,
-4.952e-10,
-4.968e-10,
-4.97e-10,
-4.968e-10,
-4.959999999999999e-10,
-4.964000000000001e-10,
-4.982e-10,
-4.998000000000001e-10,
-5.008000000000001e-10,
-5.004e-10,
-5.014e-10,
-5.028000000000001e-10,
-5.044e-10,
-5.076e-10,
-5.086e-10,
-5.083999999999999e-10,
-5.087999999999999e-10,
-5.108e-10,
-5.104e-10,
-5.097999999999999e-10,
-5.092000000000001e-10]
desvioestandar=[6.399999999996669e-12,
1.4028542333401336e-11,
7.483314773513922e-13,
1.0315037566582252e-11,
9.797958971143822e-13,
4.029888335926547e-12,
5.830951894846011e-12,
1.3994284547629155e-11,
4.354308211415644e-12,
1.0119288512539825e-11,
7.0540768354179015e-12,
1.5882065356871835e-11,
6.8527366796019125e-12,
2.0591260281953644e-12,
9.046546302318053e-12,
1.1661903789703824e-12,
1.3676256797826902e-11,
6.399999999996669e-12,
5.600000000000394e-12,
3.77359245282215e-12,
1.1661903789703824e-12,
2.1802752119857712e-11,
2.9664793948416288e-12,
9.329523031753072e-12,
5.7061370470716636e-12,
1.080740486888774e-11,
2.4000000000027213e-12,
2.4000000000027213e-12,
5.9531504264539894e-12,
6.693280212272482e-12,
4.454211490263779e-12,
6.053098380167177e-12,
7.999999999979292e-13,
1.0198039027168581e-12,
1.3069047402163059e-11,
3.2000000000013124e-12,
6.864575733430096e-11,
3.454041111509879e-11,
2.6437291843152154e-10,
8.657944328765747e-12,
1.4751271131668433e-11,
1.2671227249166002e-11,
3.7947331922014754e-12,
4.241414858275476e-11,
5.30216182325662e-10,
1.8173453166638426e-10,
1.498090865067937e-09,
7.127580234553669e-11,
1.0461357464497638e-11,
5.314132102234431e-12,
5.344155686354932e-12,
8.611620056644338e-12,
3.878143885933052e-12,
3.794733192202032e-12,
4.472135954999601e-12,
2.870540018881467e-12,
7.79743547584717e-12,
6.770524351924299e-12,
5.418486873657629e-12,
2.199454477819444e-11,
9.604165762834381e-12,
1.1548160026601641e-11,
1.7204650534085363e-12,
9.797958971132869e-13,
1.5999999999999946e-12,
9.97196068985433e-12,
6.770524351924313e-12,
2.70628897200576e-11,
2.7701263509089272e-11,
1.2441864811996623e-11,
9.108238029388529e-12,
7.999999999999972e-13,
1.193338175036733e-10,
7.1999999999999936e-12,
3.3226495451672186e-12,
2.8284271247461802e-12,
3.4292856398964377e-12,
2.4166091947189555e-12,
1.326649916142196e-12,
2.0396078054371413e-12,
1.3266499161421554e-12,
1.6733200530681454e-12,
9.797958971132679e-13,
2.3664319132398645e-12,
1.624807680927217e-12,
1.7204650534085195e-12,
7.483314773547856e-13,
1.5999999999999944e-12,
1.0198039027185535e-12,
1.7435595774162633e-12,
2.7129319932500977e-12,
4.841487374764065e-12,
4.898979485566339e-13,
2.059126028197393e-12,
2.416609194718906e-12,
2.785677655436814e-12,
9.797958971132679e-13,
7.999999999999971e-13,
3.05941170815566e-12,
1.3266499161421556e-12]
voltajes
corrientes
desvioestandar=[6.399999999996669e-12,
1.4028542333401336e-11,
7.483314773513922e-13,
1.0315037566582252e-11,
9.797958971143822e-13,
4.029888335926547e-12,
5.830951894846011e-12,
1.3994284547629155e-11,
4.354308211415644e-12,
1.0119288512539825e-11,
7.0540768354179015e-12,
1.5882065356871835e-11,
6.8527366796019125e-12,
2.0591260281953644e-12,
9.046546302318053e-12,
1.1661903789703824e-12,
1.3676256797826902e-11,
6.399999999996669e-12,
5.600000000000394e-12,
3.77359245282215e-12,
1.1661903789703824e-12,
2.1802752119857712e-11,
2.9664793948416288e-12,
9.329523031753072e-12,
5.7061370470716636e-12,
1.080740486888774e-11,
2.4000000000027213e-12,
2.4000000000027213e-12,
5.9531504264539894e-12,
6.693280212272482e-12,
4.454211490263779e-12,
6.053098380167177e-12,
7.999999999979292e-13,
1.0198039027168581e-12,
1.3069047402163059e-11,
3.2000000000013124e-12,
6.864575733430096e-11,
3.454041111509879e-11,
2.6437291843152154e-10,
8.657944328765747e-12,
1.4751271131668433e-11,
1.2671227249166002e-11,
3.7947331922014754e-12,
4.241414858275476e-11,
5.30216182325662e-10,
1.8173453166638426e-10,
1.498090865067937e-09,
7.127580234553669e-11,
1.0461357464497638e-11,
5.314132102234431e-12,
5.344155686354932e-12,
8.611620056644338e-12,
3.878143885933052e-12,
3.794733192202032e-12,
4.472135954999601e-12,
2.870540018881467e-12,
7.79743547584717e-12,
6.770524351924299e-12,
5.418486873657629e-12,
2.199454477819444e-11,
9.604165762834381e-12,
1.1548160026601641e-11,
1.7204650534085363e-12,
9.797958971132869e-13,
1.5999999999999946e-12,
9.97196068985433e-12,
6.770524351924313e-12,
2.70628897200576e-11,
2.7701263509089272e-11,
1.2441864811996623e-11,
9.108238029388529e-12,
7.999999999999972e-13,
1.193338175036733e-10,
7.1999999999999936e-12,
3.3226495451672186e-12,
2.8284271247461802e-12,
3.4292856398964377e-12,
2.4166091947189555e-12,
1.326649916142196e-12,
2.0396078054371413e-12,
1.3266499161421554e-12,
1.6733200530681454e-12,
9.797958971132679e-13,
2.3664319132398645e-12,
1.624807680927217e-12,
1.7204650534085195e-12,
7.483314773547856e-13,
1.5999999999999944e-12,
1.0198039027185535e-12,
1.7435595774162633e-12,
2.7129319932500977e-12,
4.841487374764065e-12,
4.898979485566339e-13,
2.059126028197393e-12,
2.416609194718906e-12,
2.785677655436814e-12,
9.797958971132679e-13,
7.999999999999971e-13,
3.05941170815566e-12,
1.3266499161421556e-12]
voltaje_c_d = []
a=len(voltajes)

for i in range(0,a,1): 
    voltaje_c_d.append([ voltajes[i],corrientes[i], desvioestandar [i] ])


# Generar una cadena formateada para Excel
cadena_excel = ''
for fila in voltaje_c_d:
    cadena_excel += ','.join(map(str, fila)) + '\n'

# Imprimir la cadena formateada para Excel

print(cadena_excel)
runfile('C:/Users/gabri/.spyder-py3/CODIGO FOTOELECTRICO_2.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Wed Mar  6 15:27:14 2024)---
runfile('C:/Users/gabri/.spyder-py3/CODIGO FOTOELECTRICO_2.py', wdir='C:/Users/gabri/.spyder-py3')
rm = visa.ResourceManager()
rm.list_resources()
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

vi = -2  # Voltaje inicial (en mV)
vf = 3  # Voltaje final (en mV)
step = 0.05  # Paso (en mV)
runfile('C:/Users/gabri/.spyder-py3/CODIGO FOTOELECTRICO_2.py', wdir='C:/Users/gabri/.spyder-py3')
import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import time
runfile('C:/Users/gabri/.spyder-py3/CODIGO FOTOELECTRICO_2.py', wdir='C:/Users/gabri/.spyder-py3')
rm.list_resources()
electrometro = rm.open_resource('GPIB0::27::INSTR')
electrometro.write(':SOUR:VOLT:MCON 1')
electrometro.write(':SENS:CURR:RANG:AUTO 1')
electrometro.write(':SENS:RES:MAN:VSO:OPER 1')
electrometro.timeout = 1000
electrometro.encoding = 'ascii'
electrometro.query_delay = 0.05
electrometro.write(':SENS:RES:MAN:VSO:OPER 0')
electrometro.write(':SENS:RES:MAN:VSO:OPER 1')
electrometro.write(':SOUR:VOLT ' +str(0))
runfile('C:/Users/gabri/.spyder-py3/CODIGO FOTOELECTRICO_2.py', wdir='C:/Users/gabri/.spyder-py3')
import pyvisa as visa
electrometro = rm.open_resource('GPIB0::27::INSTR')
rm.list_resources()
runfile('C:/Users/gabri/.spyder-py3/CODIGO FOTOELECTRICO_2.py', wdir='C:/Users/gabri/.spyder-py3')
rm.open_resource('GPIB0::27::INSTR')
open_resource('GPIB0::27::INSTR')
rm.open_resource('GPIB0::27::INSTR')
electrometro = texto.open_resource('GPIB0::27::INSTR')
electrometro = rm.open_resource('GPIB0::27::INSTR')
runfile('C:/Users/gabri/.spyder-py3/CODIGO FOTOELECTRICO_2.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Mon Mar 11 17:29:46 2024)---
rm = visa.ResourceManager()
import pyvisa as visa
rm = visa.ResourceManager()
rm.list_resources()
analizador_espectro = rm.open_resource('USB0::0x1AB1::0x0960::DSA8A163250968::INSTR')
rm = visa.ResourceManager()
rm.list_resources()
analizador_espectro = rm.open_resource('USB0::0x1AB1::0x0960::DSA8A163250968::INSTR')

## ---(Wed Mar 20 18:15:32 2024)---
rm = visa.ResourceManager()
import pyvisa as visa
rm = visa.ResourceManager()
rm.list_resources()

## ---(Wed Apr 17 15:53:11 2024)---
rm = visa.ResourceManager()
import pyvisa as visa
rm = visa.ResourceManager()
rm.list_resources()
loquisimo=rm.open_resource('GPIB0::12::INSTR')
import pyvisa as visa
rm = visa.ResourceManager()
rm.list_resources()
osciloscopio =rm.open_resource('USB0::0x1AB1::0x04B0::DS2D163351648::INSTR')
rm.list_resources()
rm = visa.ResourceManager()
rm.list_resources()
rm = visa.ResourceManager()
rm.list_resources()

## ---(Wed Apr 17 17:21:13 2024)---
rm = visa.ResourceManager()
import pyvisa as visa
rm = visa.ResourceManager()
rm.list_resources()
osciloscopio =rm.open_resource('USB0::0x1AB1::0x04B0::DS2D163351648::INSTR')
runcell(0, 'D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py')
runfile('D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py', wdir='D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3')
rm.list_resources()
runcell(0, 'D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py')
import pyvisa as visa

# Configura la conexión con el osciloscopio utilizando PyVISA
rm = visa.ResourceManager()
osc = rm.open_resource('USB0::0x1AB1::0x04B1::DS2A204001234::INSTR', timeout=10000)

try:
    # Consulta la identificación del osciloscopio
    print("Identificación del osciloscopio:", osc.query("*IDN?"))

except visa.VisaIOError as e:
    print("Error de comunicación con el osciloscopio:", e)

finally:
    # Cierra la conexión con el osciloscopio al finalizar
    osc.close()
    
import pyvisa as visa

# Configura la conexión con el osciloscopio utilizando PyVISA
rm = visa.ResourceManager()
osc = rm.open_resource('USB0::0x1AB1::0x04B0::DS2D163351648::INSTR', timeout=10000)

try:
    # Consulta la identificación del osciloscopio
    print("Identificación del osciloscopio:", osc.query("*IDN?"))

except visa.VisaIOError as e:
    print("Error de comunicación con el osciloscopio:", e)

finally:
    # Cierra la conexión con el osciloscopio al finalizar
    osc.close()
    
runcell(0, 'D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py')
runfile('D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py', wdir='D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3')
print("Identificación del osciloscopio:", osc.query("*IDN?"))
runfile('D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py', wdir='D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3')
rm = visa.ResourceManager()
osc = rm.open_resource('USB0::0x1AB1::0x04B0::DS2D163351648::INSTR', timeout=10000)
print("Identificación del osciloscopio:", osc.query("*IDN?"))
osc.write(":STOP")  # Detiene la adquisición si está en ejecución
osc.write(":WAV:MODE RAW")  # Modo de datos sin procesar (raw waveform data)
osc.write(":WAV:FORM BYTE")  # Formato de datos en bytes (sin procesar)
osc.write(":WAV:SOUR CHAN1")  # Canal de origen (por ejemplo, Canal 1)
osc.write(":WAV:DATA?")  # Solicita datos de forma de onda
print("2. Identificación del osciloscopio:", osc.query("*IDN?"))
runfile('D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py', wdir='D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3')
runcell(0, 'D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py')
runfile('D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py', wdir='D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3')
runcell(0, 'D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py')
runfile('D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py', wdir='D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3')
sample_rate = float(osc.query(":ACQ:SAMPRT?"))  # Consulta la tasa de muestreo
sample_rate = float(osc.query(":ACQ:SAMPRT?"))
runcell(0, 'D:/Gabriela Lapto 19112023/BALSEIRO/2do cuatrimestre/Laboratorio II/LAB_3/lockin_osciloscopio.py')
sample_rate = #float(osc.query(":ACQ:SAMP?"))
sample_rate = float(osc.query(":ACQ:SAMP?"))
sample_rate = float(osc.query(":ACQ:SAMPRT?"))

## ---(Mon Apr 22 17:50:02 2024)---
import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import time
# busca el instrumento e inicializa la comunicacion
rm = visa.ResourceManager()

# enlista los puertos usb
rm.list_resources()
rm.list_resources()
runfile('C:/Users/gabri/untitled0.py', wdir='C:/Users/gabri')
loquisimo
loquisimo.write(f"FREQ {1000}")
loquisimo.write(f"")
loquisimo.write("OF 10000 3")
rm.list_resources()
# busca el instrumento e inicializa la comunicacion

rm = visa.ResourceManager()


# enlista los puertos usb
rm.list_resources()
# busca el instrumento e inicializa la comunicacion


rm = visa.ResourceManager()


# enlista los puertos usb
rm.list_resources()
# busca el instrumento e inicializa la comunicacion



rm = visa.ResourceManager()


# enlista los puertos usb
rm.list_resources()

## ---(Mon Apr 22 19:09:07 2024)---
rm = visa.ResourceManager()
import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import time
rm.list_resources()
rm = visa.ResourceManager()
rm.list_resources()
loquisimo = rm.open_resource('GPIB0::12::INSTR')
loquisimo.write("OF 10000 3")
loquisimo.write("OF 50000 3")
loquisimo.write("OF 5000 4")
loquisimo.write("OF 12000 1")

## ---(Wed Apr 24 15:45:35 2024)---
import pyvisa as visa
import numpy as np

import matplotlib.pyplot as plt
import time
rm = visa.ResourceManager()
rm.list_resources()

## ---(Wed Apr 24 15:53:41 2024)---
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
rm = visa.ResourceManager()
import pyvisa as visa
rm = visa.ResourceManager()
rm.list_resources()

## ---(Wed Apr 24 16:12:26 2024)---
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
import pyvisa as visa
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
rm = visa.ResourceManager()
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
rm.list_resources()
import pyvisa as visa
rm
rm = visa.ResourceManager()
rm.list_resources()
rm = visa.ResourceManager()
rm.list_resources()
rm = visa.ResourceManager()
rm.list_resources()

## ---(Wed Apr 24 16:35:17 2024)---
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
rm.list_resources()
rm = visa.ResourceManager()
rm.list_resources()
rm = visa.ResourceManager()
rm.list_resources()
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
rm.list_resources()

## ---(Wed Apr 24 17:08:22 2024)---
import pyvisa as visa
rm = visa.ResourceManager()
rm.list_resources()
rm = visa.ResourceManager()
rm.list_resources()
rm.visalib
rm = visa.ResourceManager()
rm.list_resources()
loquisimo = rm.open_resource('GPIB0::12::INSTR')
loquisimo.write('OF 12000 1')
loquisimo.write('OF 1200 1')
loquisimo.write('TC [4]')
loquisimo.write('TC [10]')
loquisimo.write('TC[10]')
loquisimo.write('TC[]')
loquisimo.write(TC[0])
loquisimo.write('TC[0]')
loquisimo.write('TC 0')
loquisimo.write('TC 5')
loquisimo.write('OF 12000 1')
loquisimo.write('OF 14000 1')
rm = visa.ResourceManager()
rm.list_resources()
loquisimo.write('OF 10000 3')
loquisimo = rm.open_resource('GPIB0::12::INSTR')
loquisimo.write('OF 10000 3')
rm.list_resources()
loquisimo.write('OF 10000 3')
rm = visa.ResourceManager()
rm.list_resources()
loquisimo = rm.open_resource('GPIB0::12::INSTR')
loquisimo.write('OF 10000 3')
loquisimo.write("OF 10000 3")
loquisimo.write("OF 10000 3\r")
loquisimo.write("OF 10000 3\n")
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
loquisimo.write("OF 10000 3\r")
rm.list_resources()
loquisimo.write("OF 10000 3")
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
lock_in=write('TC 0')
lock_in.write('TC 5')
lock_in.write('TC 4')
lock_in.write('FLT 1')
lock_in.write('FLT 0')
lock_in.write('D2 3')
lock_in.write('D2 4')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
n2,m = 0,3
n2
m
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
def conversion_freq_comando(1000):
    
    
comand= conversion_freq_comando(1000)    
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
comand= conversion_freq_comando(1000)
comand
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
comand= conversion_freq_comando(1000)
comand
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
comand
comand= conversion_freq_comando(1000)
comand
loquisimo.write("OF 120000 5")
lock_in.write("OF 120000 5")
lock_in.write('OF 120005')
lock_in.write('OF 12000 5')
rm.list_resources()
lock_in.write('OF 12000 5')
lock_in.write('OF 10000 3')
lock_in.write('OF 120000 5')
lock_in.write('OF 2000 5')
lock_in.write('OF 8000 5')
lock_in.write('OF 10000 5')
lock_in.write('OF 12000 5')

## ---(Mon Apr 29 15:05:09 2024)---
import pyvisa as visa
rm = visa.ResourceManager()
rm.list_resources()
lock_in=rm.open_resource('GPIB0::12::INSTR')
voltajes_base = [0.5,1,1.5]
lock_in.write('OF 12000 5')
lock_in.write('OF 2000 5')
lock_in.write('NN')
lock_in.query('NN')
def get_NN():
    try:
        return lockin.query('NN')
    except:
        print('ERROR')
        get_NN()
        
get_NN
def get_NN():
    try:
        return lock_in.query('NN')
    except:
        print('ERROR')
        get_NN()
        
get_NN()
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
lock_in.write(conversion_freq_comando(frecuencias[1]))
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
lock_in.query('NN')
lock_in.write('NN')
n=lock_in.write('NN')
n
n=lock_in.query('NN')
n
n=lock_in.query('NN')
n
n=lock_in.query('NN')
n
n/100
n
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
rm.list_resources()
lock_in.write('FLT 0')
lock_in.query('FLT 0')
lock_in.write('FLT 0')
lock_in.write('FLT 1')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
lock_in.write('LF 3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
lock_in.write('TC 6')
lock_in.write('TC 5')
lock_in.write('TC 6')
lock_in.write('TC 1')
lock_in.write('TC 6')
rm.list_resources()
rm = visa.ResourceManager()
lock_in=rm.open_resource('GPIB0::12::INSTR')
lock_in.write('TC 6')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
lock_in.read('SEN')
m=conversion_freq_comando(0.5)
m
freq=5000.0
freq = int(freq)
freq
m=conversion_freq_comando(0.5)
m
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
n = lock_in.query('NN')
n = int(n.rstrip('\r'))
return n
n = lock_in.query('NN')
n=lock_in.query('NN')
n=lock_in.read('NN')
n=lock_in.query('NN')
get_NN()
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
get
get_NN()
n = lock_in.query('NN')
m=conversion_freq_comando(i)
m=conversion_freq_comando(0.5)
lock_in.write('m')
m=conversion_freq_comando(10)
lock_in.write('m')
lock_in.write(m)
m
m=conversion_freq_comando(10)
m
x=conversion_freq_comando(1)
x=conversion_freq_comando(1000)
x
m=conversion_freq_comando(0.5)
m
lock_in.write(m)
m=conversion_freq_comando(150)
m=conversion_freq_comando(0.5)
m
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
m=conversion_freq_comando(10000)
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
m=conversion_freq_comando(10000)
m
m=conversion_freq_comando(0.5)
m=conversion_freq_comando(10)
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
m=conversion_freq_comando(10)
m=conversion_freq_comando(120000)
get_NN
get_NN()
lock_in.read('SEN()')
lock_in.read('SEN')
get_NN()
m=conversion_freq_comando(1000)
lock_in.write(m)
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
mediciones = []
for i in range(5):
    mediciones.append(get_NN())
    time.sleep(1)
amplitud_prom=(sum(mediciones) / len(mediciones))
get_NN()
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
get_NN()
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
import numpy as np
import matplotlib.pyplot as plt
import wave
from scipy.io import wavfile
import soundfile as sf
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import time
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
    #imagen en m
def get_NN():
    try:
        n = lock_in.query('NN')
        n = int(n.rstrip('\r'))
        return n
    except:
        print('ERROR')
        return EOFError

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
# busca el instrumento e inicializa la comunicacion
rm = visa.ResourceManager()


rm.list_resources()
rm.list_resources()


rm = visa.ResourceManager()

# enlista los puertos usb y defino la salida como
rm.list_resources()
lock_in=rm.open_resource('GPIB0::12::INSTR')
rm = visa.ResourceManager()
rm.list_resources()
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Mon Apr 29 18:26:35 2024)---
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
n = lock_in.query('NN')
n
n = int(n.rstrip('\r'))
n
n+5
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
get_NN()
n = lock_in.query('NN')
rm.list_resources()
n = lock_in.query('NN')
m = lock_in.query('NN')
n
n = lock_in.query('NN')
lock_in.query('NN')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
n = lock_in.query('NN')
n
n = int(n.rstrip('\r'))
n
n = lock_in.query('NN')
runcell(0, 'C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py')
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
lock_in.query('SEN')

## ---(Wed May  8 15:34:08 2024)---

rm = visa.ResourceManager()

# enlista los puertos usb y defino la salida como
rm.list_resources()
lock_in=rm.open_resource('GPIB0::12::INSTR')
import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import time
rm = visa.ResourceManager()

# enlista los puertos usb y defino la salida como
rm.list_resources()
lock_in=rm.open_resource('GPIB0::12::INSTR')
rm.list_resources()
n = lock_in.query('NN')
n
n = int(n.rstrip('\r'))
n
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Mon May 13 15:20:57 2024)---
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')
kl
kj

hgjh
hg
g
runfile('C:/Users/gabri/.spyder-py3/CODIGO LOCK-IN - Ruido Jhonson.py', wdir='C:/Users/gabri/.spyder-py3')