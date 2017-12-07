from Case import *
from go import *
from Sensor import *
from Turn import *
import time
import RPi.GPIO as GPIO

if __name__ == "__main__":
    pwm_setup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    try:
        while True:
            sensor = get()
            print(sensor)
            if sensor in right_turn_case :
                stop()
                print("right")
                go_forward_any(80)
                time.sleep(0.2)
                stop()
                rightPointTurn(100,0.1)
                while get()[3] == 0:
                    go_forward_any(80)
                    time.sleep(0.05)
                while get()[3] == 1:
                    rightPointTurn(70,0.1)
                    stop()
                    time.sleep(0.1)
                    get()
                stop()
                while get()[1] == 0:
                    leftPointTurn(100,0.1)
                    stop()
                    time.sleep(0.1)
                    get()
                time.sleep(1)
            elif sensor == [1,1,1,1,1]:
                stop()
                time.sleep(1)
                go_forward_any(80)
                time.sleep(0.1)
                while get()[2]!=0:
                    rightPointTurn(100,0.1)
                    stop()
                    time.sleep(0.1)
                    get()
                stop()
            elif sensor in left_turn_case:
                print("left")
                stop()
                while get()[0] == 0 :
                    go_forward_any(80)
		    time.sleep(0.3)
                    stop()
                    get()
                if get()[2] == 0 :
                    go_forward_any(80)
                    stop()
                    get()
                else :
                    leftPointTurn(70,0.1)
                    stop()
                    time.sleep(0.1)
                    while get()[4] == 1:
                        leftPointTurn(70,0.1)
                        stop()
                        time.sleep(0.1)
                        get()
                while get()[4] == 0 :
                        rightPointTurn(100,0.1)
                        stop()
                        time.sleep(0.1)
                        get()
                stop()
            elif sensor in forward_case:
                go_forward_any(80)
                time.sleep(0.005)
            elif sensor in right_case:
                rightSwingTurn(50,0.01)
            elif sensor in left_case:
                leftSwingTurn(60,0.01)
            elif sensor == [0,0,0,0,1] :
                go_forward(80,0.1)
                stop()
                time.sleep(0.2)
                get()
                if sensor == [0,0,0,0,1] :
                    stop()
                    go_forward_any(80)
                    time.sleep(0.1)
                    stop()
                    rightPointTurn(100,0.1)
                    while get()[4] == 0:
                        go_forward_any(80)
                        time.sleep(0.05)
                    while get()[3] == 1:
                        rightPointTurn(70,0.1)
                        stop()
                        time.sleep(0.1)
                        get()
                        stop()
                else :
                    continue
                while get()[0] == 0:
                    leftPointTurn(100,0.1)
                    stop()
                    time.sleep(0.1)
                    get()
                time.sleep(1)

            else:
                continue
    except KeyboardInterrupt:
        GPIO.output(MotorLeft_PWM, GPIO.LOW)
        # left motor will be stopped with function of ChangeDutyCycle(0)
        LeftPwm.ChangeDutyCycle(0)
        # the speed of right motor will be set as LOW
        GPIO.output(MotorRight_PWM, GPIO.LOW)
        # right motor will be stopped with function of ChangeDutyCycle(0)
        RightPwm.ChangeDutyCycle(0)
        # GPIO pin setup has been cleared
        GPIO.cleanup()
