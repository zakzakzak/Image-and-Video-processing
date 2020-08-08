# resize berdasarkan width dan height ke semua foto di dalam folder

import cv2
import time
import numpy as np



arr_dataset = []
for i in range(210):

    stri = 'D:/boku no projecto/python/image/cctv/frame_vid/an/img ('+str(i+1)+').jpg'
    img = cv2.imread(stri)

    resized_image = cv2.resize(img, (100, 100))
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    flat = gray.flatten().tolist()
    flat.append(0)
    arr_dataset.append(flat)



for i in range(160):

    stri = 'D:/boku no projecto/python/image/cctv/frame_vid/biyan/img ('+str(i+1)+').jpg'
    img = cv2.imread(stri)

    resized_image = cv2.resize(img, (100, 100))
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    flat = gray.flatten().tolist()
    flat.append(1)
    arr_dataset.append(flat)

print(len(arr_dataset))

# import pandas as pd
# pd.DataFrame(arr_dataset).to_csv("D:/boku no projecto/python/image/cctv/datasets_an_biyan.csv")
import csv
with open("D:/boku no projecto/python/image/cctv/datasets_an_biyan.csv", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in range(len(arr_dataset)):
         wr.writerow(arr_dataset[i])
