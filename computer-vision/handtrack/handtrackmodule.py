'''Este es un modulo para crear una funcion para el rastreo de manos; poder
pedir al modulo que rastree un punto en particular de la mano, o que el modulo
nos de los pixeles en los que se encuentran los 21 puntos de la mano'''


import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode = False, maxHands=2, detectionCon = 0.5, trackCon = 0.5): #constructor
        self.mode = mode 
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands #siempre antes de usar modelo para deteccion de manos
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, 
                                        self.detectionCon, self.trackCon) #creo el objeto de la mano
        self.dots = mp.solutions.drawing_utils #dibujar 21 puntos de la mano


    def find_hands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convertir la imagen a imagen RGB ya que el objeto mano solo usa imagenes RGB
        self.result = self.hands.process(imgRGB) #procesamiento de frame (imagen) de video 
        #print (result.multi_hand_landmarks) #saber si una mano ha sido detectada
        if self.result.multi_hand_landmarks: #si se detectan n manos
            for handLms in self.result.multi_hand_landmarks: #extraer la informacion de n manos
                if draw:
                    self.dots.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS) #dibujamos en la imagen normal por que esta es la que esta siendo mostrada, si hay n manos dibujamos en una mano y luego en las demas
                                              #HAND_CONNECTIONS para dibujar las conexiones entre los puntos de la mano
        return img


    def findPosition(self, img, pointNo = [0], handNumber= 0,draw = True):
        lmList = [] #lista de pixeles donde esta punto de la mano solicitado
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNumber] #capturar los datos de solo una mano
            for id, lm in enumerate(myHand.landmark): #capturar punto y coordenas x y de 21 puntos de n manos
                #print(id,lm) punto de la mano, coordenadas punto de la mano
                h,w,c = img.shape #alto, ancho y canales de imagen
                px, py = int(lm.x*w), int(lm.y*h) #pixel x,y en donde esta un punto de 21 de la mano
                #print(id, px,py)
                lmList.append([id,px,py])
                if draw and id in pointNo: #en pixeles de punto 4 de mano
                    cv2.circle(img, (px,py), 9, (255,0,0), cv2.FILLED) #dibujar un circulo
                          #imagen #coordenadas #tamaño #color   #lleno
        return lmList

def run():
    previusTime = 0
    currentTime = 0
    video = cv2.VideoCapture(0) #captura de video desde camara 0
    detector = handDetector()
    while True:
        success, img = video.read() #leer video y capturar imagen
        img = detector.find_hands(img)
        lmList = detector.findPosition(img, pointNo=[4,8])
        if len(lmList) != 0:
            print (lmList[4]) #pixeles en donde esta el punto 4 de mano
        currentTime = time.time() #tiempo actual
        fps = 1/(currentTime-previusTime)
        previusTime = currentTime
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2) #poner texto en la imagen
                                        #posicion #fuente de texto      #tamaño #color  #grosor texto  
        cv2.imshow("Image", img) #mostar imagen capturada
        cv2.waitKey(1)


if __name__ == '__main__':
    run() 