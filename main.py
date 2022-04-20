
from tkinter import *
from random import randint
import serial
serialPort = serial.Serial(port = "COM8", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    
serialString = ""                           # Used to hold data coming over UART

from PIL import ImageTk
root = Tk()
root.minsize(500, 500)
lab = Label(root)
lab.pack()

def update():
    # if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        x = serialString.decode('Ascii')
        print(x)
        lab['text'] = x
        root.after(1000, update) # run itself again after 1000 ms

# run first time
update()

root.mainloop()