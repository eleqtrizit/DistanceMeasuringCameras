"""

math.degrees(math.atan(.75))
.75 is opp/adj

|\
| \
|__\  <-- 26 degrees

  ^-- 12 units

Solving for straight up side:
12*math.tan(math.radians(26))

"""
# set index numbers of the camera for OpenCV
# if you don't know these #'s for Linux, run:
# ls -ltrh /dev/video*
camera1 = 0
camera2 = 2

# PARAMETERS BELOW NEED TO BE SET BY YOU
# field of view for left lens, in centimeters
fieldOfView = 78

# distance between lenses in centimeters
distanceBetweenLenses = 6.25

# the degree in which objects disappear from the right camera's field of vision, left side
startDegree = 32.569
startDegree = 45.4

# resolution of camera
width = 1280  # 720p
height = 720  # 720p

# CALCULATED FOR USE BELOW
# we will not need to look past the middle of the right lens
centerView = fieldOfView/2

# same as center width.. for ease of reading
halfWidth = int(width/2)
halfHeight = int(height/2)

# the degree in which objects disappear from the right camera's field of vision, right side
endDegree = 180-startDegree
centerDegree = 90  # duh
fieldOfViewInDegrees = endDegree-startDegree

# ratio of pixels to degrees
ratioOfPixelsToDegrees = fieldOfViewInDegrees/width

# segment size to look for from one camera to the other
segmentSize = 128
halfSegment = int(segmentSize/2)
