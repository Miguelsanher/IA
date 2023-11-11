# MODELO DE IA 

Esta es una IA de regresión que de una serie de Celsius y Fahrenheit es capaz de adivinar todos los demás valores.

Ha sido desarrollada en Google Colab. El archivo .h5 es el modelo entrenado listo para ser exportado a cualquier otro PC para entrenarlo más o hacer pruebas con él. Es recomendable hacer pruebas desde el cmd.

# REQUISITOS

-Tener python 3.11 es recomendable y vital tener una versión soportada por tensorflow.

-Python 3.12 no soporta tensorflow por tanto no funcionará.

# EXPORTAR MODELO

Descarga el modelo'DeCaFEntrenado.h5'

Primero crea un código con la sala de pruebas incluida en el modelo o crea la tuya propia.

Luego mete la sala de pruebas en el mismo sitio que tengas el modelo .h5.

Ejecuta desde el cmd:

```cmd
C:\Users\Usuario\Carpeta_con_modelo_y_sala_de_pruebas>python nombre.py

```

Si quieres entrenarlo solo descárgalo, entrénalo y ejecútalo para ver resultados.

# INFORMACION DEL MODELO ENTRENADO

El modelo entrenado cuenta con un loss en el test de 0.04033243656158447.

Depende del entrenamiento y la modificación el el batch_size y las épocas se obtendrán resultados diferentes.
