import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

leftmostled=16
leftlessled=18
centerled=22
rightlessled=40
rightmostled=32

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)


def trackingModule() :
    reli = []
    reli.append(GPIO.input(leftmostled))
    reli.append(GPIO.input(leftlessled))
    reli.append(GPIO.input(centerled))
    reli.append(GPIO.input(rightlessled))
    reli.append(GPIO.input(rightmostled))
    return reli

def get() :
    return [GPIO.input(leftmostled), GPIO.input(leftlessled), GPIO.input(centerled), GPIO.input(rightlessled), GPIO.input(rightmostled)]

