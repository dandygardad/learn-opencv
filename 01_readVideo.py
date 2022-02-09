# Import OpenCV
import cv2 as cv

# Masukkan video ke variabel
video = cv.VideoCapture('files/videolagi.mp4')

print(cv.CAP_PROP_FRAME_WIDTH , 'x' , cv.CAP_PROP_FRAME_HEIGHT)
# Memunculkan video
while True:
    selesai, frame = video.read()
    
    cv.imshow('Webcam Laptop', frame)

    # Saat menekan tombol q maka akan break
    # waitKey bekerja dalam menghitung berapa fps diambil, 0 berarti freeze

    if cv.waitKey(30) & 0xFF == ord('q'):
        break

# Stop video
video.release()
cv.destroyAllWindows()
