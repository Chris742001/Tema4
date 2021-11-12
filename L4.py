import numpy as np
from scipy import stats
import matplotlib.pyplot as plt #Para plot
#Unico cambio fue X(t)----> W(T)
# Variables aleatorias X y Y
va_X = stats.norm(0, np.sqrt(8))
va_Y = stats.norm(0, np.sqrt(8))

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 100
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t)
for i in range(N):
	X = va_X.rvs()
	Y = va_Y.rvs()
	x_t = X * np.cos(np.pi*t) + Y * np.sin(np.pi*t)
	X_t[i,:] = x_t
	plt.plot(t, x_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6, label='Promedio de las  100 realizaciones')

# Graficar el resultado teórico del valor esperado
E = 0*t
plt.plot(t, E, '-.', lw=4, label='Resultado teórico del valor esperado')

# Mostrar las realizaciones del promedio calculado y teórico.
plt.title('Figura 1. Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.legend() # Se imprime las leyendas de la gráfica.
plt.show()   # Muestra la gráfica.

# T valores de desplazamiento tau. 
desplazamiento = np.arange(T) 
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones.
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación.
plt.figure()

# Cálculo de autocorrelación para cada valor de tau.
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(X_t[n,:], np.roll(X_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de autocorrelación.
Rww = 8 * np.cos(np.pi*taus)

# Gr\'aficas de autocorrelación para cada realización del proceso.
plt.plot(taus, Rww, '-.', lw=4, label='Autocorrelación teórica')
plt.title('Figura 2. Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend() # Se imprime la leyenda de la gráfica.
plt.show()   # Muestra la gráfica.

# Gráficas de la autocorrelación en el tiempo.  
plt.plot(t, corr[n,:], lw=6, color = 'blue', label='Autocorrelación experimental del proceso aleatorio X(t)')
plt.plot(t, Rww, '-.', lw=4, color='lime', label='Autocorrelación teórica del proceso aleatorio X(t)')
plt.title('Funciones de autocorrelación a través del tiempo')
plt.xlabel(r'$t$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend() # Se imprime la leyenda de la gráfica.
plt.show()   # Muestra la gráfica