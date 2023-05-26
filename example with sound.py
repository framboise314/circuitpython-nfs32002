import time
import board
import audiobusio
import audiocore
from circuitpython-nfs3200 import CC1101_NFS32002

# radio module
radio = CC1101_NFS32002(board.GP6, board.GP7, board.GP4, board.GP5, board.GP8)
# audio file
wave_file = open("message.wav", "rb") # 22 KHz sample rate (or less) and 16-bit, under 2MB
wave = audiocore.WaveFile(wave_file)
# audio output
audio = audiobusio.I2SOut(bit_clock=board.GP0, word_select=board.GP1, data=board.GP2)

# boucle principale
while True:
    message_recu = radio.wait_for_data()    
    audio.play(wave)
    while audio.playing:
        pass
    time.sleep(0.1) 
