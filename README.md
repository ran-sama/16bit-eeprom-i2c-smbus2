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
Added writing and reading from any possible offset (0-32767):
```
./write-offsets256.py 0 < yukarin.txt
./read-offsets256.py 0 7 | sha1sum
2d38e855276997a6fce97115cf4b856aca0227ce -
sha1sum yukarin.txt
2d38e855276997a6fce97115cf4b856aca0227ce yukarin.txt
```
You can use it as storage for cryptographic keys (clone a backup to a second EEPROM):

```shell
COUNTER=0
for run in {1..215}
do
  echo Writing to offset $COUNTER
  openssl genpkey -algorithm X448 | python write-offsets256.py $COUNTER
  let COUNTER+=152
done
let COUNTER=32680
for run in {1..11}
do
  echo Writing to offset $COUNTER
  printf "ransama9" | python write-offsets256.py $COUNTER
  let COUNTER+=8
done
```


## Benefits

Due to usage of smbus2 this is not only faster but also very reliable compared to the outdated smbus.

The first two (read/write) code samples are accelerated due to 32 byte blocks being read and written.

The latter two (with the offsets) perform much poorer. This is due to slow byte-by-byte operations.

## License

Licensed under the WTFPL license.
