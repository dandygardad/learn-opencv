# Import OpenCV
import cv2 as cv

# Masukkan gambar ke dalam variabel image
img = cv.imread('files/hyouka.JPG')

# Show shape gambar, 1 untuk width, 0 untuk height
print(img.shape[1] , 'x' , img.shape[0])

# Show gambar
cv.imshow('Hyouka scene', img)

# Membuat window gambar tidak langsung keluar
cv.waitKey(0)