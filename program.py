from BeepForDistance import DistanceMeasurement
from CameraManager import Camera

def main():
    cam = Camera()
    cam.initialise()
    dm = DistanceMeasurement()
    dm.initialise()
    while True:
        dm.update()
        cam.start()

def run_program():
    pass

if __name__ == "__main__":
    main()
