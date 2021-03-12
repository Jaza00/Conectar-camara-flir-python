<div align="center">
    <img src="images\imagenIntecol.PNG"></img>
</div>

<h1 align="center">
    Conectar cámara FLIR con python
</h1>

<h4><b>Realizado por:</b> Ing. Jaimen Aza</h4>

<p>
    En este documento vamos a mostrar como acceder a una cámara FLIR desde python3.8 con ayuda del SDK de spinnaker y la libreria PySpin, adicional a esto también se muestran otras librerias que facilitan el uso de la libreria principal PySpin. Tambien se muestran unos ejemplos básicos del uso de estas librerias. 
    Para empezar con el procedimiento es necesario tener previamente instalado unas dependecias.
<p>

<h2>
    Instalar dependecias
</h2>

<h3> Instalar python3.8 </h3>
<p>
    En windows, ir a Microsft Store, buscar python3.8 e instalar.
</p>

<h3>Instalar el SDK spinnaker</h3>
<p>
    Para esto, instalar el archivo adjunto llamado <b>SpinnakerSDK_FULL_2.3.0.77_x64.exe</b>
</p>

<h3>Instalar librerias de python</h3>
<p>
    Si en el ordenador existe más de una verisión de Python, instalar las librerias con pip3.8
</p>

* Instalar numpy

```
    pip3.8 install numpy
```

* Instalar matplotlib
```
    pip3.8 install matplotlib
```
<p>Matplotlib no es necesario para PySpin, pero es necesario para algunos ejemplos.</p>

* Instalar PySpin
<p>
    La extensión PySpin Python proporciona una interfaz de software común para controlar y adquirir imágenes de cámaras FLIR USB 3.0, GigE y USB 2.0 utilizando la misma API en Windows de 32 o 64 bits.
</p>
<p>
    Para esto, instalar el whl aquí adjunto llamado <b>spinnaker_python-2.3.0.77-cp38-cp38-win_amd64.whl</b> con la siguinte linea de comando:
</p>

```
    python3.8 -m pip install spinnaker_python-2.3.0.77-cp38-cp38-win_amd64.whl
```

**Observacion:**
La versión de la librería spinnaker de python deben corresponder a la versión del SDK de spinnaker, en este ejemplo la versión para los dos archivos es 2.3.0.77.

<h3>Conectar cámara y verificar funcionamiento en el equipo</h3>
<p>
    Para esto presionar menu + R y ejecutar <b>devmgmt.msc</b>, si la cámara es reconocida debe aparecer en los dispositivos, así: 
</p>
<div align="center">
    <img src="images\dispositivosUSB.PNG"></img>
</div>
<p>
    De lo contrario, significa que hay un problema de driver. Para corregir esto, abrir el programa SpinView
</p>
<div align="center">
    <img src="images\errorSpinView.PNG"></img>
</div>
<p>
    click derecho sobre el error y seleccionar <b>Switch driver to resolve</b>
</p>
<div align="center">
    <img src="images\cambiarDriverSpinView.PNG"></img>
</div>
<p>
    seleccionar el driver Microsoft y hacer click en <b>Install Driver</b>.
</p>
<div align="center">
    <img src="images\instalarDriver.PNG"></img>
</div>
<p>
    Finalmente, ver una captura de la cámara para verificar su funcionamiento
</p>
<div align="center">
    <img src="images\capturaImagenSpinView.PNG" width="700"></img>
</div>

<h3>Conectar cámara desde python</h3>
<p>
    Ir a la ruta <b>files\spinnaker\Examples\Python3</b> y ejecutar:
<p>

```
    python3.8 Acquisition.py
```

<h3>Otras librerias que facilitan el uso de PySpin</h3>

* simple-pyspin
<p>
    Para poder usar esta libreria es necesario haber realizado todos los anteriores pasos, ya que simple-pyspin es una libreria que trabaja sobre PySpin y facilita su uso. Para su instalación ejecutar:
<p>

```
    pip install simple-pyspin
```
<p>
    <b>Ejemplo 1:</b>
    En este ejemplo se muestra como capturar y visualizar una imagen usando opencv y simple_pyspin
</p>

```python
from simple_pyspin import Camera
import cv2

cam = Camera() # adquirir camara
cam.init() # inicializar camara
cam.start() # empezar stream
frame = cam.get_array() # obtener imagen
cv2.imshow("frame", frame) #mostrar frame
cv2.waitKey(0) # pulsar la letra Q para cerrar la ventana
cv2.destroyAllWindows()
cam.stop() # detener stream
cam.close() # es recomendable limpiar todo 
```

<p>
    <b>Ejemplo 2:</b> Adquirir video rgb
</p>

```python
from simple_pyspin import Camera
import cv2


with Camera() as cam: # Initialize Camera
    # If this is a color camera, get the image in RGB format.
    if 'Bayer' in cam.PixelFormat:
        cam.PixelFormat = "RGB8"

    cam.init() 
    cam.start() 

    print("start video")
    while True:
        # capturar frame a frame
        frame = cam.get_array()
        cv2.imshow("frame", frame) 
        if cv2.waitKey(1) == ord('q'): #presionamos la tecla Q para cerrar la ventanas
            break

    cam.stop()
    cv2.destroyAllWindows()
    print("stop video")
```

<p>
    Para más información visitar: <a href="https://klecknerlab.github.io/simple_pyspin/">simple_pyspi</a>
</p>

* EasyPySpin
<p>
    EasyPySpin es otra libreria que facilita el uso de PySpin, al igual que simple_pyspin esta libreria trabaja sobre PySpin. Para su instalación ejecutar:
</p>

```
    pip3.8 install git+https://github.com/elerac/EasyPySpin
```

<p>
    <b>Ejemplo:</b>
    En este ejemplo se muestra como capturar y visualizar una imagen usando opencv y EasyPySpin
</p>

```python
import cv2
import EasyPySpin

cap = EasyPySpin.VideoCapture(0) # adquirir camara
ret, frame = cap.read() # capturar frame
cv2.imshow("frame", frame) # visualizar frame
cv2.waitKey(0) # presionar tecla Q para cerrar ventana
cap.release() # desconectar camara
cv2.destroyAllWindows() 
```
<p>
    Para más información visitar: <a href="https://github.com/elerac/EasyPySpin">EasyPySpin</a>
</p>
