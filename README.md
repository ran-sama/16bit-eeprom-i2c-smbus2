# 16bit-eeprom-i2c-smbus2
Write to and read from a 16bit EEPROM or FRAM with Python 3 smbus2 over the i2c serial communication bus.

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
./write-eeprom256.py onefill32
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

## Benchmarks

```
Full chip write, 32 byte chunks:
10.6536 seconds
Lifetime endurance at constant writing:
(1000000 * 10.6536) seconds = 4.05 months
Writing speed, 32 byte mode:
(10.6536 / 32768) seconds/bytes = 0.3251 ms/byte
```
```
Full chip write, 1 byte at a time:
193.202 seconds
Lifetime endurance at constant writing:
(1000000 * 193.202) seconds =  73.47 months
Writing speed, single-byte mode:
(193.202 / 32768) seconds/bytes = 5.8961 ms/byte
```

Subtracting the mandatory 5ms wait between operations, an overhead of 896.1 microseconds results for code execution and bus.

The endurance is much longer than any SSD can offer, as NAND flash is rated at mere 10,000 duty cycles. In a setting where you want to only store data long term (EEPROM data retention: 40 years) this is more than sufficient. FRAM modules can provide longer retention (151 years), more cycles (10^14) and unnoticeable (~90ns) write delays. Despite its name ferroelectric RAM is actually non-volatile.


## Benefits

Due to usage of smbus2 this is not only faster but also very reliable compared to the outdated smbus.

The first two (read/write) code samples are accelerated due to 32 byte blocks being read and written.

The latter two (with the offsets) perform much poorer. This is due to slow byte-by-byte operations.

## License

Licensed under the WTFPL license.
