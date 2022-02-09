import cv2 as cv

# Rescale
# Scale bisa diset dari 0.0 - 1.0
def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dim = (width, height)

    # Interpolation INTER_AREA menghasilkan gambar halus saat diperkecil
    hasil = cv.resize(frame, dim, interpolation=cv.INTER_AREA)
    return hasil

gambar = cv.imread('files/hyouka.JPG')

hasil_rescale = rescale_frame(gambar, .1)

# Melakukan perbandingan
cv.imshow('Hasil Resize', hasil_rescale)
cv.imshow('Hasil Ori', gambar)

cv.waitKey(0)