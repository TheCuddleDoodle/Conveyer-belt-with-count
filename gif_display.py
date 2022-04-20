from tkinter import *
import serial
serialPort = serial.Serial(port = "COM8", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


    
serialString = ""  

mywindow = Tk()
mywindow.title("Conveyer belt") 
mywindow.geometry("780x640") #This will be the window size (str)
mywindow.minsize(540, 420) #This will be set a limit for the window's minimum size (int)
mywindow.configure(bg="grey") #This will be the background color
inputtxt = Label(mywindow, height = 10,
                width = 80, text = "Input Text",
                bg = "light grey")
inputtxt.pack()



def update():
    serialString = serialPort.readline()
    x = serialString.decode('Ascii')
    if len(x) != 0:
        print(len(x))
        y = x
        inputtxt.config(text = y)
        mywindow.after(1000, update)
    else:
        mywindow.after(1000, update)
update()

#add gif at the center of window
# canvas = Canvas(mywindow, width = 500, height = 500)
# canvas.pack()
# my_image = PhotoImage(file='main_loop.gif')
# canvas.create_image(0, 0, anchor = NW, image=my_image)
mywindow.mainloop() #You must add this at the end to show the window