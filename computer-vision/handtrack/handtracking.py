import cv2
import mediapipe as mp
import time

video = cv2.VideoCapture(0) #captura de video desde camara 0

mpHands = mp.solutions.hands #siempre antes de usar modelo para deteccion de manos
hands = mpHands.Hands() #creo el objeto de la mano
dots = mp.solutions.drawing_utils #dibujar 21 puntos de la mano
'''mp.Hands.Hands() parametros por default: 
    static_image_mode = False: Si esta en falso algunas veces detecta y otras rastrea segun el nivel de confianza
                               Si esta en verdadero siempre hara la parte de deteccion lo que lo hace lento.
                               Cada vez que la confianza de rastreo baja, hara la deteccion de nuevo.
    max_num_hands = 2: Numero maximo de manos
    min_detection_confidence =0.5: 
    min_tracking_confidence = 0.5: Si baja del 50% hara la deteccion de nuevo
    '''
previusTime = 0
currentTime = 0 

while True:
    success, img = video.read() #leer video y capturar imagen
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convertir la imagen a imagen RGB ya que el objeto mano solo usa imagenes RGB
    result = hands.process(imgRGB) #procesamiento de frame (imagen) de video 
    #print (result.multi_hand_landmarks) #saber si una mano ha sido detectada
    if result.multi_hand_landmarks: #si se detectan n manos
        for handLms in result.multi_hand_landmarks: #extraer la informacion de n manos
            for id, lm in enumerate(handLms.landmark): #capturar punto y coordenas x y de 21 puntos de n manos
                #print(id,lm) punto de la mano, coordenadas punto de la mano
                h,w,c = img.shape #alto, ancho y canales de imagen
                px, py = int(lm.x*w), int(lm.y*h) #pixel x,y en donde esta un punto de 21 de la mano
                print(id, px,py) 
                if id == 4: #en pixeles de punto 4 de mano
                    cv2.circle(img, (px,py), 25, (255,0,255), cv2.FILLED) #dibujar un circulo
                        #imagen #coordenadas #tamaño #color   #lleno
            dots.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #dibujamos en la imagen normal por que esta es la que esta siendo mostrada, si hay n manos dibujamos en una mano y luego en las demas
                                              #HAND_CONNECTIONS para dibujar las conexiones entre los puntos de la mano
    currentTime = time.time() #tiempo actual
    fps = 1/(currentTime-previusTime)
    previusTime = currentTime
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2) #poner texto en la imagen
                                   #posicion #fuente de texto       #tamaño #color  #grosor texto  
    cv2.imshow("Image", img) #mostar imagen capturada
    cv2.waitKey(1)


