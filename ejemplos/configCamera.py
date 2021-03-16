from simple_pyspin import Camera
import cv2


with Camera() as cam: # Initialize Camera
    # Set the area of interest (AOI) to the middle half
    cam.Width = cam.SensorWidth // 2
    cam.Height = cam.SensorHeight // 2
    cam.OffsetX = 0
    cam.OffsetY = 0

    # Obtener las imágenes a color 
    cam.PixelFormat = "RGB8"
    
    # Obtener las imágenes en escala de grises
    cam.PixelFormat = "Mono8"

    # To change the frame rate, we need to enable manual control
    #cam.AcquisitionFrameRateAuto = 'Continuous'
    #cam.AcquisitionFrameRateAuto = 'Off'
    #cam.AcquisitionFrameRateEnabled = True
    #cam.AcquisitionFrameRate = 60
    
    # To control the exposure settings, we need to turn off auto
    #cam.GainAuto = 'Continuous'
    #cam.GainAuto = 'Off'
    
    # Set the gain to 20 dB or the maximum of the camera.
    #gain = min(20, cam.get_info('Gain')['max'])
    #print('Gain:', gain)
    #cam.Gain = gain

    #cam.ExposureAuto = 'Continuous'
    #cam.ExposureTime = 10000 # microseconds
    #cam.init()

    cam.start() 

    print("start video")
    while True:
        # capturar frame a frame
        frame = cam.get_array()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow("frame", frame) 
        if cv2.waitKey(1) == ord('q'): #presionamos la tecla Q para cerrar la ventanas
            break

    cam.stop()
    cv2.destroyAllWindows()
    print("stop video")