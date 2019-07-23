import cv2
import numpy as np
import time
import settings as cfg
import DistanceMath as dm


class StereoCameras:
    def __init__(self):
        cfg.startW = int((cfg.width/2) - cfg.halfSegment)
        cfg.endW = int(cfg.startW + cfg.segmentSize)
        cfg.startH = int((cfg.height/2) - cfg.halfSegment)
        cfg.endH = int(cfg.startH+cfg.segmentSize)
        self.millis = int(round(time.time() * 1000))
        self.dm = dm.DistanceMath()

    def drawRectangle(self, top_left, image):
        bottom_right = (top_left[0] + cfg.segmentSize,
                        top_left[1] + cfg.segmentSize)

        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 1)
        return image

    def findSegment(self, left, right):
        cfg.segment = np.zeros(
            (cfg.segmentSize, cfg.segmentSize), dtype='uint8')
        cfg.segment = left[cfg.startH:cfg.endH, cfg.startW:cfg.endW]

        centerStrip = np.zeros((cfg.segmentSize, cfg.width), dtype='uint8')
        centerStrip = right[cfg.halfHeight -
                            cfg.halfSegment:cfg.halfHeight+cfg.halfSegment, 0:cfg.halfWidth]

        res = cv2.matchTemplate(centerStrip, cfg.segment, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        centerStrip = self.drawRectangle(max_loc, centerStrip)

        centerW = int(max_loc[0]+cfg.halfSegment)
        centerH = int(max_loc[1]+cfg.halfSegment)
        cv2.circle(centerStrip, (centerW, centerH), 10, (0, 255, 0), 2)
        cv2.imshow("centerstrip", centerStrip)

        return (centerW, centerH)

    def go(self):
        leftCam = cv2.VideoCapture(cfg.camera1)
        while not leftCam.isOpened:
            print("Camera", cfg.camera1,
                  " failed to open.  Might be a USB power problem.  Might be a Windows problem (if using it).")
            time.sleep(0.2)
        print("Camera ", cfg.camera1, " opened.")

        rightCam = cv2.VideoCapture(cfg.camera2)

        while not rightCam.isOpened():
            print("Camera", cfg.camera2,
                  " failed to open.  Might be a USB power problem.  Might be a Windows problem (if using it).")
            time.sleep(0.2)

        print("Camera ", cfg.camera2, " opened.")

        leftCam.set(3, cfg.width)
        leftCam.set(4, cfg.height)
        rightCam.set(3, cfg.width)
        rightCam.set(4, cfg.height)

        while True:
            if not (leftCam.grab() and rightCam.grab()):
                print("No more frames.")
                break

            ret, leftFrame = leftCam.read()
            ret2, rightFrame = rightCam.read()

            leftCrossHairs = leftFrame.copy()

            leftCrossHairs[cfg.halfHeight, 0:cfg.width, 1] = 255
            leftCrossHairs[0:cfg.height, cfg.halfWidth, 1] = 255

            if not ret or not ret2:
                break

            # Wait for a key
            key = cv2.waitKey(1)
            if key == ord("q"):
                break

            center = self.findSegment(leftFrame, rightFrame)
            (w, h) = center
            distance = self.dm.getDistance(w)
            print("Distance: " + str(distance))
            text = "D: " + str(round(distance, 2))
            cv2.putText(leftCrossHairs, text, (75, 75),
                        cv2.FONT_HERSHEY_SIMPLEX, 3.0, (0, 255, 0))
            cv2.imshow("Left", leftCrossHairs)

        leftCam.release()
        rightCam.release()

        cv2.destroyAllWindows()
