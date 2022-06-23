import cv2

body_classifier = cv2.CascadeClassifier('./haarcascade_fullbody.xml')
camera = cv2.VideoCapture(0)

while True:
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    body = body_classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in body:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
