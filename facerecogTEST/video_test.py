import cv2
import face_recognition

video_cap = cv2.VideoCapture(1)

while True:
    ret, frame = video_cap.read()
    cv2.imshow('Video', frame)
    k = cv2.waitKey(20)
    if (k & 0xff ==ord('q')):
        break
video_cap.release()
cv2.destroyAllWindows()
