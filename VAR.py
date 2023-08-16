import tkinter
from tkinter.constants import BOTTOM, CENTER, E, N
# from typing import Set
import warnings
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture("varvedio3.mp4")
flag = True
def play(speed):
    global flag
    print(f"Clicked on play and speed is {speed}")
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(430, 26, fill="orange red", font="Helvetica 30 bold", text="VAR Checking")
    flag = not flag
def pending(decision):
    frame = cv2.cvtColor(cv2.imread("varcheckinggoal.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    time.sleep(1)
    
    frame = cv2.cvtColor(cv2.imread("varcomplete.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    time.sleep(1)
    
    
    if decision == 'goal':
        decisionImg="vargoal.png"
    elif decision == 'no_goal':
        decisionImg="varnogoal.png"
    elif decision == 'penalty':
        decisionImg="varpenalty.png" 
    else:
        decisionImg="varnopenalty.png"
    
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

def goal():
    thread=threading.Thread(target=pending,args=("goal",))
    thread.daemon=1
    thread.start()
    print("Goal")
def no_goal():
    thread=threading.Thread(target=pending,args=("no_goal",))
    thread.daemon=1
    thread.start()
    print("No Goal")

def penalty():
    thread=threading.Thread(target=pending,args=("penalty",))
    thread.daemon=1
    thread.start()
    print("Penalty")

def no_penalty():
    thread=threading.Thread(target=pending,args=("no_penalty",))
    thread.daemon=1
    thread.start()
    print("No Penalty")

SET_WIDTH=900
SET_HEIGHT=450

window=tkinter.Tk()
window.title("Divyansh Vedio Assistant Refree")
cv_img=cv2.cvtColor(cv2.imread("var.png"), cv2.COLOR_RGB2BGR)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW, image=photo)
window.configure(bg='snow')
canvas.pack()

#playback control

btn=tkinter.Button(window,text="<==Previous(Slow)  ",font= ('CourierHelvetica 10 bold'),bg = "gray18",fg = "lime green",width=20, command=partial(play,-2))
btn.place(relx = 0, x =270, y = 475, anchor=CENTER)

btn=tkinter.Button(window,text="<==Previous(Fast)  " ,font= ('CourierHelvetica 10 bold'),bg="gray18",fg = "red2",width=20, command=partial(play,-15))
btn.place(relx = 0, x =95, y = 475, anchor=CENTER)

btn=tkinter.Button(window,text="  Next(Slow)==>",font= ('CourierHelvetica 10 bold'),bg = "gray18",fg = "lime green",width=20, command=partial(play,1))
btn.place(relx = 1, x =-270, y = 475, anchor=CENTER)

btn=tkinter.Button(window,text="  Next(Fast)==>",font= ('CourierHelvetica 10 bold'),bg = "gray18",fg = "red2",width=20, command=partial(play,15))
btn.place(relx = 1, x =-95, y = 475, anchor=CENTER)

btn=tkinter.Button(window,text="  Goal  ",font= ('CoCourier 10 bold'),bg = "lime green",fg = "gray1",width=15, command=goal)
btn.place(relx = 0, x=290, y = 510, anchor=CENTER)

btn=tkinter.Button(window,text="  No Goal  ",font= ('CoCourier 10 bold'),bg = "red2",fg = "gray1",width=15, command=no_goal)
btn.place(relx = 1, x=-290, y = 510, anchor=CENTER)

btn=tkinter.Button(window,text="  Penalty  ",font= ('CoCourier 10 bold'),bg = "lime green",fg = "gray1",width=15, command=penalty)
btn.place(relx = 0, x=290, y = 550, anchor=CENTER)

btn=tkinter.Button(window,text="  No Penalty  ",font= ('CoCourier 10 bold'),bg = "red2",fg = "gray1",width=15, command=no_penalty)
btn.place(relx = 1, x=-290, y = 550, anchor=CENTER)

btn=tkinter.Button(window,text="  Exit  ",width=15,font= ('CoCourier 10 bold'),bg = "gray18",fg = "red2", command=exit)
btn.pack(side=BOTTOM)

window.mainloop()