#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time
from smbus2 import SMBus as SMBus2, i2c_msg

def atmel_write(bus, device_address, memory_address, chunk):
    data = [memory_address >> 8, memory_address & 0xff]+map(ord, chunk)
    write = i2c_msg.write(device_address, data)
    bus.i2c_rdwr(write)
    time.sleep(0.005)

bus2 = SMBus2(1)
device_address = 0x50

offset = int(sys.argv[1])
data = sys.stdin.read()

i=0
while i < len(data):
    chunk = data[i]
    atmel_write(bus2, device_address, offset+i, chunk)
    i += 1
