import serial, binascii
import time

ser = serial.Serial(
    port = '/dev/serial0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)

ser.close()
ser.open()

while 1:
    print(ser)
    
    data = str(binascii.hexlify(ser.read(17)))
    
    print(data)
    
    if data != "":
        print("tag: {}".format(data[6:22]))
    else:
        print("No tag detected...")

    time.sleep(1)
