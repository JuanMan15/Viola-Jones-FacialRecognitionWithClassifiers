import cv2
import os

# Cargar clasificadores
ruta_base = os.path.join(os.path.dirname(__file__), "..", "classifiers")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
nose_cascade = cv2.CascadeClassifier(os.path.join(ruta_base, "haarcascade_mcs_nose.xml"))
mouth_cascade = cv2.CascadeClassifier(os.path.join(ruta_base, "haarcascade_mcs_mouth.xml"))

# Historial de detecciones
ultima_deteccion = {
    "rostro": None,
    "ojos": [],
    "nariz": [],
    "boca": []
}

def detectar_partes_faciales(frame):
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gris = cv2.equalizeHist(gris)

    rostros = face_cascade.detectMultiScale(gris, 1.1, 5, minSize=(100, 100))

    if len(rostros) > 0:
        ultima_deteccion["rostro"] = rostros[0]
    elif ultima_deteccion["rostro"] is None:
        return frame

    x, y, w, h = ultima_deteccion["rostro"]
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    roi_gris = gris[y:y + h, x:x + w]
    roi_color = frame[y:y + h, x:x + w]

    # OJOS
    ojos = eye_cascade.detectMultiScale(roi_gris[0:h//2], 1.1, 10, minSize=(20, 20))
    if len(ojos) >= 2:
        ultima_deteccion["ojos"] = ojos
    for (ex, ey, ew, eh) in ultima_deteccion["ojos"]:
        cv2.circle(roi_color, (ex + ew//2, ey + eh//2), ew//2, (0, 255, 0), 2)

    # NARIZ
    nariz_roi = roi_gris[h//4:3*h//4]
    nariz = nose_cascade.detectMultiScale(nariz_roi, 1.1, 5, minSize=(30, 30))
    if len(nariz) > 0:
        ultima_deteccion["nariz"] = nariz
    for (nx, ny, nw, nh) in ultima_deteccion["nariz"]:
        ny += h // 4
        cv2.circle(roi_color, (nx + nw//2, ny + nh//2), nw//3, (0, 255, 255), 2)

    # BOCA
    boca_roi = roi_gris[h//2:]
    boca = mouth_cascade.detectMultiScale(boca_roi, 1.3, 15, minSize=(30, 30))
    if len(boca) > 0:
        ultima_deteccion["boca"] = boca
    for (mx, my, mw, mh) in ultima_deteccion["boca"]:
        my += h // 2
        cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (255, 0, 255), 2)

    return frame
