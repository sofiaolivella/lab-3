# import wfdb
import matplotlib.pyplot as plt
import numpy as np
# from scipy.stats import gaussian_kde
import scipy.io.wavfile as waves
from sklearn.decomposition import FastICA
import sounddevice as sd


archivo1 = 'Juanealta.wav';
muestreo1, sonido1 = waves.read(archivo1)

archivo2 = 'ruide.wav';
muestreo2, sonido2 = waves.read(archivo2)

archivo3 = 'sofiaYA.wav';
muestreo3, sonido3 = waves.read(archivo3)

potJuane = np.sum(sonido1**2) / len(sonido1)
potSofia = np.sum(sonido3**2) / len(sonido3)
potRuido = np.sum(sonido2**2) / len(sonido2)

if len(sonido1.shape) > 1:
    sonido1 = sonido1[:, 0]
if len(sonido2.shape) > 1:
    sonido2 = sonido2[:, 0]
if len(sonido3.shape) > 1:
    sonido3 = sonido3[:, 0]

# Asegurar que las señales tengan la misma longitud
min_len = min(len(sonido1), len(sonido3))
sonido1 = sonido1[:min_len]
sonido3 = sonido3[:min_len]


SNR1 = 10*np.log10(potJuane/potRuido)
SNR2 = 10*np.log10(potSofia/potRuido)

print(f"Potencia de audio Juane: {potJuane:.4f}")
print(f"Potencia de audio sofiaYA: {potSofia:.4f}")
print(f"Potencia de ruido: {potRuido:.4f}")

print(f"SNR de audio juane: {SNR1:.4f}")
print(f"SNR de audio sofiaYA: {SNR2:.4f}")

# Graficar señales
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.semilogy(np.abs(sonido1), color='red')
plt.title(f"{archivo1} (Semilogarítmica)")
plt.xlabel("Tiempo [muestras]")
plt.ylabel("Amplitud")

plt.subplot(3, 1, 2)
plt.semilogy(np.abs(sonido2), color='green')
plt.title(f"{archivo2} (Semilogarítmica)")
plt.xlabel("Tiempo [muestras]")
plt.ylabel("Amplitud")

plt.subplot(3, 1, 3)
plt.semilogy(np.abs(sonido3), color='blue')
plt.title(f"{archivo3} (Semilogarítmica)")
plt.xlabel("Tiempo [muestras]")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()

#Transformada de Fourier
N1 = len(sonido1)
frecuencia1 = np.fft.fftfreq(N1, 1/muestreo1)
fft1 = np.fft.fft(sonido1)
magnitud1 = np.abs(fft1)

N2 = len(sonido2)
frecuencia2 = np.fft.fftfreq(N2, 1/muestreo2)
fft2 = np.fft.fft(sonido2)
magnitud2 = np.abs(fft2)

N3 = len(sonido3)
frecuencia3 = np.fft.fftfreq(N3, 1/muestreo3)
fft3 = np.fft.fft(sonido3)
magnitud3 = np.abs(fft3)

plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(frecuencia1, magnitud1, color='purple')
plt.title(f"{archivo1} (Frecuencia)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")

plt.subplot(3, 1, 2)
plt.plot(frecuencia2, magnitud2, color='orange')
plt.title(f"{archivo2} (Frecuencia)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")

plt.subplot(3, 1, 3)
plt.plot(frecuencia3, magnitud3, color='brown')
plt.title(f"{archivo3} (Frecuencia)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")

plt.tight_layout()
plt.show()

# Aplicar ICA
mezcla = np.vstack([sonido1, sonido3]).T

ica = FastICA(n_components=2)
senales_separadas = ica.fit_transform(mezcla)

# Graficar señales separadas por ICA
plt.figure(figsize=(15, 7))
for i in range(2):
    plt.subplot(2, 1, i+1)
    plt.plot(senales_separadas[:, i], label=f"Señal {i+1}", color=f"C{i}")
    plt.title(f"Señal Separada {i+1} por ICA")
    plt.xlabel("Tiempo [muestras]")
    plt.ylabel("Amplitud")
    plt.legend()

plt.tight_layout()
plt.show()


#Beamforming con un retardo de ejemplo (10 muestras)
d = 2.5  # Distancia en metros
v = 343  # Velocidad del sonido en m/s
fs = muestreo1  # Frecuencia de muestreo

delay_samples = int((d * fs) / v)
print(f"Retardo calculado: {delay_samples} muestras")

sonido3_delayed = np.roll(sonido3, delay_samples)
beamforming_resultado = (sonido1 + sonido3_delayed) / 2


plt.subplot(3, 1, 3)
plt.plot(beamforming_resultado, label="Señal Filtrada por Beamforming", color="C2")
plt.title("Resultado de Beamforming por Delay-and-Sum")
plt.xlabel("Tiempo [muestras]")
plt.ylabel("Amplitud")
plt.legend()

plt.tight_layout()
plt.show()


# Voces por ICA
for i in range(2):
    print(f"Reproduciendo señal separada {i+1} por ICA...")
    sd.play(senales_separadas[:, i], muestreo1)
    sd.wait()
    
# Voces por Beamforming
print("Reproduciendo señal filtrada por Beamforming...")
sd.play(beamforming_resultado, muestreo1)
sd.wait()