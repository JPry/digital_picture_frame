import RPi.GPIO as io
import time
import os

SHUTDOWN_PIN = 23
HOLD_SECONDS = 3

def shutdown():
    os.system("sudo shutdown -h now")

def main():
    io.setmode(io.BCM)
    io.setup(SHUTDOWN_PIN, io.IN, pull_up_down=io.PUD_UP)
#   io.add_event_detect(SHUTDOWN_PIN, io.FALLING, callback=shutdown, bouncetime = 200)

    # Wait for the button to be pressed
    while True:
        button_state = io.input(SHUTDOWN_PIN)
        if button_state == False:
            # Require the button to be pressed for HOLD_SECONDS
            time.sleep(HOLD_SECONDS)
            new_state = io.input(SHUTDOWN_PIN)
            if new_state == False:
                shutdown()

        time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()
