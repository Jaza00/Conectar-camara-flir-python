import cv2
import EasyPySpin

cap = EasyPySpin.VideoCapture(0) # adquirir camara
ret, frame = cap.read() # capturar frame
cv2.imshow("frame", frame) # visualizar frame
cv2.waitKey(0) # presionar tecla Q para cerrar ventana
cap.release() # desconectar camara
cv2.destroyAllWindows() 