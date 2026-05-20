import time
import serial
import numpy as np
import matplotlib.pyplot as plt

#############################################
# Nota:
# Comentar esta linea si se utiliza el puerto serie
# con la FPGA
ser = serial.serial_for_url('loop://', timeout=1)

ser.isOpen()
ser.timeout=None
ser.flushInput()
ser.flushOutput()


class RaisedCosineFilter:
    def __init__(self, alpha=0.25, span=6, sps=8, rrc=True):
        """
        Filtro de coseno realzado o raíz de coseno realzado.
        
        Parámetros:
        - alpha: Factor de roll-off (0 <= alpha <= 1)
        - span: Duración total del filtro en símbolos 
        - sps: Muestras por símbolo
        - rrc: Si True, genera raíz de coseno realzado; si False, coseno realzado
        -> si quiero que el beta sea esto 1 estoy teniendo mucho ancho de banda y la señal es lo mas parecida a un pulso y seria lo ideal pero consume mucho ancho de banda
        si cambio un poco el beta a 0.5 o 0.25 la señal se va a parecer un poco menos a un pulso pero consume menos ancho de banda
         
        -> si alpha es mas cercano a cero comprimo mas abrupta es la caida del filtro comprimo en frecuencia, expando en tiempo
        -> cual es la resolucion que debo usar en cada coeficiente, cuantos coeficientes y la atenuacion maxima que necesitaria tener en base a la resolucion y cantidad de coeficientes
        -> el filtro de RCC es una cuadrada con alpha cero, en cuanto mas lo relaj llevando el alfa a 1 se suavia mas y pasa a tener mas ancho de banda
        """
        self.alpha = alpha
        self.span = span
        self.sps = sps
        self.rrc = rrc
        self.taps = self._generate_filter()

    def _generate_filter(self):

        T = 1  # Duración del símbolo (normalizado)
        N = self.span * self.sps
        t = np.arange(-N//2, N//2 + 1) / self.sps

        if self.rrc:
            # Filtro Root Raised Cosine
            h = np.zeros_like(t)
            for i in range(len(t)):
                ti = t[i]
                if ti == 0.0:
                    h[i] = 1.0 - self.alpha + (4 * self.alpha / np.pi)
                elif abs(ti) == T / (4 * self.alpha):
                    h[i] = (self.alpha / np.sqrt(2)) * (
                        ((1 + 2/np.pi) * (np.sin(np.pi/(4*self.alpha)))) +
                        ((1 - 2/np.pi) * (np.cos(np.pi/(4*self.alpha))))
                    )
                else:
                    h[i] = (np.sin(np.pi * ti * (1 - self.alpha) / T) +
                            4 * self.alpha * ti / T *
                            np.cos(np.pi * ti * (1 + self.alpha) / T)) / \
                           (np.pi * ti * (1 - (4 * self.alpha * ti / T) ** 2))
        else:
            # Filtro Raised Cosine clásico
            h = np.zeros_like(t)
            for i in range(len(t)):
                ti = t[i]
                if ti == 0.0:
                    h[i] = 1.0
                elif abs(ti) == T / (2 * self.alpha):
                    h[i] = (np.pi / 4) * np.sinc(1 / (2 * self.alpha))
                else:
                    h[i] = np.sinc(ti / T) * \
                           np.cos(np.pi * self.alpha * ti / T) / \
                           (1 - (2 * self.alpha * ti / T) ** 2)

        return h

    def plot(self, time_domain=True, freq_domain=False, plot_type=1):

        t = np.arange(-len(self.taps)//2, len(self.taps)//2 + 1) / self.sps
        plt.figure(figsize=(10,8))

        if time_domain:
            plt.subplot(2,1,1)
            if plot_type == 0:   plt.stem(t[:len(self.taps)], self.taps, label="Impulse Response")
            elif plot_type == 1: plt.plot(t[:len(self.taps)], self.taps, label="Impulse Response")
            plt.title("Raised Cosine Filter (Time Domain)")
            plt.xlabel("Time [symbol periods]")
            plt.ylabel("Amplitude")
            plt.grid(True)
            plt.legend()

        if freq_domain:
            H = np.fft.fftshift(np.fft.fft(self.taps, 1024))
            f = np.linspace(-0.5, 0.5, len(H), endpoint=False)
            plt.subplot(2,1,2)
            if plot_type == 0:   plt.stem(f, 20 * np.log10(np.abs(H) + 1e-6), label="Frequency Response [dB]")
            elif plot_type == 1: plt.plot(f, 20 * np.log10(np.abs(H) + 1e-6), label="Frequency Response [dB]")
            plt.title("Raised Cosine Filter (Frequency Domain)")
            plt.xlabel("Normalized Frequency [×π rad/sample]")
            plt.ylabel("Magnitude [dB]")
            plt.grid(True)
            plt.legend()

        plt.tight_layout()
        plt.show()
        
    def get_coefficients(self):
        return self.taps

"""
filtro = RaisedCosineFilter(alpha=1, span=10, sps=10, rrc=True)

coef = filtro.get_coefficients()
print(coef)

filtro.plot(time_domain=True, freq_domain=True)
"""

# Variables iniciales del filtro
# alpha -> rolloff
# span  -> cantidad de símbolos
# sps   -> muestras por símbolo
# rrc   -> True = Root Raised Cosine

alpha = 1
span = 10
sps = 10
rrc = True
plot_type = 1
saved_filters = []
comm= ""
comment = ""


print("\nComandos disponibles:")
print("alpha=0.5 -> Cambia el factor roll-off del filtro")
print("span=8 -> Cambia la cantidad de símbolos que abarca el filtro")
print("sps=16 -> Cambia las muestras por símbolo")
print("rrc=0  -> Cambia el tipo de filtro (0 = Raised Cosine, 1 = Root Raised Cosine)")
print("plot=0 -> Cambia el tipo de gráfico (0 = Stem, 1 = Plot)")
print("plot   -> Muestra el gráfico del filtro actual")
print("save   -> Guarda el filtro actual con un comentario")
print("comment=Texto -> Agrega un comentario al filtro")
print("reset  -> Elimina todos los filtros guardados")
print("compare -> Compara los filtros guardados en un mismo gráfico")
print("coef   -> Muestra los coeficientes del filtro actual")
print("exit\n")







while 1 :
    data = input("ToSent: ")
    if data == 'exit':
        if ser.isOpen():
            ser.close()
        break
    else:
        ser.write(data.encode())
        out = ''
        while ser.inWaiting() > 0:
            out += ser.read(1).decode()
        #print(">> " + out)

        if "alpha=" in out:
            alpha = float(out.split('=')[1])
            print(f"Nuevo alpha: {alpha}")
        elif "span=" in out:
            span = int(out.split('=')[1])
            print(f"Nuevo span: {span}")
        elif "sps=" in out:
            sps = int(out.split('=')[1])
            print(f"Nuevo sps: {sps}")
        elif "rrc=" in out:
            rrc = bool(int(out.split('=')[1]))
            print(f"Nuevo rrc: {rrc}")
        elif "plot=" in out:
            plot_type = int(out.split('=')[1])
            print(f"Nuevo plot_type: {plot_type}")
        elif "comment=" in out:
            comment = out.split("=")[1]
            print(f"Nuevo comentario: {comment}")
        
        
        filtro= RaisedCosineFilter(alpha=alpha, span=span, sps=sps, rrc=rrc)

    
        if out == "plot":
            filtro.plot(time_domain=True, freq_domain=True, plot_type=plot_type)
        
        if out == "save":
            saved_filters.append((filtro, comment))
            comment = ""
            print(f"Filtro guardado: Total guardados: {len(saved_filters)}")

        if out == "compare":
            if len(saved_filters) < 2:
                print("Se necesitan al menos 2 filtros guardados para comparar.")
            else:
                plt.figure(figsize=(10, 8))

                plt.subplot(2,1,1)
                for idx, (f,comm) in enumerate(saved_filters):
                    t = np.arange(-len(f.taps)//2, len(f.taps)//2 + 1) / f.sps
                    if plot_type == 0:   plt.stem(t[:len(f.taps)], f.taps, label=f"Filtro {idx+1} -{comm}")
                    elif plot_type == 1: plt.plot(t[:len(f.taps)], f.taps, label=f"Filtro {idx+1} -{comm}")
                plt.title("Comparacion Temporal de Filtros")
                plt.xlabel("Tiempo [símbolos]")
                plt.ylabel("Amplitud")
                plt.grid(True)
                plt.legend()
                

                plt.subplot(2,1,2)
                for idx, (f,comm) in enumerate(saved_filters):
                    H = np.fft.fftshift(np.fft.fft(f.taps, 1024))
                    f_axis = np.linspace(-0.5, 0.5, len(H), endpoint=False)
                    if plot_type == 0:   plt.stem(f_axis, 20 * np.log10(np.abs(H) + 1e-6), label=f"Filtro {idx+1} -{comm}")
                    elif plot_type == 1: plt.plot(f_axis, 20 * np.log10(np.abs(H) + 1e-6), label=f"Filtro {idx+1} -{comm}")
                plt.title("Comparacion en Frecuencia de Filtros")
                plt.xlabel("Frecuencia Normalizada [×π rad/sample]")
                plt.ylabel("Magnitud [dB]")
                plt.grid(True)
                plt.legend()
                plt.figtext(0.05, 0.01, f"Comentario: {comment}", ha="left", fontsize=10, color="gray")

                plt.tight_layout()
                plt.show()

        if out == "coef":
            print(filtro.get_coefficients())
        
        if out == "reset":
            saved_filters.clear()
            print("Filtros guardados eliminados.")

        
