# lab-3
## Descripción


## Desarrollo
### Adquicisión de los datos
Después de tener grabados los audios que se encuentran en el presente repositorio, hicimos uso de una librería especial “scipy.io.wavfile” la cuál nos permite traer los audios de tipo “wav” y usar toda la información de ellos. 
Primeramente para traerlos al entorno de programación de “Spyder” usamos la función “waves.read()” la cuál tiene como parámetro el nombre del archivo que se desea leer y los da los datos y el muestreo. A continuación se muestra la línea del código respectiva. 

    archivo1 = 'Juanealta.wav';
    muestreo1, sonido1 = waves.read(archivo1)
    
    archivo2 = 'ruide.wav';
    muestreo2, sonido2 = waves.read(archivo2)
    
    archivo3 = 'sofiaYA.wav';
    muestreo3, sonido3 = waves.read(archivo3)
Para poder trabajar con los audios obtenidos y grabados en el laboratorio de diseño y simulación dentro de la universidad militar nueva granada, ya que es una sala completamente insonorizada que asegura que el ruido existente en los audios sean lo menores posible, es necesario hacerle unos ajustes especiales a los audios como asegurarse que tengan la misma duración, misma cantidad de muestras tomadas entre otras cosas. Una vez realizados los respectivos ajustes, se grafican estos datos por medio de las siguientes líneas de código.

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

![alt](AudiosNormales.png)

### SNR
La relación entre el ruido y la señal normal es calculada por medio del siguiente código y es importante en el laboratorio ya que si el resultado nos muestra mucho más ruido que la señal, se va a dificultar bastante esa filtración de una de las voces que se escuchen. 

        potJuane = np.sum(sonido1**2) / len(sonido1)
        potSofia = np.sum(sonido3**2) / len(sonido3)
        potRuido = np.sum(sonido2**2) / len(sonido2)
        SNR1 = 10*np.log10(potJuane/potRuido)
        SNR2 = 10*np.log10(potSofia/potRuido)
        
        print(f"Potencia de audio Juane: {potJuane:.4f}")
        print(f"Potencia de audio sofiaYA: {potSofia:.4f}")
        print(f"Potencia de ruido: {potRuido:.4f}")
        
        print(f"SNR de audio juane: {SNR1:.4f}")
        print(f"SNR de audio sofiaYA: {SNR2:.4f}")
        
        #Resultados en el terminal Python
        Potencia de audio Juane: 470273.9062
        Potencia de audio sofiaYA: 140361.2344
        Potencia de ruido: 6809.4594
        SNR de audio juane: 18.3924
        SNR de audio sofiaYA: 13.1413


### Transformada de Fourier

### ICA

### Beamforming


## REQUERIMIENTOS
- Python 3.11
- Spyder 6.0
- Librerias como: wfdb, matplotlib, numpy, scipy.io.wavfile, sklearn.decomposition, sounddevice
## REFERENCIAS
[1] 

[2] 

[3]  
## AUTORES
- Juan Diego Clavijo Fuentes
  est.juan.dclavijjo@unimilitar.edu.co
- Sofia Olivella Moreno
  est.sofia.olivella@unimilitar.edu.co
