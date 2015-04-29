#!/usr/bin/env monkeyrunner  

import sys, time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

if (len(sys.argv) != 2):
    print 'Usage: monkeyrunner unlock_device.py <pin number>'
    sys.exit(0)

pin_number = int(sys.argv[1])
device     = MonkeyRunner.waitForConnection()

height = device.getProperty('display.height')
width  = device.getProperty('display.width')

coordinates_for = {
  '1': {'height': int(height) / 2, 'width': int(width) / 3},
  '2': {'height': int(height) / 2, 'width': int(width) / 2},
  '3': {'height': int(height) / 2, 'width': int(width) - int(width) / 3},
  '4': {'height': int(height) / 2 + int(height) / 8, 'width': int(width) / 3},
  '5': {'height': int(height) / 2 + int(height) / 8, 'width': int(width) / 2},
  '6': {'height': int(height) / 2 + int(height) / 8, 'width': int(width) - int(width) / 3},
  '7': {'height': int(height) / 2 + int(height) / 4, 'width': int(width) / 3},
  '8': {'height': int(height) / 2 + int(height) / 4, 'width': int(width) / 2},
  '9': {'height': int(height) / 2 + int(height) / 4, 'width': int(width) - int(width) / 3},
  '0': {'height': int(height) / 2 + int(height) / 3, 'width': int(width) / 2},
  'ok_button': {'height': int(height) / 2 + int(height) / 3, 'width': int(width) - int(width) / 3},
  'lock_icon': {'height': int(height) - int(height) / 8, 'width': int(width) / 2},
}

def slide_to_unlock():
    duration   = 0.5
    steps      = 3
    from_tuple = (coordinates_for['lock_icon']['width'], coordinates_for['lock_icon']['height'])
    to_tuple   = (int(width) / 2, int(height) / 5)
    
    return device.drag(from_tuple, to_tuple, duration, steps)

def input_pin(pin_number):
    for char in str(pin_number):
        time.sleep(0.2)
        device.touch(
            coordinates_for[char]['width'], 
            coordinates_for[char]['height'], 
            MonkeyDevice.DOWN_AND_UP
        )
    
    time.sleep(0.2)
    return device.touch(
        coordinates_for['ok_button']['width'], 
        coordinates_for['ok_button']['height'], 
        MonkeyDevice.DOWN_AND_UP
    )

def unlock_device():
    device.wake()
    slide_to_unlock()
    input_pin(pin_number)

if __name__ == '__main__':
    unlock_device()
