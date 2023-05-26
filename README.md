# circuitpython-nfs32002

Réimplémentation pour CircuitPython du protocole NF S 32-002 utilisé par les balises sonores des feux piétons. Permet de détecter le signal d'une télécommande à partir d'un module radio CC1101.

Le module utilise la librairie [CPY-CC1101](https://github.com/unixb0y/CPY-CC1101).

Exemple d'utilisation avec un Raspberry Pico :

```python=
import time
import board
from circuitpython-nfs3200 import CC1101_NFS32002

# radio module
radio = CC1101_NFS32002(board.GP6, board.GP7, board.GP4, board.GP5, board.GP8)

# boucle principale
while True:
    message_recu = radio.wait_for_data()    
    print("Ouistici !")
```
Câblage correspondant :
![plan de cablage](plan_balise_circuitpython.png)
