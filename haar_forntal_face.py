# Deteksi wajah menggunakan haar cascade

import cv2

# pengambilan video dari folder
cap = cv2.VideoCapture('D:/boku no projecto/python/image/cctv/videoplayback (5).mp4')

# pemilihan xml cascade
face_cascade = cv2.CascadeClassifier('D:/boku no projecto/python/image/cctv/haarcascade_frontalface_default.xml')



# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.1, 1)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
# cv2.imshow("feed", img)
# cv2.waitKey()


counter = 0
# loop forever gambar dari video
while cap.isOpened():
    # read frame setiap video
    ret, frame = cap.read()

    # counter untuk perhitungan frame
    counter = counter+1
    # perhitungan dilakukan setiap 5 frame untuk alasan kecepatan komputasi
    if counter%5==0:
        print(counter)

        # mengubah gambar video (frame) jadi gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # deteksi wajah pada gambar, lalu dikumpulkan ke dalam array faces
        # atribut pertama (1.1) untuk seberapa kejelasan wajah
        # atribut kedua (10) untuk minimum ketetangaan
        faces = face_cascade.detectMultiScale(gray, 1.1, 10)

        # setiap faces yg didapat, diambil x,y (posisi) dan w,h (lebar, tinggi)
        for (x, y, w, h) in faces:
            # cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
            # melakukan tambahan dengan angka untuk menambah besar kotak pada wajah
            a = x-50
            b = y-50
            c = w+100
            d = h+100
            cv2.rectangle(frame, (a,b), (a+c, b+d), (255, 0, 0), 2)

        # simpan frame----------------------------------------
        # cv2.imwrite('D:/boku no projecto/python/image/cctv/frame_vid/'+str(counter)+'.jpg', frame)
        # simpan frame----------------------------------------


        # Resize gambar--------------------------------------------
        # scale_percent = 200 # percent of original size
        # width = int(frame.shape[1] * scale_percent / 100)
        # height = int(frame.shape[0] * scale_percent / 100)
        # dim = (width, height)
        # # resize image
        # frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        # Resize gambar--------------------------------------------

        # --view------------------------
        cv2.imshow("feed", frame)
        if cv2.waitKey(40) == 27:
            break
        # --view------------------------

cv2.destroyAllWindows()
cap.release()
