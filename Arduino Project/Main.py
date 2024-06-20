# Arduino pH meter, project vruchtensap

# Imports:
import serial.tools.list_ports as listports
from Modules.ReadSerial import readSerial
import os

def portCheck():
    return list(listports.comports())

# Opstarten
print("pH meter vruchtenssappen project.\n")

COMPorts = portCheck()
print("Poortlijst:\n")

for p in COMPorts:
    print(p)

COMPorts = input("Vul hier je COM Poort in:\n")

os.system('cls') # clear terminal

print("Programma start nu op...\n")
packet = readSerial(COMPorts)
