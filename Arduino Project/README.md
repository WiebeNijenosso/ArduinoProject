# Checklist:
- [x] Scherm waar je de huidige meetwaarde af kan lezen.
- [x] Data verwerkt naar csv.
- [x] Seriele berichten versturen via de comport naar de arduino en een seriele response terugkrijgen en kunnen decoderen.
- [x] Sketch van de sensor aanpassen.

# Dingen die mij niet gelukt zijn:

- [ ] Makkelijk leesbare en aanpasbare code schrijven.
- [ ] Snelheid optimalisatie
- [ ] Filter maken voor berichten vanuit de sensor die niks te maken hebben met de ph.


# uitleg functies:
```py
import serial

def readserial(COMport):
    client = serial.Serial()
    client.port = string("Comport")
```
Start de pc/laptop client voor de communicatie met de arduino.

```py
# client wacht en luisterd naar berichten, stuurt ze naar packet.
if client.in_waiting():
    packet = client.readline()

# client stuurt een bericht naar de arduino.
msg = "abcDEFG123"
client.write(msg.encode("utf-8"))
```

```py
import tkinter as tk

# Start constructor voor appart scherm.
root = tk.Tk()

# Scherm instellingen
root.geometry("400x400")

# Update het scherm met nieuwe informatie:
root.update()
```
Voor de rest is het allemaal denk ik wel redelijk duidelijk.