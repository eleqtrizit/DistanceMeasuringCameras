import math
import settings as cfg

class DistanceMath:
    def __init__(self):
        print("Distance math class initiated.")

    # angle in degrees
    def convertPixelToAngle(self,pixel):
        return pixel * cfg.ratioOfPixelsToDegrees + cfg.startDegree

    def convertPixelToAngleCalibrate(self,pixel,startDegree):
        return pixel * cfg.ratioOfPixelsToDegrees + startDegree

    def calcDistance(self,angle):
        return cfg.distanceBetweenLenses * math.tan(math.radians(angle))

    # this is the function you want to call
    def getDistance(self,pixel):
        angle = self.convertPixelToAngle(pixel)
        print("Estimated angle: ", angle, " from Pixel: ", pixel)
        return self.calcDistance(angle)
