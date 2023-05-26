import time
import board
from circuitpython_nfs3200 import CC1101_NFS32002

# radio module
radio = CC1101_NFS32002(board.GP6, board.GP7, board.GP4, board.GP5, board.GP8)

# boucle principale
while True:
    message_recu = radio.wait_for_data()    
    print("Ouistici !")
    time.sleep(0.1)
