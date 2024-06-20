# Grote globale functie.

# imports

# Seriele monitor communicatie:
import serial
# GUI:
import tkinter as tk
# Tijd:
import time

import re


# CSV Imports:
import csv
import datetime

def extractInteger(string):
    intergers = re.findall(r'\d+', string)
    output = ''.join(intergers)
    out =  int(output)
    return out

def readSerial(COMport):   
    client = serial.Serial(
        port=COMport,
        baudrate=115200,
        timeout=0.2,
        write_timeout=1
    )
    
    menu = input("Toets 1 om te calibreren. druk op iets anders om af te sluiten\n")
      
    if menu == '1':
        
        for i in range(20):
            if client.in_waiting:
                client.readline()
            time.sleep(0.2)
        
        msg = 'enterph\r\n'
        client.write(msg.encode('utf-8'))
        
        
        for I in range(3):
            if client.in_waiting:
                packet = client.readline()
                print(packet.decode('utf').replace("\r\n", ""))
            time.sleep(1)
            
        input("Druk op enter om verder te gaan met calibreren!")
       
        msg = 'calph\r\n'
        client.write(msg.encode('utf-8'))
        
        time.sleep(2)        
        
        for I in range(20):
            if client.in_waiting:
                packet = client.readline()
                print(packet.decode('utf').replace("\r\n", ""))
            time.sleep(1)
        
        msg = "exitph\r\n"
        client.write(msg.encode('utf-8'))
        
   
        root = tk.Tk()
        root.geometry("800x500")
        
        label = tk.Label(root, text="PH Meter, CTRL+C in de terminal om af te sluiten\npH:", font=("Arial",15))
        label.pack(pady=20)
    	
        switch = True

       
        fields = ["pH","Date","Mean"]
        meanList = [] # Word later gebruikt voor gemiddelde uit zoveel meetingen.
        
        with open("data.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fields)
            writer.writeheader()
            while switch == True:
                if client.in_waiting:
                    packet = client.readline()
                    print(packet.decode("utf").replace("\r\n", ""))
                    val = tk.Label(root, text=packet.decode("utf8").replace("pH:", ""), font=("Arial",12))
                    val.pack()
                    root.update()
                    val.after(1000,val.destroy())
                    
                    today = datetime.datetime.now()
                    timeformat = today.strftime("%d/%m/%y - %H:%M:%S")
                    
                    
                    #Gemiddelde uit x metingen:
                    plainTextPacket = packet.decode("utf").replace("\r\n","")
                    try:
                        numbers = extractInteger(plainTextPacket)
                    except:
                        print("Oopsie, geen nummers in deze meting. Naar de volgende")
                    
                    meanList.append(numbers)
                    
                    
                    if len(meanList) == 10:
                        print("10 objects in list, returning mean:")
                        mean = (sum(meanList)/len(meanList))/100
                        meanList = []
                        mean = round(mean)
                        
                    else:
                        mean = ""
                    
                    datadict = {"pH": packet.decode("utf").replace('pH:',"").replace("\r\n",""),
                                "Date": timeformat,
                                "Mean": mean
                            }
                    
                    print(meanList)
                    print(len(meanList))
                        
                    writer.writerow(datadict) # Staat nu in csv!
                    
                    
                    
                    
            