# Import OpenCV
import cv2 as cv
import numpy as np

# Buat blank
gambar = np.zeros((500,500,3), dtype="uint8")

# Gambar kotak
cv.rectangle(gambar, (0,0), (gambar.shape[1]//2, gambar.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('kotak', gambar)

# Gambar bulat
cv.circle(gambar, (gambar.shape[1]//2, gambar.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('bulat', gambar)

# Gambar garis
cv.line(gambar, (0,0), (500, 500), (255, 255, 255), thickness=3)
cv.imshow('garis', gambar)

cv.waitKey(0)