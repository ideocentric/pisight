#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gpio_triggers = [2,4,27,5,13]
gpio_echoes = [3,17,22,6,19]

for i in gpio_triggers:
  GPIO.setup(i, GPIO.OUT)
for i in gpio_echoes:
  GPIO.setup(i, GPIO.IN)


def distance(trigger,echo):
  # Set Trigger HIGH
  GPIO.output(trigger, True)

  # Set Trigger LOW after 0.01ms
  time.sleep(0.00001)
  GPIO.output(trigger, False)

  startTime = time.time()
  stopTime = time.time()

  # save startTime
  while GPIO.input(echo) == 0:
    startTime = time.time()

  # save stopTime
  while GPIO.input(echo) == 1:
    stopTime = time.time()

  # Calculate distance based on sound traveling feet/second
  timeElapsed = stopTime - startTime
  distance = (timeElapsed * 1125)/2

  return distance

if __name__ == '__main__':
  try:
    while True:
      for i in range(0, len(gpio_triggers)):
        dist = distance(gpio_triggers[i], gpio_echoes[i])
        print("%.1f ft " % dist)
        time.sleep(.1)

      print("----------")
      time.sleep(.5)

  except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
