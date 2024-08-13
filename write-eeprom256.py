#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time
from smbus2 import SMBus as SMBus2, i2c_msg

def atmel_write(bus, device_address, memory_address, chunk):
    data = [memory_address >> 8, memory_address & 0xff]+map(ord, chunk)
    write = i2c_msg.write(device_address, data)
    bus.i2c_rdwr(write)
    time.sleep(0.005)#EEPROMs can only write 1 block per 5ms

BUF_SIZE = 32
bus2 = SMBus2(1)
chip_size = 32768
device_address = 0x50

filename = str(sys.argv[1])
f=open(filename,"rb")

i=0
while i * BUF_SIZE < chip_size:
    chunk = f.read(BUF_SIZE)
    atmel_write(bus2, device_address, i*BUF_SIZE, chunk)
    i += 1
f.close()
