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


 	def initialize(self):

		rawCapture = PiRGBArray(self.camera, size=(640, 480))
		time.sleep(0.1)

	def start(self):


# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
