#!/usr/bin/env python
from time import sleep
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
            print "Taking down the curtain..."
            requests.delete(ENDPOINT, timeout=TIMEOUT)
            GPIO.output(PIN_LED, True)
        else:
            print "Putting up the curtain..."
            requests.post(ENDPOINT, timeout=TIMEOUT)
            GPIO.output(PIN_LED, False)
    except Exception:
        pass


switch()

while 1:
    print "Waiting..."
    GPIO.wait_for_edge(PIN_SWITCH, GPIO.BOTH)
    switch()