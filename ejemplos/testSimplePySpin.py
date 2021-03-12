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