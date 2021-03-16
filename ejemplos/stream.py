from simple_pyspin import Camera
import cv2


with Camera() as cam: # Initialize Camera
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