# Deteksi pergerakan dengan kontur pada gambar
# Kontur dibuat dengan cara membandingkan 2 gambar yaitu gambar sebelum dan gambar sekarang

import cv2

# Inisialisasi pengambilan data gambar video secara real time
cap = cv2.VideoCapture('D:/boku no projecto/python/image/cctv/videoplayback (3).mp4')

# pengambilan 2 frame awal untuk dibandingkan
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Looping forever untuk pengambilan real time gambar (video)
while cap.isOpened():
    # perhitungan perbedaan antara 2 gambar
    diff = cv2.absdiff(frame1, frame2)

    # pengubahan gambar diff menjadi grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # proses pengebluran gambar gray
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # proses penghitungan kontur
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations = 3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    # ketika kumpulan kontur sudah didapatkan, dikumpulkan, lalu yang terkumpul dengan ketetangaan terdekat akan disatukan dan dijadikan area kotak
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1200:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1, "Status: ()".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    # visualisasi kontur
    cv2.imshow("feed", frame1)

    # frame lama di replace dengan yang baru
    frame1 = frame2
    ret, frame2 = cap.read()

    # untuk memberhentikan loop view imshow
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
