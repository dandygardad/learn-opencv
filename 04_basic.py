from configparser import Interpolation
import cv2 as cv

gambar = cv.imread('files/example.jpg')
cv.imshow('Gambar', gambar)

# Convert to grayscale
gray = cv.cvtColor(gambar, cv.COLOR_BGR2GRAY)
cv.imshow('Gambar gray', gray)

# Convert to blur, kernel sizenya harus odd number
blur = cv.GaussianBlur(gambar, (7,7), cv.BORDER_DEFAULT);
cv.imshow('Gambar blur', blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Gambar canny', canny)

# Dilated
dilated = cv.dilate(gambar, (3,3), iterations=3)
cv.imshow('Gambar dilasi', dilated)

# Eroding (kebalikan dari dilated)
eroded = cv.erode(gambar, (3,3), iterations=3)
cv.imshow('Gambar eroded', eroded)

# Resize
# Gunakan cv.inter_area untuk perkecil tapi gunakan
# cv.INTER_CUBIC untuk diperbesar
resized = cv.resize(gambar, (500,500), interpolation=cv.INTER_AREA);
cv.imshow('Gambar resized', resized)

# Crop
crop = gambar[10:100, 100:200]
cv.imshow('Gambar crop', crop)

cv.waitKey(0)