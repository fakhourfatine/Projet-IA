import cv2
import numpy as np
import pyautogui # Controls keyboard and mouse
import time
import winsound
red_lower = np.array([0, 100, 100])
red_upper = np.array([7, 255, 255])
orange_lower = np.array([10, 100, 100])
orange_upper = np.array([18, 255, 255])
blue_lower = np.array([100, 100, 100])
blue_upper = np.array([131, 255, 255])
green_lower = np.array([42, 100, 100])
green_upper = np.array([75, 255, 255])
yellow_lower = np.array([25, 100, 100])
yellow_upper = np.array([30, 255, 255])
black_lower = np.array([0, 0, 0])
black_upper = np.array([112, 255, 255])
def main():
    previous_y = 0
    previous_x = 0
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
        # We can also visualize the real part of the target color (from the original image)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        # Find contour
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours :
            area = cv2.contourArea(c)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(c) # w= width, h= hight
                print(f'{x} - {y}')
                cv2.rectangle(mask, (x,y), (x+w, y+h), (75, 100, 138), 4)
                cv2.rectangle(res, (x, y), (x + w, y + h), (75, 100, 138), 4)
                if y < previous_y:
                    print('Vers le haut')
                    pyautogui.press('up')
                    time.sleep(0)
                elif y > previous_y:
                    print('Vers le bas')
                    pyautogui.press('down')
                    time.sleep(0)
                else: continue
                previous_y = y
                if y == 0:
                    winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
        mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        stacked = np.hstack((frame,hsv, mask_bgr, res))
        # cv2.imshow('Camera BGR', frame)
        # cv2.imshow('Camera HSV', hsv)
        # cv2.imshow('Camera Mask', mask)
        # cv2.imshow('Camera BitWise', res)
        cv2.imshow('Trackbars', cv2.resize(stacked, None, fx=0.8, fy=0.8))
        cv2.waitKey(1)
if __name__ == '__main__':
    main()