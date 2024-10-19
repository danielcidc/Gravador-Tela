import numpy as np 
import cv2
from PIL import ImageGrab 

def gravaTela():
    
    # Define o codec de saída para gravar a tela
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768)) # testei para ambos os formatos AVI e MKV 

    # Captura a tela e converte para RGB antes de gravar no vídeo
    while True:
        img = ImageGrab.grab() 
        img_np = np.array(img) 
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB) 
        cv2.imshow("Gravador de Tela", frame) 
        out.write(frame) 

        if cv2.waitKey(1) == 27: #o valor 27 corresponde à tecla Q
            break 

    # Fecha os recursos
    out.release()
    cv2.destroyAllWindows() 

gravaTela() 

