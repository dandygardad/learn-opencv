import cv2 as cv
import numpy as np

# Buat gambar kosong
gambar = np.zeros((500, 500, 3), dtype='uint8')

# Taruh text
cv.putText(gambar, 'Hello world!', (gambar.shape[1]//2, gambar.shape[0]//2), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), thickness=2)

cv.waitKey(0)