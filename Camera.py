# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera

class Cam:
    def __init__(self, resolution = (640, 480), framerate = 32):
        self.resolution = resolution
        self.framerate = framerate
        self.rawCapture = PiRGBArray(camera, size=resolution)
