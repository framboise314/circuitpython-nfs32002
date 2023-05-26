import time
import asyncio
import busio
from digitalio import DigitalInOut
from cpc.cpc import CC1101

class CC1101_NFS32002:

    self.syncword = "B4AA"
    self.baudrate = 5000
    self.frequency = 868300000
    def __init__(self, sclk, mosi, miso, csn, gdo0, gdo2):

        self.myspi = busio.SPI(clock=sclk, MOSI=mosi, MISO=miso)
        self.cs = DigitalInOut(csn)
        self.gdo0 = DigitalInOut(gdo0)
        self.radio = CC1101(spi=myspi, 
            cs=cs,
            gdo0=gdo0,
            baudrate=self.baudrate,
            frequency=self.frequency, 
            syncword=self.syncword)

        self.radio.setupRX()
        self.radio.setupCheck()
        time.sleep(0.2)
        self.radio.setSampleRate_4000()
        time.sleep(0.2)

    def get_sample_rate(self):
        return self.radio.get_sample_rate()

    def get_syncword(self):
        retrun self.syncword

    def wait_for_data(self): 
        data = radio.receiveData(0x16)
        return True
    
    async def wait_for_data(self):
        pass # TODO : implement async wait for data in cc1101 lib

