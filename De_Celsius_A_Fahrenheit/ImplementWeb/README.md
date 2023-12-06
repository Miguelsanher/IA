# Español
## ¿QUE ES ESTO?
Son los archivos para la exportacion del modelo a una web con html, css y javascript.                  
El archivo .bin y model.json el el modelo DeCaFEntrenado_1.2.h5. Este cambio de formato hará posible la implementacion web gracias a TensorFlowjs.

## DESPLIEGUE
- Descarga toda la carpeta De_Celsius_A_Fahrenheit. Puedes descargar solo la carpeta ImplementWeb si solo deseas la implementacion web.
  El unico cambio sería hacer un cd menos.
- Pon la carpeta descargada en tu escritorio.
- Es hora de crear un server http para que pueda cojer la librería de TensorFlow js lo haremos simple con python
- Abre el cmd y con Python instalado escribe:
  ```cmd
    C:\Users\Usuario\Desktop\De_Celsius_A_Fahrenheit\ImplementWeb>python -m http.server 8000
  ```
  Si has descargado la carpeta De_Celsius_A_Fahrenheit esa será tu ruta si solo descargaste ImplementWeb te ahorras un cd.
- Una vez abierto el server dirígete al puerto en nuestro caso el 8000 (abre google y ve a http://localhost:8000/)
- Una vez quieras cerrar el server solo cierra el cmd.
  Deberías ver algo tal que esto:
  ![](https://github.com/Miguelsanher/IA/blob/main/De_Celsius_A_Fahrenheit/ImplementWeb/capGitHub.PNG)

  ## ACUALIZACIONES
  - He añadido fotos tematicas. Hay una para temperaturas frías(a pesar de que el modelo no predice temperaturas negativas), normales y cálidas.Tambien he puesto una foto de fondo inicial del espacio.

