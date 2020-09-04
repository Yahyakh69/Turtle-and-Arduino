"""
Controling Turtle with Arduino with 7 push buttons ,
each has a role ,one of them for example is to move forward when pressed
"""


import pyfirmata
from tkinter import * 

from turtle import * 

if __name__ == '__main__':
    
    #building a tkinter window that refers each button and its job
    root= Tk()

    T=Text(root,root.title("Controls"),height=8 ,width = 60)
    T.pack()

    T.insert(END,"Button1=Forward \n Button2=Backward\n Button3=Turn left\n Button4=Turn right\n Button5=Pen up\nButton6=Pen down\n Button7=Clear")
    
    
    
    board = pyfirmata.Arduino('Your Arduino Port')
    print("Communication Successfully started")
    
    # turtle pen width,speed,color
    width(2)
    speed(0)
    pencolor("blue")
    #assign each pin to a variable 
    button1=board.digital[2]
    button2=board.digital[3]
    button3=board.digital[4]
    button4=board.digital[5]
    button5=board.digital[6]
    button6=board.digital[7]
    button7=board.digital[8]
    
    
    
  
    it = pyfirmata.util.Iterator(board)
    it.start()
    # Buttons are inputs 
    button1.mode = pyfirmata.INPUT
    button2.mode = pyfirmata.INPUT
    button3.mode = pyfirmata.INPUT
    button4.mode = pyfirmata.INPUT
    button5.mode = pyfirmata.INPUT
    button6.mode = pyfirmata.INPUT
    button7.mode = pyfirmata.INPUT
     
    
    while True : 
        button_state1 =button1.read()
        button_state2 =button2.read()
        button_state3 =button3.read()
        button_state4 =button4.read()
        button_state5 =button5.read()
        button_state6 =button6.read()
        button_state7 =button7.read()
        
        if button_state1 == 1 :  #Forward 
            forward(5)
        if button_state2 == 1 :  #Backward 
            back(5)
        
        if button_state3 == 1 :  #Left 
            left(5)
        if button_state4 == 1 :  #Right 
            right(5)
        if button_state5 == 1 :  #Pen up 
            
            up()
        if button_state6 == 1 :  #Pen down 
            down()
        
        if button_state7 == 1 :  #clear 
        
            clear()
 
            
 
    
 
    
 
    
 
    
 
    
 
    
        
        
        



