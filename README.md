# 16bit-eeprom-i2c-smbus2
Write to and read from a 16bit EEPROM or FRAM with Python smbus2 over the i2c serial communication bus.

Tested on AT24C256 with 256 Kibibit (aka 32 KiB or 32768 Byte):

https://ww1.microchip.com/downloads/en/devicedoc/doc0670.pdf

## Requirements

https://pypi.org/project/smbus2/

```
pip install smbus2
```
If pip gives you troubles you can put sudo -H in front of it, if you know what you are doing.


## Usage

Make sure to chmod +x your files, usage is trivial:

```
./write-eeprom256.py empty32768
./read-eeprom256.py empty_output.txt
./write-eeprom256.py mlems_eeprom.jpg
./read-eeprom256.py mlems_output.jpg
```

## Benefits

Due to usage of smbus2 this is not only faster but also very reliable compared to the outdated smbus.

## License

Licensed under the WTFPL license.
