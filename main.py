#Lorawan V3 node
from time import sleep
#sleep(3)
print("main.py")
import utime
import struct
import urandom
from sx127x import TTN, SX127x
from ttn_eu import TTN_FREQS_STR
from machine import Pin, SPI
from config import *


__DEBUG__ = True

print("Setting TTNconfig")
ttn_config = TTN(ttn_config['devaddr'], ttn_config['nwkey'], ttn_config['app'], country=ttn_config['country'])
print("TTN Country:", TTN.country)

print("Setting device_spi")
device_spi = SPI(device_config['spi_unit'], baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

print("Setting lora")
lora = SX127x(device_spi, pins=device_config, lora_parameters=lora_parameters, ttn_config=ttn_config)
frame_counter = 0

def on_receive(lora, outgoing):
    payload = lora.read_payload()
    print("RX>>>", payload)

lora.on_receive(on_receive)
lora.receive()

print("Lora Configuration:")
print("Freq: ",TTN_FREQS_STR[0])
print(lora_parameters)

while True:
    __SAMPLE_DATA__ = False
    
    if __SAMPLE_DATA__:
        epoch = utime.time()
        temperature = urandom.randint(0,30)

        payload = struct.pack('@Qh', int(epoch), int(temperature))
        if __DEBUG__:
            print(type(payload))
    else:
        if __DEBUG__:
            print("encoding payload to CayenneLPP")
        #create a cayenneLPP payload
        #from lpp_frame import LppFrame
        # create empty frame
        #frame = LppFrame()
        # add some sensor data
        #frame.add_temperature(0, -1.2)
        #frame.add_humidity(6, 34.5)
        #if __DEBUG__:
        #    print(frame)
        # get byte buffer in CayenneLPP format
        #payload = bytes(frame)
        payload = bytearray([0x01, 0x67, 0x00, 0xff])

    if __DEBUG__:
        #print("%s: %s" % (epoch, temperature))
        print("payload:", payload)

    lora.send_data(data=payload, data_length=len(payload), frame_counter=frame_counter)
    lora.receive()
    
    frame_counter += 1
    print("framecounter:", frame_counter)
    print("rssi", lora.packet_rssi())
    print("snr", lora.packet_snr())

    for i in range(app_config['loop']):
        #print(".")
        lora.receive()
        utime.sleep_ms(app_config['sleep'])