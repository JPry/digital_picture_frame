import RPi.GPIO as io
import time
import os

BUTTON_PIN = 18

def kill_slideshow():
    print "Killing slideshow!"
    os.system('pkill fbi')

def setup_gpio():
    io.setmode(io.BCM)
    io.setup(BUTTON_PIN, io.IN, pull_up_down=io.PUD_UP)

def unmount_drive():
    print "Unmounting USB drive..."
    os.system('umount /dev/sda1')
    print "Safe to remove USB drive!"

def main():
    setup_gpio()

    while True:
        button_state = io.input(BUTTON_PIN)
        if button_state == False:
            kill_slideshow()
            unmount_drive()
            time.sleep(0.5)

        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()
