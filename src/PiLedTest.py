import RPi.GPIO as GPIO #import RPi.GPIO module
from hal import hal_led as led
from time import sleep

def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22, GPIO.IN) #set GPIO 22 as input
    GPIO.setup(24, GPIO.OUT)  # set GPIO 24 as output



def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        ret = 1
        set_output(24, 1)

    return ret

def set_output(led, level):
    GPIO.output(24, level)

def main():
    init()
    read_slide_switch()

if __name__ == "__main__":
    main()


