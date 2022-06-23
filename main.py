import cv2


class Detect:
    def __init__(self, body_classifier, camera):
        while True:
            ret, img = camera.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = body_classifier.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                self.detect(x, y, w, h, img)

            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

    def detect(self, x, y, w, h, img):
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        smile = smile_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 255, 255), 2)

        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy),
                          (sx + sw, sy + sh), (255, 0, 255), 2)


if __name__ == '__main__':
    body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    camera = cv2.VideoCapture(0)
    detect = Detect(body_classifier, camera)
