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


def show_dashboard():
    try:
        requests.delete(ENDPOINT, timeout=TIMEOUT)
        GPIO.output(PIN_LED, True)
    except Exception:
        pass


def hide_dashboard():
    try:
        requests.post(ENDPOINT, timeout=TIMEOUT)
        GPIO.output(PIN_LED, False)
    except Exception:
        pass


GPIO.add_event_detect(PIN_SWITCH, GPIO.RISING, callback=show_dashboard, bouncetime=200)
GPIO.add_event_detect(PIN_SWITCH, GPIO.FALLING, callback=hide_dashboard, bouncetime=200)