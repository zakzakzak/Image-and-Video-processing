# Deteksi wajah pada video secara real time, namun area yg tidak terdeteksi wajah
# akan menjadi hitam, sehingga hanya menampilkan wajah saja

import cv2
import numpy as np

cap = cv2.VideoCapture('D:/boku no projecto/python/image/cctv/videoplayback (5).mp4')
face_cascade = cv2.CascadeClassifier('D:/boku no projecto/python/image/cctv/haarcascade_frontalface_default.xml')


counter = 0
while cap.isOpened():
    ret, frame = cap.read()
    bg_hitam = np.zeros((720, 1280,3), dtype=np.uint8)

    counter = counter+1

    if counter%5==0 and counter > 10000:
        print(counter)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 10)
        if (len(faces) > 0):
            for (x, y, w, h) in faces:
                # cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
                a = x-50
                b = y-50
                c = w+100
                d = h+100
                cv2.rectangle(frame, (a,b), (a+c, b+d), (255, 0, 0), 2)
                print(a,b,a+c,b+d)
                # bg_hitam[a:c, b:d] = frame
                print(frame.shape)
                bg_hitam[b:b+d, a:a+c] = frame[b:b+d, a:a+c]

            # simpan frame----------------------------------------
            # cv2.imwrite('D:/boku no projecto/python/image/cctv/frame_vid/'+str(counter)+'.jpg', frame)
            # simpan frame----------------------------------------

            # scale_percent = 200 # percent of original size
            # width = int(frame.shape[1] * scale_percent / 100)
            # height = int(frame.shape[0] * scale_percent / 100)
            # dim = (width, height)
            # # resize image
            # frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

            # --view------------------------
            cv2.imshow("feed", bg_hitam)
            if cv2.waitKey(40) == 27:
                break
            # --view------------------------

cv2.destroyAllWindows()
cap.release()
