# -*- coding: utf-8 -*-
"""
@author: julian
"""
# Importar librerias
import numpy as np                  # Biblioteca para crear vectores y matrices grandes multidimensionales
import matplotlib.pyplot as plt     # BIblioteca para crear graficos

# Creamos la clase del modelo de la red neuronal
class NeuralNetwork:
    # Rutina: Inicio
    def __init__(self, layers, activation='tanh'):
        # Si la funcion de activacion es sigmoid
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_prime = sigmoid_derivada
        # Si la funcion de activacion es tanh
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_prime = tanh_derivada

        # Inicializar los pesos
        self.weights = []
        self.deltas = []
        # Capas = [2,3,4]
        # asigno valores aleatorios (-1,1) a capa de entrada y capa oculta
        for i in range(1, len(layers) - 1):
            r = 2*np.random.random((layers[i-1] + 1, layers[i] + 1)) -1
            self.weights.append(r)
        # Asigno aleatorios (-1,1) a capa de salida
        r = 2*np.random.random( (layers[i] + 1, layers[i+1])) - 1
        self.weights.append(r)

    # Rutina: Entrenar modelo
    def fit(self, X, y, learning_rate=0.2, epochs=100000):
        # Agrego columna de unos a las entradas X
        # Con esto agregamos la unidad de Bias a la capa de entrada
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)
        
        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]

            for l in range(len(self.weights)):
                    dot_value = np.dot(a[l], self.weights[l])
                    activation = self.activation(dot_value)
                    a.append(activation)
            # Calculo la diferencia en la capa de salida y el valor obtenido
            error = y[i] - a[-1]
            deltas = [error * self.activation_prime(a[-1])]
            
            # Empezamos en el segundo layer hasta el ultimo
            # (Una capa anterior a la de salida)
            for l in range(len(a) - 2, 0, -1): 
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_prime(a[l]))
            self.deltas.append(deltas)

            # Invertir: [level3(output)->level2(hidden)]  => [level2(hidden)->level3(output)]
            deltas.reverse()

            # Backpropagation
            # 1. Multiplcar los delta de salida con las activaciones de entrada para obtener el gradiente del peso.
            # 2. Actualizo el peso restandole un porcentaje del gradiente
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

            if k % 10000 == 0: print('epochs:', k)

    # Rutina: Prediccion
    def predict(self, x): 
        ones = np.atleast_2d(np.ones(x.shape[0]))
        a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a

    # Rutina: Imrpimir pesos
    def print_weights(self):
        print("Listado pesos de conexiones:")
        for i in range(len(self.weights)):
            print(self.weights[i])

    # Rutina: Obtener pesos
    def get_weights(self):
        return self.weights
    
    # Rutina: Obtener deltas
    def get_deltas(self):
        return self.deltas

# Funciones de activacion: Al crear la red, podremos elegir entre usar la funcion sigmoid o tanh
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))
def sigmoid_derivada(x):
    return sigmoid(x)*(1.0-sigmoid(x))
def tanh(x):
    return np.tanh(x)
def tanh_derivada(x):
    return 1.0 - x**2

# Red para controlar Temperatura y Humedad con Ventilador, Resistencia y Electrovalvula 
# Capa de entrada: 2 neuronas
# Capa de oculta:  3 neuronas
# Capa de salida:  3 neuronas 
# Funcion de activacion: tanh
nn = NeuralNetwork([2,3,3],activation ='tanh')

# Las entradas corresponden a: [Temperatura, Humedad]
X = np.array([
              [-1, -1], [-1, 0], [-1, 1],  # 1,2,3
              [0,  -1], [0,  0], [0,  1],  # 4,5,6
              [1,  -1], [1,  0], [1,  1],  # 7,8,9
             ])

# Las salidas corresponden a: [Ventilador, Resistencia, Electrovalvula]
y = np.array([[0,1,1],    # 1
              [0,1,-1],   # 2
              [0,1,0],    # 3
              [-1,-1,1],  # 4 
              [-1,-1,-1], # 5
              [-1,-1,0],  # 6
              [1,0,1],    # 7
              [1,0,-1],   # 8
              [1,0,0],    # 9
             ])

# Entrenar modelo con las entradas y salidas
nn.fit(X, y, learning_rate=0.03,epochs=50501)

# Prediccion de prueba 
index=0
for e in X:
    prediccion = nn.predict(e)
    print("X:",e,"esperado:",y[index],"obtenido:",  (int)(round(prediccion[0])), (int)(round(prediccion[1])), (int)(round(prediccion[2])))
    #print("X:",e,"y:",y[index],"Network:",prediccion)
    index=index+1

# Rutina para convertir valor a String
def to_str(name, W):
    s = str(W.tolist()).replace('[', '{').replace(']', '}')
    return 'float '+name+'['+str(W.shape[0])+']['+str(W.shape[1])+'] = ' + s + ';'

# Obtenermos los pesos entrenados para poder usarlos en el codigo de arduino
pesos = nn.get_weights()
print('\n')
print('Pesos de capa oculta y capa de salida:')
print(to_str('pesos_capa_oculta', pesos[0]))
print(to_str('pesos_capa_salida', pesos[1]))

# Graficas datos de entrenamiento
deltas = nn.get_deltas()
valores=[]
index=0
for arreglo in deltas:
    valores.append(arreglo[1][0] + arreglo[1][1])
    index=index+1

plt.plot(range(len(valores)), valores, color='b')
plt.ylim([0, 0.4])
plt.ylabel('Coste')
plt.xlabel('Epocas')
plt.tight_layout()
plt.show()