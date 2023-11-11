import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

listaC=[0,5,8,6.3,120,78,2,5.5,71,2.3,45,84,34,450,266,61,1,59,850]
listaF=[32,41,46.4,145.4,248,172.4,35.6,131,159.8,73.4,113,183.2,93.2,842,510.8,141.8,33.8,138.2,1562]
listaCt=[9,49,120,50,122]
listaFt=[48.2,120.2,248,122,251.6]
datos_1=np.array(listaC,dtype=float)
datos_2=np.array(listaF,dtype=float)
#CONSTRUIMOS EL MODELO
def crear_modelo():
  model=tf.keras.models.Sequential()
  model.add(tf.keras.layers.Input(shape=(1,))) #PARA VECTORES UNIDIMENSIONALES SIEMPRE (n,)
  model.add(tf.keras.layers.Dense(16,activation='relu'))

  model.add(tf.keras.layers.Dense(32,activation='relu'))

  model.add(tf.keras.layers.Dense(64,activation='relu'))

  model.add(tf.keras.layers.Dense(128,activation='relu'))

  model.add(tf.keras.layers.Dense(256,activation='relu'))

  model.add(tf.keras.layers.Dense(units=1,activation='linear'))
  return model
#LLAMAMOS AL MODELO
modeloEntrenar = crear_modelo()
#COMPILAMOS
optimizer = tf.keras.optimizers.Adam(learning_rate=0.008)
modeloEntrenar.compile(optimizer= optimizer, loss='mean_squared_error')
#ENTRENAMOS
print("Comenzando a entrenar......")
historial= modeloEntrenar.fit(listaC,listaF,epochs=1000,verbose=True,batch_size=32)
print("Modelo entrenado")

#CREAMOS UN GRÁFICO PARA VER EL LOSS
plt.xlabel("EPOCA")
plt.ylabel("Magnitud perdida")
plt.plot(historial.history["loss"])
#PREDICCIÓN DE PRUEBA
resultado = modeloEntrenar.predict([100.0])
print("Son"+str(resultado)+"farenhait ")

#HACEMOS UN TEST
test_loss = modeloEntrenar.evaluate(listaCt, listaFt)
print(f"Test loss is: {test_loss}")

#PREDECIR VALORES (SALA DE PRUEBAS)
flag=1
while(flag==1):
  dato=float(input("Introduce dato en celsius "))
  resultado = modeloEntrenar.predict([dato])
  print("El resultado en fahrenheit es "+str(resultado))
  respuesta1= str(input("Quieres predecir otro? (s/n)"))
  if(respuesta1=='N' or respuesta1=='n'):
    flag=0
