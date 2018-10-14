from BeepForDistance import DistanceMeasurement
from CameraManager import Camera

def main():
    cam = Camera()
    cam.initialise()
    dm = DistanceMeasurement()
    dm.initialise()
    while True:
	if ord("v"):
	   cam.start()
	dm.update()        

def run_program():
    pass

if __name__ == "__main__":
    main()
