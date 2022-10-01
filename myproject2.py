from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("Backgound color changer with Color code")
root.config(bg='#'+'00'+'00'+'00')
def colorchanger(event):
    rr='%4s'%hex(redc.get())
    print(rr)
    gg='%4s'%hex(greenc.get())
    bb='%4s'%hex(bluec.get())
    rgbc=(rr+gg+bb).replace('0x',"")
    rgbc=rgbc.replace(" ","0")
    print(rgbc.replace(' ','0'))
    root.config(bg='#'+rgbc)
    l.config(text="Color code:#"+rgbc)
#red color Scale
redc=Scale(root,label="red",from_=0,to=255,orient=HORIZONTAL,tickinterval=25,
           length=1075,width=40,bg='red')#,command=colorchanger)
redc.pack(anchor='nw')
#Green color scale
greenc=Scale(root,label="green",from_=0,to=255,orient=HORIZONTAL,tickinterval=25,
           length=1075,width=40,bg='green')#,command=colorchanger)
greenc.pack(anchor='nw')
#Blue color scale
bluec=Scale(root,label="blue",from_=0,to=255,orient=HORIZONTAL,tickinterval=25,
           length=1075,width=40,bg='blue')#,command=colorchanger)
bluec.pack(anchor='nw')
#Label for  color code
l=Label(root,text='Color code:#000000',font=('Lucida 20 bold'))
l.pack(fill=X)
root.bind('<B1-Motion>',colorchanger)
root.mainloop()
