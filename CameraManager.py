# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

class Camera:
	def __init__(self, resolution =  (640, 480), framerate = 32):
            # initialize the camera and grab a reference to the raw camera capture
            self.camera = PiCamera()
            self.resolution = resolution
            self.framerate = framerate
            self.rawCapture = PiRGBArray(self.camera, size=(640, 480))

	def initialise(self):
            self.camera.framerate = self.framerate
            self.camera.resolution = self.resolution
            time.sleep(0.1)

	def start(self):
	    	# capture frames from the camera
            for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
				# grab the raw NumPy array representing the image, then initialize the timestamp
				# and occupied/unoccupied text
                image = frame.array

				# show the frame
                cv2.imshow("Frame", image)
                key = cv2.waitKey(1) & 0xFF

				# clear the stream in preparation for the next frame
                self.rawCapture.truncate(0)

                if key == ord("q"):
                   return
