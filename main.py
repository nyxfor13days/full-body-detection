import cv2

body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

frame = cv2.imread('2.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

bodies = body_classifier.detectMultiScale(gray, 1.2, 3)

for (x, y, w, h) in bodies:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

cv2.imshow('Humans', frame)
cv2.waitKey()
cv2.destroyAllWindows()
