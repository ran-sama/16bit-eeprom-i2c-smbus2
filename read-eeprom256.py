#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from smbus2 import SMBus as SMBus2, i2c_msg

def atmel_read(BUF_SIZE, bus, chip_size, device_address):
    data = []
    f = open(filename, "w")
    for i in range(chip_size/BUF_SIZE):
        memory_address = i*BUF_SIZE
        offset = i2c_msg.write(device_address, [memory_address >> 8, memory_address & 0xff])
        chunk = i2c_msg.read(device_address, BUF_SIZE)
        bus.i2c_rdwr(offset, chunk)
        blob = list(chunk)
        for ch in map(chr,blob):
            f.write(ch)
    f.close()

BUF_SIZE = 32
bus2 = SMBus2(1)
chip_size = 32768
device_address = 0x50

filename = str(sys.argv[1])
atmel_read(BUF_SIZE, bus2, chip_size, device_address)
