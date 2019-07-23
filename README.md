# DistanceMeasuringCameras
Measure the distance of objects using a stereoscopic camera.

Using a stereoscopic camera purchased off Amazon (SVPRO 720p HD Webcam MJPEG &YUY2 Mini CMOS OV9712 USB Camera Module), I'm using simply trigonometry to measure the distance of an object.

The left camera is used as the basis of the measurement. How it works:

* The app will display the camera's view along with a cross hair to aim at the object you are trying to measure.  
* A segment from the center of the image will then be taken and searched for in the right camera's view.  
* Once found, the distance will be calculated using an angle-to-pixel ratio.

This was tested as working with a Jetson Nano and PC versions of Ubuntu 18/19.  The PC version will perform poorly unless OpenCV has been compiled with GPU optimizations or the cameras' resolution is turned down.  Higher resolutions allow larger segment sizes for searching.

Config file: settings.py

__You will need to know the field of view and the distance between the lenses.  __
