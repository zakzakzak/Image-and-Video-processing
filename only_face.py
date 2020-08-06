# Deteksi wajah pada video, hanya menampilkan wajah saja tanpa video

import cv2
import numpy as np

# Inisialisasi video
cap = cv2.VideoCapture('D:/boku no projecto/python/image/cctv/videoplayback (5).mp4')

# deteksi wajah dengan haar
face_cascade = cv2.CascadeClassifier('D:/boku no projecto/python/image/cctv/haarcascade_frontalface_default.xml')


counter = 0
counter2 = 0

# loop forever real-time
while cap.isOpened():
    # membaca frame video
    ret, frame = cap.read()


    counter = counter+1
    # setiap 2 frame baru di hitung untuk alasan kecepatan
    if counter%2==0:
        print(counter)

        # convert ke grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # pengumpulan wajah yg didapatkan dari sebuah frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 10)

        # Inisialisasi array arr_face (perbedaan dengan array atas adalah array ini berisi gambar, sedangkan yg atas berupa posisi)
        arr_faces = []

        for (x, y, w, h) in faces:
            # cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
            # penentuan besar area kotak sekitar wajah yang akan digunakan (kotak asli diperbesar sebanyak setengah dari lebar asli)
            tambahan1 = int(w*0.5)
            a = x-tambahan1
            b = y-tambahan1
            c = w+(tambahan1*2)
            d = h+(tambahan1*2)

            e = b+d
            f = a+c


            # karena hanya akan menggunakan gambar berupa kotak, maka, gambar yang berada di ujung (terpotong) akan diabaikan
            if a > 0 and b > 0 and f < 1280 and e < 720:
                crop_img = frame[b:e, a:f]

                # resize gambar sesuai size yg diinginkan (200)
                scale_percent = 200/c*100
                width = int(crop_img.shape[1] * scale_percent / 100)
                height = int(crop_img.shape[0] * scale_percent / 100)
                dim = (width, height)
                # resize image
                crop_img = cv2.resize(crop_img, dim, interpolation = cv2.INTER_AREA)

                # penambahan gambar ke arr_face
                arr_faces.append(crop_img[:199, :])

        # simpan frame----------------------------------------
        # cv2.imwrite('D:/boku no projecto/python/image/cctv/frame_vid/'+str(counter)+'.jpg', frame)
        # simpan frame----------------------------------------


        # --view------------------------
        if "crop_img" in locals() and len(arr_faces) > 0:
            # menyatukan semua gambar wajah, lalu di bentangkan
            vis = np.concatenate(arr_faces, axis=1)
            # simpan frame----------------------------------------
            cv2.imwrite('D:/boku no projecto/python/image/cctv/frame_vid/'+str(counter2)+'.jpg', vis)
            # simpan frame----------------------------------------
            counter2 = counter2+1
            # cv2.imshow("feed", vis)
        if cv2.waitKey(40) == 27:
            break
        # --view------------------------

cv2.destroyAllWindows()
cap.release()
