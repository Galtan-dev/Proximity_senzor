import RPi.GPIO
import time

btn = RPi.GPIO.setmode(RPi.GPIO.BCM)

# starting variables definition
m = 0
dc = 10
channel_one = 17
channel_button = 27
channel_two = 13
channel_three = 19
channel_four = 26

# definition of input and output pins
RPi.GPIO.setup(channel_one, RPi.GPIO.IN)
RPi.GPIO.setup(channel_button, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_DOWN)
RPi.GPIO.setup(channel_two, RPi.GPIO.OUT)
RPi.GPIO.setup(channel_three, RPi.GPIO.OUT)
RPi.GPIO.setup(channel_four, RPi.GPIO.OUT)

# declaration of variables for control of dutycycle
p1 = RPi.GPIO.PWM(channel_two, 1000)
p2 = RPi.GPIO.PWM(channel_three, 1000)
p3 = RPi.GPIO.PWM(channel_four, 1000)
p1.start(dc)
p2.start(dc)
p3.start(dc)

# first definition of output pins
RPi.GPIO.output(channel_two, True)
RPi.GPIO.output(channel_three, True)
RPi.GPIO.output(channel_four, True)

# list of variables for dutycycle update
L = [p1, p2, p3]

# cycle which control which number is set and that relates to defined color
while True:
    # condition that control if senzor is triggered
    if RPi.GPIO.input(channel_button) == True:
        dc = 0
        if m == 2:
            m = 0
            # function for waiting between press of button for color change
            time.sleep(0.5)
        else:
            m += 1
            time.sleep(0.5)
    else:
        # condition that add 10 % to luminance if senzor is triggered
        if RPi.GPIO.input(channel_one) == False and dc != 100:
            dc += 10
            L[m].ChangeDutyCycle(dc)
            time.sleep(0.5)
        # condition that null dutycycle if is on 100 %
        elif dc == 100:
            dc = 0
        else:
            pass

