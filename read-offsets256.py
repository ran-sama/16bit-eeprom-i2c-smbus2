#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from smbus2 import SMBus as SMBus2, i2c_msg

def atmel_read(BUF_SIZE, bus, device_address, memory_address, blocklen):
    data = []
    for i in range(blocklen):
        offset = i2c_msg.write(device_address, [memory_address >> 8, memory_address & 0xff])
        chunk = i2c_msg.read(device_address, BUF_SIZE)
        bus.i2c_rdwr(offset, chunk)
        blob = list(chunk)
        for ch in map(chr,blob):
            sys.stdout.write(ch)
            sys.stdout.flush()
        memory_address += 1

BUF_SIZE = 1
bus2 = SMBus2(1)
device_address = 0x50

offset1 = int(sys.argv[1])
blocklen = int(sys.argv[2])
atmel_read(BUF_SIZE, bus2, device_address, offset1, blocklen)
