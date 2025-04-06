import cv2
import winsound


def main():
    cam = cv2.VideoCapture(0)
    # Tant que camer ouverte
    while cam.isOpened():
        # capture two frames(instances) to compare and detect the motion
        success, frame1 = cam.read()
        success, frame2 = cam.read()
        # compute the difference of both frames
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        # cv2.imshow('Difference', gray)
        # cv2.imshow('Blur', blur)
        # cv2.imshow('Tresh', thresh)
        # cv2.imshow('Dilate', dilated)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 8000:
                continue # ignorer les contours dont l'air rst < 8000
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            winsound.PlaySound('alert.wav' , winsound.SND_ASYNC)
        cv2.imshow('camera', frame1)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
