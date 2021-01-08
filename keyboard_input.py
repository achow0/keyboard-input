import tkinter as tk
from pynput import keyboard
 
def on_press(key):
    global pressedList,rdict,textList,boxList
    try:
        strkey=key.char
    except:
        strkey=str(key)
    print(key)
    if strkey not in pressedList:
        try:
            event=rdict[strkey]
        except:
            return
        pressedList.append(strkey)
        tmpList=rectangle_25(event[0],event[1],event[2],"black","white")
        textList.append(strkey)
        textList.append(tmpList[1])
        boxList.append(strkey)
        boxList.append(tmpList[0])
        
def on_release(key):
    global pressedList, textList, boxList
    try:
        strkey=key.char
    except:
        strkey=str(key)
    try:
        canvas.delete(textList[textList.index(strkey)+1])
    except:
        return
    canvas.delete(boxList[boxList.index(strkey)+1])
    textList.pop(textList.index(strkey)+1)
    textList.pop(textList.index(strkey))
    boxList.pop(boxList.index(strkey)+1)
    boxList.pop(boxList.index(strkey))
    pressedList.remove(strkey)
 
pressedList=[]
textList=[]
boxList=[]
listener=keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()
 
def rectangle_25(a,b,s, bgcolor,textcolor):
    return [canvas.create_rectangle(a,b,a+25,b+25,fill=bgcolor),canvas.create_text(a+12.5,b+12.5,text=s,fill=textcolor)]
 
root=tk.Tk()
root.resizable(width=False,height=False)
canvas=tk.Canvas(root,bg="white",height=150,width=325)
root.title("Keyboard Inputs")
root.wm_attributes("-topmost",-1)
rdict={"Key.left":[200,100,"←"],
       "Key.down":[225,100,"↓"],
       "Key.right":[250,100,"→"],
       "Key.up":[225,75,"↑"],
       "0":[75,100,"0"],
       "8":[75,75,"8"],
       "7":[50,75,"7"],
       "9":[100,75,"9"],
       "4":[50,50,"4"],
       "5":[75,50,"5"],
       "6":[100,50,"6"],
       "1":[50,25,"1"],
       "2":[75,25,"2"],
       "3":[100,25,"3"],
       "Key.enter":[100,100,"↵"],
       "Key.backspace":[50,100,"⌫"],
       "b":[225,25,"B"]}
for i in rdict:
    item=rdict[i]
    rectangle_25(item[0],item[1],item[2],None,"black")
canvas.pack()
root.mainloop()
