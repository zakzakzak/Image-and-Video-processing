# Meng-animasikan frame yang ada
# tujuan dari algo ini adalah :
# dikarenakan sangat lambat sekali melakukan perhitungan secara realtime, sehingga untuk melihat hasil video yang sudah dihitung
# juga lambat, jadi penulis mempunyai ide untuk menyimpan gambar hasil perhitungan tersebut setiap frame nya
# lalu me mutar ulang kumpulan gambar tersebut sehingga lebih cepat untuk dilihat
# kekurangan, harus menunggu lama, apalagi jika ada perhitungan yang ingin di ganti

import cv2
import time
import numpy as np


counter = 0
aaaa = np.zeros((300, 2000,3), dtype=np.uint8)
for i in range(272):

    counter = counter+1
    if counter%1==0:
        print(counter)

        img = cv2.imread('D:/boku no projecto/python/image/cctv/frame_vid/'+str(counter)+'.jpg')

        scale_percent = 150 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        # print(img.shape)
        # aaaa[:img.shape[0], :img.shape[1]] = img

        # --view------------------------
        cv2.imshow("feed", img)
        if cv2.waitKey(40) == 27:
            break
        # --view------------------------
        # time.sleep(0.5)



cv2.destroyAllWindows()






# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------COMBINE IMAGE ALGO------------------------------------------
# img1 = cv2.imread('D:/boku no projecto/python/image/cctv/frame_vid/1.jpg')
# img2 = cv2.imread('D:/boku no projecto/python/image/cctv/frame_vid/100.jpg')
#
# scale_percent = 20
# width = int(img1.shape[1] * scale_percent / 100)
# height = int(img1.shape[0] * scale_percent / 100)
# dim = (width, height)
# img1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
#
# scale_percent = 20
# width = int(img2.shape[1] * scale_percent / 100)
# height = int(img2.shape[0] * scale_percent / 100)
# dim = (width, height)
# img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
#
#
# vis = np.concatenate([img2, img1, img1], axis=1)
#
# cv2.imshow("feed", vis)
# cv2.waitKey()
