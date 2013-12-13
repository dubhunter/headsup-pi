#!/usr/bin/env python
import requests
import RPi.GPIO as GPIO

ENDPOINT = 'https://headsup.twilio.com/v1/curtain'
TIMEOUT = 3

PIN_LED = 4
PIN_SWITCH = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def switch():
    try:
        if GPIO.input(PIN_SWITCH):
            requests.delete(ENDPOINT, timeout=TIMEOUT)
            GPIO.output(PIN_LED, True)
        else:
            requests.post(ENDPOINT, timeout=TIMEOUT)
            GPIO.output(PIN_LED, False)
    except Exception:
        pass


GPIO.add_event_detect(PIN_SWITCH, GPIO.BOTH, callback=switch, bouncetime=200)