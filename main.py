import cv2
import os
from utils.detector import detectar_partes_faciales

def iniciar_camara():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("No se pudo abrir la cámara.")
        return

    print("Presiona ESC para salir...")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("No se pudo capturar el video.")
            break

        frame_con_detecciones = detectar_partes_faciales(frame)
        cv2.imshow("rostro, ojos, nariz y boca Viola-Jones", frame_con_detecciones)

        if cv2.waitKey(1) & 0xFF == 27: 
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    iniciar_camara()
