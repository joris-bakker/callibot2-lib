# calliope mini CalliBot2 Simple API
from calliopemini import *
i2c.init()
import time

# -------------------------------------------
# Motoren
# -------------------------------------------

def motorL(dir, speed):
    if i2c.scan():
        buf = bytearray(3)
        buf[0] = 0x00   # linker Motor
        buf[1] = dir    # 0=vorwärts, 1=rückwärts
        buf[2] = min(255, max(0, speed))
        i2c.write(0x20, buf)

def motorR(dir, speed):
    if i2c.scan():
        buf = bytearray(3)
        buf[0] = 0x02   # rechter Motor
        buf[1] = dir
        buf[2] = min(255, max(0, speed))
        i2c.write(0x20, buf)

def stopL():
    motorL(0, 0) # Stoppe Linken Motor

def stopR():
    motorR(0, 0) # Stoppe rechten Motor

# -------------------------------------------
# Servos
# -------------------------------------------

def servo1(angle):
    if i2c.scan():
        angle = max(0, min(180, angle))
        i2c.write(0x20, bytearray([0x14, angle]))

def servo2(angle):
    if i2c.scan():
        angle = max(0, min(180, angle))
        i2c.write(0x20, bytearray([0x15, angle]))

# -------------------------------------------
# LEDs am CalliBot
# -------------------------------------------

def ledL(on):
    if i2c.scan():
        value = 1 if on else 0
        i2c.write(0x21, bytearray([0x00, value]))

def ledR(on):
    if i2c.scan():
        value = 2 if on else 0
        i2c.write(0x21, bytearray([0x00, value]))


# -------------------------------------------
# RGB LEDs
# -------------------------------------------

# LED-Index Mapping
RGB = {
    "LV": 1,  # links vorne
    "LH": 2,  # links hinten
    "RH": 3,  # rechts hinten
    "RV": 4   # rechts vorne
}

def rgbLed(led, r, g, b):  #  zum Beispiel "LV" als input eintragen
    if i2c.scan():
        idx = RGB[led]
        i2c.write(0x22, bytearray([0x03, idx, r, g, b]))

def rgbAll(r, g, b):
    if i2c.scan():
        for idx in range(1, 5):
            i2c.write(0x22, bytearray([0x03, idx, r, g, b]))

# -------------------------------------------
# Sensorsystem
# -------------------------------------------

def bumperL():
    val = 0
    if i2c.scan():
        val = i2c.read(0x21, 1)[0]
    return bool(val & 0x08)

def bumperR():
    val = 0
    if i2c.scan():
        val = i2c.read(0x21, 1)[0]
    return bool(val & 0x04)

def lineL():
    val = 0
    if i2c.scan():
        val = i2c.read(0x21, 1)[0]
    return not bool(val & 0x02)   # 0 = dunkel, 1 = hell

def lineR():
    val = i2c.read(0x21, 1)[0]
    return not bool(val & 0x01)

def distance_mm():
    buf = [0,0,0]
    if i2c.scan():
        buf = i2c.read(0x21, 3)
    return buf[1] * 256 + buf[2]

def distance_cm():
    return distance_mm() / 10


